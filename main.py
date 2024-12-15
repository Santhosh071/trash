# main.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from trash_detect import TrashDetector
from number_plate_detect import NumberPlateDetector

def send_email(plate_number):
    sender_email = "your_email@example.com"  # Replace with your email
    receiver_email = "dasavikash.r2021@vitstudent.ac.in"
    password = "Vikash@2004"  # Replace with your email password

    subject = "Plastic Fine Notification"
    body = f"A fine of 500 Rs has been issued for plastic generated. Vehicle Number: {plate_number}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    # Initialize detectors
    trash_detector = TrashDetector('models/best.pt')
    number_plate_detector = NumberPlateDetector("C:\\Users\\user\\Downloads\\Trash_detection\\Trash_detection\\haarcascade_russian_plate_number.xml")

    # Start trash detection
    if trash_detector.detect_trash():
        # If plastic is detected, start number plate detection
        plate_number = number_plate_detector.detect_number_plate()
        if plate_number:
            send_email(plate_number)

if __name__ == "__main__":
    main()
