# Trash Detection System with Vehicle Number Plate Recognition

## Overview
This project focuses on detecting trash and identifying vehicle number plates in real-time using computer vision and machine learning. The goal is to automate the process of issuing fines for plastic-related waste by detecting and reading number plates from images or video feeds.

## Features
- **Trash Detection**: Detects plastic waste using a pre-trained YOLO model.
- **Number Plate Detection**: Identifies vehicle number plates using Haar Cascade and EasyOCR.
- **Email Notification**: Sends a fine notification via email once a vehicle's number plate is detected.

## Prerequisites
Before running the project, ensure you have the following dependencies installed:
- Python (3.x)
- OpenCV
- EasyOCR
- `ultralytics/yolov5` for YOLO-based object detection

## How to Run

1. **Run the Trash Detection and Number Plate Detection System**:
   ```bash
   python main.py
   ```

2. The system will capture frames from the camera and detect plastic waste. If plastic is detected, it will then search for a vehicle's number plate.

3. Upon detecting a number plate, the system will send an email notification to the configured recipient.

4. Press `q` to exit the application at any time.

## Customization
1. **Email Configuration**: 
   Modify `send_email` function in `main.py` to change the recipient or email settings if necessary.
   
2. **Model Paths**:
   Ensure the paths to the required model files (`best.pt`, Haar Cascade) are correct in the respective scripts.

3. **Plate Detection Methods**:
   You can switch between different number plate detection methods (Haar Cascade or YOLO-based) as per your preference by modifying the `number_plate_detect.py` script.
