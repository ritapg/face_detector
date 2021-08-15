from src.features.face_detector import *
import numpy as np
from glob import glob
import cv2

# import data
face_files = np.array(glob("data/test/*"))

# import model
face_cascade = cv2.CascadeClassifier('cv2/haarcascade_frontalface_alt.xml')

for i in range(len(face_files)):
    face_count = face_detector(face_files[i], face_cascade)
    if face_count is ():
            print("No faces found")
    for (x, y, w, h) in face_count:
            print("faces found:", len(face_count))
            img = cv2.imread(face_files[i], 1)

            #add rectangle & text
            cv2.rectangle(img, (x, y), (x + w, y + h), (169, 115, 73), 2)
            cv2.putText(img, 'Face', (x, y - 9), cv2.FONT_HERSHEY_PLAIN, 0.8, (169, 115, 73), 1)

            #show image
            cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('image', img)
            cv2.waitKey()



