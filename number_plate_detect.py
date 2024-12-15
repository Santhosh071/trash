import cv2
import easyocr
import os

# Path to the Haar Cascade file
harcascade = r"D:\Trash_detection\haarcascade_russian_plate_number.xml"

# Check if the Haar Cascade file exists
if not os.path.exists(harcascade):
    print("Haar Cascade file not found at the specified path.")
    exit()

# Load the Haar Cascade classifier
plate_cascade = cv2.CascadeClassifier(harcascade)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify the language

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0

# List to store recognized plate numbers
recognized_plates = []

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

            # Use EasyOCR to extract text from the number plate
            result = reader.readtext(img_roi)

            # Process the results
            for (bbox, text, prob) in result:
                text = text.strip()  # Clean up the text
                if text and len(text) >= 5:  # Check for at least 5 characters
                    recognized_plates.append(text)  # Store the recognized plate number
                    cv2.putText(img, text, (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 255), 3)  # Enhanced text display
                    print(f"Recognized Plate: {text}")  # Print recognized plate

                    # Terminate after recognizing a valid plate
                    if len(recognized_plates) == 1:  # Stop after first valid plate
                        cap.release()
                        cv2.destroyAllWindows()
                        exit()

            if cv2.waitKey(1) & 0xFF == ord('s'):  # Save if 's' is pressed
                cv2.imwrite("plates/scanned_img_" + str(count) + ".jpg", img_roi)
                cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
                cv2.imshow("Result", img)
                cv2.waitKey(500)
                count += 1

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit if 'q' is pressed
        break

# Save recognized plates to a text file
with open("recognized_plates.txt", "w") as f:
    for plate in recognized_plates:
        f.write(plate + "\n")

print("Recognized plates saved to recognized_plates.txt")

cap.release()
cv2.destroyAllWindows()
