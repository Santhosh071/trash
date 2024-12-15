Trash Detection System with Vehicle Number Plate Recognition
Overview
This project focuses on detecting trash and identifying vehicle number plates in real-time using computer vision and machine learning. The goal is to automate the process of issuing fines for plastic-related waste by detecting and reading number plates from images or video feeds.

Features
Trash Detection: Detects plastic waste using a pre-trained YOLO model.
Number Plate Detection: Identifies vehicle number plates using Haar Cascade and EasyOCR.
Email Notification: Sends a fine notification via email once a vehicle's number plate is detected.
Prerequisites
Before running the project, ensure you have the following dependencies installed:

Python (3.x)
OpenCV
EasyOCR
ultralytics/yolov5 for YOLO-based object detection
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/trash-detection.git
cd trash-detection
Install required packages:

bash
Copy code
pip install -r requirements.txt
Set environment variables for email configuration:

bash
Copy code
export SENDER_EMAIL="your_email@example.com"
export EMAIL_PASSWORD="your_email_password"
Ensure required model files are available:

models/best.pt (for trash detection)
Haar Cascade XML file for number plate detection
How to Run
Run the Trash Detection and Number Plate Detection System:

bash
Copy code
python main.py
The system will capture frames from the camera and detect plastic waste. If plastic is detected, it will then search for a vehicle's number plate.

Upon detecting a number plate, the system will send an email notification to the configured recipient.

Press q to exit the application at any time.

Customization
Email Configuration: Modify send_email function in main.py to change the recipient or email settings if necessary.

Model Paths: Ensure the paths to the required model files (best.pt, Haar Cascade) are correct in the respective scripts.

Plate Detection Methods: You can switch between different number plate detection methods (Haar Cascade or YOLO-based) as per your preference by modifying the number_plate_detect.py script.

Acknowledgements
This project utilizes YOLO for object detection and EasyOCR for text extraction from images.
Special thanks to the authors of the models and libraries used.
Contributing
If you'd like to contribute to this project or find any issues, please feel free to create a pull request or report them.

