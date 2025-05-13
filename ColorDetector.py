import numpy as np
import cv2
from PIL import Image

from utility import get_limits
from utility import in_range

red = [0,0,255]
yellow = [0,255,255]
blue = [255,0,0]
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Finding yellow objects
    yellow_lowerLim, yellow_upperLim = get_limits(color =yellow)

    yellow_booleanMask = in_range(hsvImage, yellow_lowerLim, yellow_upperLim)
    yellow_booleanMask_ = Image.fromarray(yellow_booleanMask)

    yellow_bbox = yellow_booleanMask_.getbbox()

    if yellow_bbox is not None:
        yellow_x1, yellow_y1, yellow_x2, yellow_y2 = yellow_bbox
        cv2.rectangle(frame, (yellow_x1,yellow_y1), (yellow_x2, yellow_y2), (0, 255, 255), 5)

    # #Finding red objects
    # red_lowerLim, red_upperLim = get_limits(color =red)

    # red_booleanMask = in_range(hsvImage, red_lowerLim, red_upperLim)

    # red_booleanMask_ = Image.fromarray(red_booleanMask)

    # red_bbox = red_booleanMask_.getbbox()

    # if red_bbox is not None:
    #     red_x1, red_y1,red_x2,red_y2 = red_bbox
    #     cv2.rectangle(frame, (red_x1,red_y1), (red_x2,red_y2), (0, 0, 255), 5)

    #Finding blue objects
    blue_lowerLim, blue_upperLim = get_limits(color =blue)

    blue_booleanMask = in_range(hsvImage, blue_lowerLim,blue_upperLim)
    blue_booleanMask_ = Image.fromarray(blue_booleanMask)

    blue_bbox = blue_booleanMask_.getbbox()

    if blue_bbox is not None:
        blue_x1, blue_y1,blue_x2,blue_y2 = blue_bbox
        cv2.rectangle(frame, (blue_x1,blue_y1), (blue_x2, blue_y2), (255, 0, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()