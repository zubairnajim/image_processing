import cv2


#boyutlandirma 
def boyutlandirma(img, x, y):
    return cv2.resize(img, (x, y))

