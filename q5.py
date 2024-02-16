import cv2
import pytesseract

# Path to the Tesseract executable 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_license_plate(image_path):
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Enhance text
    _, threshold_img = cv2.threshold(gray_img, 80, 255, cv2.THRESH_BINARY)

    license_plate_text = pytesseract.image_to_string(threshold_img)

    return license_plate_text.strip()


image_path = 'image6.2.jpg'
recognized_plate = recognize_license_plate(image_path)

print(f"License Plate: {recognized_plate}")
