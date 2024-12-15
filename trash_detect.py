import cv2
from ultralytics import YOLO


# Load the YOLO model
model = YOLO('models/best.pt')

# Open a connection to the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Assuming the model has a method to get class names
class_names = model.names  # Get the class names from the model

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Perform prediction on the current frame
    results = model.predict(frame)

    # Display the results
    print(results[0])
    print("===============================")
    
    # Draw boxes and labels on the frame
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get the coordinates
        class_id = int(box.cls[0])  # Get class index
        label = f"{class_names[class_id]}: {box.conf[0]:.2f}"  # Get class name and confidence

        # Draw the rectangle
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        
        # Put the label above the box
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Show the frame with detections
    cv2.imshow('Camera Feed', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
