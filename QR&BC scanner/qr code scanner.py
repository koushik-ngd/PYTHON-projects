import cv2 
import numpy as np
from pyzbar.pyzbar import decode


web_cam = cv2.VideoCapture(0)

while True:
    success,frame = web_cam.read()
    for code in decode(frame):
        data = code.data.decode('utf-8')
        print("The code shows: ",data)
        pts = np.array([code.polygon],np.int32).reshape((-1,1,2))
        cv2.polylines(frame,[pts],True,(0,255,0),5)
        cv2.putText(frame,data,(code.rect[0],code.rect[1]),cv2.FONT_HERSHEY_PLAIN,0.9,(0,255,0),2)
        
    cv2.imshow('Image Frame',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break