import numpy as np
import cv2 as cv
import timecode


def test_black_corners(img_array, offset_top, offset_bottom, offset_right, offset_left):
    if img_array[0 + offset_top, 0 + offset_left] == 17:  # TESTING UP LEFT CORNER
        return True
    if img_array[0 + offset_top, img_array.shape[1] - 1 - offset_right] == 17:  # TESTING UP RIGHT CORNER
        return True
    if img_array[img_array.shape[0] - 1 - offset_bottom, img_array.shape[1] - 1 - offset_right] == 17:  # DOWNRIGHT CORNER
        return True
    if img_array[img_array.shape[0] - 1 - offset_bottom, 0 + offset_left] == 17:  # TESTING DOWN LEFT CORNER
        return True
    return False




def test_video(path,start_frm, offset_up, offset_down, offset_right, offset_left):
    incidents = []
    try:
        cap = cv.VideoCapture(path)
    except:
        return False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        current_frame = cap.get(cv.CAP_PROP_POS_FRAMES)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        if current_frame >= start_frm:
            if test_black_corners(gray, offset_up, offset_down, offset_right, offset_left):

                if incidents == []:
                    incidents.append({
                        "start_frm": current_frame,
                        "end_frm": current_frame

                    })
                else:
                    if incidents[-1].get("end_frm") == (current_frame-1):
                        incidents[-1]["end_frm"] = current_frame
                    else:
                        incidents.append({
                            "start_frm": current_frame,
                            "end_frm": current_frame
                        })

        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    return path, incidents


def print_report(path,frame_rate,start_tc, incidents):
   print(f"Analyse du fichier: {path}")
   print(f"Time code de début: {start_tc}")
   h,m,s,f = timecode.tc_split(start_tc)
   start_frm = timecode.tc_to_frame(h,m,s,f,frame_rate)
   for incident in incidents:
        print(f" (!)  -> PB BLANKING DETECTE:  {timecode.frame_to_tc_02(incident.get('start_frm') -1 + start_frm, frame_rate)} à {timecode.frame_to_tc_02(incident.get('end_frm') + start_frm, frame_rate)} ")




if __name__ == '__main__':
    path, test= test_video('../VIDEO_TEST/TEST_CROP_ROTATE_RIGHT.avi',1.0,0,0,0,0)
    print_report(path,24,"01:00:00:00",test)
