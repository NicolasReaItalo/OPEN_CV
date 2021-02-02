

cap = cv.VideoCapture('../VIDEO_TEST/TEST_LPR.avi')

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # print(gray.shape)
    cv.imshow('frame', gray)
    if test_black_corners(gray,0,0,0,0):
        print(f" {timecode.frame_to_tc_02(cap.get(cv.CAP_PROP_POS_FRAMES), 24)}  :  NOIR DETECTE")

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
