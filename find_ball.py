import cv2
import numpy as np

def segmentaition(frame):

    img_ycrcb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    y,cr,cb = cv2.split(img_ycrcb)

    _, cb_th = cv2.threshold(cb, 90, 255, cv2.THRESH_BINARY_INV)
    cb_th = cv2.dilate(cv2.erode(cb_th, None, iterations=2), None, iterations=2)
    #cb_th = cv2.dilate(cb_th, None, iterations=2)

    return cb_th

def find_ball(frame,cb_th):

    cnts = cv2.findContours(cb_th, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    p2d = []

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 5:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
                
            p2d = center

    return p2d

def mian():

    while(1):

        _,frame1 = cap1.read()

        cb_th1 = segmentaition(frame1)

        pt1 = find_ball(frame1,cb_th1)

        if len(pt1) > 0:

            print("find ball")
            print("img_x: %d, img_y: %d" %(pt1[0],pt[1]))
            
        else:
            print("No ball")
                

        cv2.imshow('frame1',frame1)
        cv2.imshow('frame2',frame2)

        if cv2.waitKey(1) == ord('q'):
            break
    
    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()

        
