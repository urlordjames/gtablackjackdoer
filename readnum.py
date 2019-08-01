import cv2
import pytesseract
from PIL import Image

def getnum(location, invert):
    text = dogetnum(location, invert, 250)
    print(text)
    try:
        return intate(text)
    except:
        try:
            text = doggetnum(location, invert, 200)
            return intate(text)
        except:
            return 0

def dogetnum(location, invert, long):
    img = cv2.imread(location, cv2.IMREAD_GRAYSCALE)

    crop_img = img[25:60, 20:long]

    if invert:
        crop_img = 255-crop_img
    
    cv2.imwrite("cropped.png", crop_img)

    pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(crop_img)
    return text

def intate(text):
    newtext = ""
    for i in text:
        legit = False
        for n in range(0, 9):
            if i == str(n):
                legit = True
        if legit:
            newtext += i
    return int(newtext)
