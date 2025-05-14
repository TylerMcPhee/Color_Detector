import numpy as np
import cv2
from PIL import Image

from utility import get_HSV_limits
from utility import in_range_HSV
from utility import get_RGB_limits  
from utility import in_range_rgb

# #HSV -------------------------------
# red = [0,0,255]
# yellow = [0,255,255]
# blue = [255,0,0]
# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     #Finding yellow objects
#     yellow_lowerLim, yellow_upperLim = get_HSV_limits(color= yellow)

#     yellow_booleanMask = cv2.inRange(hsvImage, yellow_lowerLim, yellow_upperLim)#in_range(hsvImage, yellow_lowerLim, yellow_upperLim)
#     yellow_booleanMask_ = Image.fromarray(yellow_booleanMask)

#     yellow_bbox = yellow_booleanMask_.getbbox()

#     if yellow_bbox is not None:
#         yellow_x1, yellow_y1, yellow_x2, yellow_y2 = yellow_bbox
#         cv2.rectangle(frame, (yellow_x1,yellow_y1), (yellow_x2, yellow_y2), (0, 255, 255), 5)
#         cv2.putText(frame, "yellow", (yellow_x1,yellow_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [0,255,255])

#     #Finding blue objects
#     blue_lowerLim, blue_upperLim = get_HSV_limits(color =blue)

#     blue_booleanMask = cv2.inRange(hsvImage, blue_lowerLim, blue_upperLim)#in_range(hsvImage, blue_lowerLim,blue_upperLim)
#     blue_booleanMask_ = Image.fromarray(blue_booleanMask)

#     blue_bbox = blue_booleanMask_.getbbox()

#     if blue_bbox is not None:
#         blue_x1, blue_y1,blue_x2,blue_y2 = blue_bbox
#         cv2.rectangle(frame, (blue_x1,blue_y1), (blue_x2, blue_y2), (255, 0, 0), 5)
#         cv2.putText(frame, "blue", (blue_x1,blue_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [255,0,0])

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()

# cv2.destroyAllWindows()


#BGR ----------------------------------
cap = cv2.VideoCapture(0)

# running while loop just to make sure that
# our program keeps running until we stop it
while True:
    # capturing the current frame
    ret, frame = cap.read()

    # displaying the current frame
    cv2.imshow("frame", frame)

    # setting values for base colors
    b = frame[:, :, 0]  # Blue channel
    g = frame[:, :, 1]  # Green channel
    r = frame[:, :, 2]  # Red channel

    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    # displaying the most prominent color
    if b_mean > g_mean and b_mean > r_mean:
        print("Blue")
    elif g_mean > r_mean and g_mean > b_mean:
        print("Green")
    else:
        print("Red")

    # breaking the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releasing the video capture object and closing all windows
cap.release()
cv2.destroyAllWindows()
#---------------------------------Below attempts at BGR do not work
# #RGB
# red = [0, 0, 255]
# yellow = [0, 255, 255]
# blue = [255, 0, 0]

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     if not ret:
#         break

#     # Finding yellow objects
#     yellow_lower, yellow_upper = get_RGB_limits( color=yellow)
#     yellow_mask = cv2.inRange(frame_rgb, yellow_lower, yellow_upper)
#     yellow_mask_pil = Image.fromarray(yellow_mask)
    
#     yellow_bbox = yellow_mask_pil.getbbox()
#     if yellow_bbox is not None:
#         yellow_x1, yellow_y1, yellow_x2, yellow_y2 = yellow_bbox
#         cv2.rectangle(frame, (yellow_x1, yellow_y1), (yellow_x2, yellow_y2), (0, 255, 255), 5)
#         cv2.putText(frame, "yellow", (yellow_x1,yellow_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [0,255,255])

#     # # Finding red objects
#     # red_lower, red_upper = get_RGB_limits(color=red)
#     # red_mask = in_range_rgb(frame, red_lower, red_upper)
#     # red_mask_pil = Image.fromarray(red_mask)
    
#     # red_bbox = red_mask_pil.getbbox()
#     # if red_bbox is not None:
#     #     x1, y1, x2, y2 = red_bbox
#     #     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)

#     # Finding blue objects
#     blue_lower, blue_upper = get_RGB_limits(color=blue)
#     blue_mask = cv2.inRange(frame_rgb, blue_lower, blue_upper)
#     blue_mask_pil = Image.fromarray(blue_mask)
    
#     blue_bbox = blue_mask_pil.getbbox()
#     if blue_bbox is not None:
#         blue_x1, blue_y1, blue_x2, blue_y2 = blue_bbox
#         cv2.rectangle(frame, (blue_x1, blue_y1), (blue_x2, blue_y2), (255, 0, 0), 5)
#         cv2.putText(frame, "blue", (blue_x1,blue_y1-10), cv2.FONT_HERSHEY_SIMPLEX, .7, [255,0,0])

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# vid = cv2.VideoCapture(0)

# # running while loop just to make sure that
# # our program keeps running until we stop it
# while True:
#     # capturing the current frame
#     _, frame = vid.read()

#     # displaying the current frame
#     cv2.imshow("frame", frame)

#     # setting values for base colors
#     b = frame[:, :, 0]  # Blue channel
#     g = frame[:, :, 1]  # Green channel
#     r = frame[:, :, 2]  # Red channel

#     # computing the mean
#     blue_mask = cv2.threshold(b, 100, 255, cv2.THRESH_BINARY)[1]
#     green_mask = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)[1]
#     red_mask = cv2.threshold(r, 100, 255, cv2.THRESH_BINARY)[1]

    
    
#     blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for cnt in blue_contours:
#         if cv2.contourArea(cnt) > 100:
#             x, y, w, h = cv2.boundingRect(cnt)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), [255,0,0], 2)
#             cv2.putText(frame, "Blue", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [255,0,0])

#     green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for cnt in green_contours:
#         if cv2.contourArea(cnt) > 100:
#             x, y, w, h = cv2.boundingRect(cnt)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), [0,255,0], 2)
#             cv2.putText(frame, "Green", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0,255,0])

#     red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for cnt in red_contours:
#         if cv2.contourArea(cnt) > 100:
#             x, y, w, h = cv2.boundingRect(cnt)
#             cv2.rectangle(frame, (x, y), (x+w, y+h), [0,0,255], 2)
#             cv2.putText(frame, "Red", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0,0,255])

#     # breaking the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # releasing the video capture object and closing all windows
# vid.release()
# cv2.destroyAllWindows()


