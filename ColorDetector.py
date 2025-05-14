import numpy as np
import cv2
from PIL import Image

from utility import get_HSV_limits
# from utility import in_range_HSV
# from utility import get_RGB_limits  
# from utility import in_range_rgb


red = [0,0,255]
yellow = [0,255,255]
blue = [255,0,0]
cap = cv2.VideoCapture(0)
while True:
    #HSV-----------------------------------------------------------------------
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Finding yellow objects
    HSV_yellow_lowerLim, HSV_yellow_upperLim = get_HSV_limits(color= yellow)

    HSV_yellow_booleanMask = cv2.inRange(hsvImage, HSV_yellow_lowerLim, HSV_yellow_upperLim)#in_range(hsvImage, yellow_lowerLim, yellow_upperLim)
    HSV_yellow_booleanMask_ = Image.fromarray(HSV_yellow_booleanMask)

    HSV_yellow_bbox = HSV_yellow_booleanMask_.getbbox()

    if HSV_yellow_bbox is not None:
        HSV_yellow_x1, HSV_yellow_y1, HSV_yellow_x2, HSV_yellow_y2 = HSV_yellow_bbox
        cv2.rectangle(frame, (HSV_yellow_x1,HSV_yellow_y1), (HSV_yellow_x2, HSV_yellow_y2), (0, 255, 255), 5)
        cv2.putText(frame, "yellow", (HSV_yellow_x1,HSV_yellow_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [0,255,255])

    #Finding blue objects
    HSV_blue_lowerLim, HSV_blue_upperLim = get_HSV_limits(color =blue)

    HSV_blue_booleanMask = cv2.inRange(hsvImage, HSV_blue_lowerLim, HSV_blue_upperLim)#in_range(hsvImage, blue_lowerLim,blue_upperLim)
    HSV_blue_booleanMask_ = Image.fromarray(HSV_blue_booleanMask)

    HSV_blue_bbox = HSV_blue_booleanMask_.getbbox()

    if HSV_blue_bbox is not None:
        HSV_blue_x1, HSV_blue_y1,HSV_blue_x2,HSV_blue_y2 = HSV_blue_bbox
        cv2.rectangle(frame, (HSV_blue_x1,HSV_blue_y1), (HSV_blue_x2, HSV_blue_y2), (255, 0, 0), 5)
        cv2.putText(frame, "blue", (HSV_blue_x1,HSV_blue_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [255,0,0])


    #BGR------------------------------------------------------------------------
    ret, image = cap.read()
    # define the list of boundaries

    # loop over the boundaries
    #for (lower, upper) in blue_boundaries:
    # create NumPy arrays from the boundaries
    BGR_blue_lower = np.array([86, 31, 4], dtype="uint8")
    BGR_blue_upper = np.array([220, 88, 50], dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    BGR_blue_booleanMask = cv2.inRange(image, BGR_blue_lower, BGR_blue_upper)
    BGR_blue_booleanMask_ = Image.fromarray(BGR_blue_booleanMask)

    BGR_blue_bbox = BGR_blue_booleanMask_.getbbox()

    if BGR_blue_bbox is not None:
        BGR_blue_x1, BGR_blue_y1,BGR_blue_x2,BGR_blue_y2 = BGR_blue_bbox
        cv2.rectangle(image, (BGR_blue_x1,BGR_blue_y1), (BGR_blue_x2, BGR_blue_y2), (255, 0, 0), 5)
        cv2.putText(image, "blue", (BGR_blue_x1,BGR_blue_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [255,0,0])
    
    #for (lower, upper) in yellow_boundries:
    # create NumPy arrays from the boundaries
    BGR_yellow_lower = np.array([62,90,190], dtype="uint8")
    BGR_yellow_upper = np.array([196,255,255], dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    BGR_yellow_booleanMask = cv2.inRange(image, BGR_yellow_lower, BGR_yellow_upper)
    BGR_yellow_booleanMask_ = Image.fromarray(BGR_yellow_booleanMask)

    BGR_yellow_bbox = BGR_yellow_booleanMask_.getbbox()

    if BGR_yellow_bbox is not None:
        BGR_yellow_x1, BGR_yellow_y1, BGR_yellow_x2, BGR_yellow_y2 = BGR_yellow_bbox
        cv2.rectangle(image, (BGR_yellow_x1,BGR_yellow_y1), (BGR_yellow_x2, BGR_yellow_y2), (0, 255, 255), 5)
        cv2.putText(image, "yellow", (BGR_yellow_x1,BGR_yellow_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [0,255,255])

    
    output = np.hstack([frame,image])




    cv2.imshow('HSV (Left) vs BGR (right)', output) #change back to frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
