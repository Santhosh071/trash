import cv2
import torch
import easyocr
import numpy as np

# Load YOLOv5 model (ensure you have the yolov5 directory cloned)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # You can use a custom model too

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify the language

# Open a connection to the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Use YOLOv5 to detect objects
    results = model(frame)

    # Process results
    for result in results.xyxy[0]:  # xyxy format
        x1, y1, x2, y2, conf, cls = result
        if int(cls) == 2:  # Assuming class '2' is for number plates
            # Draw rectangle around the detected number plate
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            # Extract the number plate region
            plate_region = frame[int(y1):int(y2), int(x1):int(x2)]
            
            # Preprocess the plate region for better OCR results
            plate_region_gray = cv2.cvtColor(plate_region, cv2.COLOR_BGR2GRAY)
            plate_region_gray = cv2.GaussianBlur(plate_region_gray, (5, 5), 0)
            _, plate_region_bin = cv2.threshold(plate_region_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Use EasyOCR to do OCR on the processed plate region
            results = reader.readtext(plate_region_bin)

            # Extract and display the text
            for (bbox, text, prob) in results:
                (top_left, top_right, bottom_right, bottom_left) = bbox
                top_left = tuple(map(int, top_left))
                bottom_right = tuple(map(int, bottom_right))
                cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
                cv2.putText(frame, text.strip(), (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show the frame with detections
    cv2.imshow('Number Plate Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
