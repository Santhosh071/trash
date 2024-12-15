import cv2
import numpy as np
import pytesseract
import os

# Initialize variables
captured_image = None
extracted_text = ""

# Open a connection to the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'S' to capture the image and focus on the paper.")
print("Press 'A' to extract and display text from the captured image.")
print("Press 'B' to open the extracted text in Notepad.")
print("Press 'Q' to quit.")


def preprocess_for_ocr(image):
    """
    Pre-processes the image to improve text extraction.
    - Convert to grayscale
    - Denoise
    - Apply thresholding to make text clearer
    - Adjust contrast and brightness
    """
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Denoise the image to reduce any noise/artifacts
    denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

    # Adjust contrast and brightness
    adjusted = cv2.convertScaleAbs(denoised, alpha=1.5, beta=20)

    # Apply binary thresholding (simple thresholding to focus on text)
    _, thresholded = cv2.threshold(adjusted, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    return thresholded


while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if ret:
        cv2.imshow('Camera', frame)
    else:
        print("Error: Could not read frame.")
        break

    # Wait for user input
    key = cv2.waitKey(1) & 0xFF

    # If 'S' is pressed, capture and display the original image
    if key == ord('s'):
        captured_image = frame.copy()

        # Pre-process the captured image for better OCR
        processed_image = preprocess_for_ocr(captured_image)

        # Display the original and processed (thresholded) images
        cv2.imshow("Original Image", captured_image)
        cv2.imshow("Processed Image", processed_image)

        # Save images for reference
        cv2.imwrite("original_image.jpg", captured_image)
        cv2.imwrite("processed_image.jpg", processed_image)

        print("Captured images saved as 'original_image.jpg' and 'processed_image.jpg'.")

    # If 'A' is pressed, extract and display text from the captured image
    elif key == ord('a'):
        if captured_image is not None:
            # Perform OCR on the captured image with better config
            custom_config = r'--oem 3 --psm 6'  # OEM: 3 (Default), PSM: 6 (Assume a single uniform block of text)
            extracted_text = pytesseract.image_to_string(captured_image, config=custom_config)

            print("Extracted Text from Captured Image:")
            print(extracted_text)
        else:
            print("No image captured. Press 'S' to capture an image first.")

    # If 'B' is pressed, save the extracted text to a file and open in Notepad
    elif key == ord('b'):
        if extracted_text:
            with open("extracted_text.txt", "w") as text_file:
                text_file.write(extracted_text)
            print("Text saved as 'extracted_text.txt'")

            # Open the text file in Notepad
            os.system("notepad.exe extracted_text.txt")
        else:
            print("No text to display. Please press 'A' to extract text first.")

    # If 'Q' is pressed, quit
    elif key == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
