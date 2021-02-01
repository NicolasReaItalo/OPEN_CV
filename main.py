import numpy as np
import cv2 as cv






cap = cv.VideoCapture('../VIDEO_TEST/TEST_YUV.avi')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)

   # print(gray[0,0])
   #  print(type(gray[0,0]))
   # print(type(cap.get(cv.CAP_PROP_POS_FRAMES)))
    print(gray[0, 0])
    if gray[0,0] == 0:

        print(f"Alerte {cap.get(cv.CAP_PROP_POS_FRAMES)}: noir coin supérieur gauche")

    if gray[1079, 0] == 0:
        print(f"Alerte {cap.get(cv.CAP_PROP_POS_FRAMES)}: noir coin inférieur gauche")

    if gray[0, 1997] == 0:
        print(f"Alerte {cap.get(cv.CAP_PROP_POS_FRAMES)}: noir coin supérieur droit")

    if gray[1079, 1997] == 0:
        print(f"Alerte {cap.get(cv.CAP_PROP_POS_FRAMES)}: noir coin inférieur droit")

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()