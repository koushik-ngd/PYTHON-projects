import cv2

camera = cv2.VideoCapture(0)

# here we load the haar cascade file which is downloaded on an xml file format on the same directory
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while True:
    success,frame = camera.read()
    faces = faceCascade.detectMultiScale(frame,1.2,4)
    for (x, y, w, h) in faces:
        
        ROI = frame[y:y+h, x:x+w]
        blur_face = cv2.GaussianBlur(ROI, (91,91),0) 
        # Insert ROI back into the image
        frame[y:y+h, x:x+w] = blur_face

        # To make a bounding box #*(Not Necessary)
        
        # if no face(s) are detected then display the message below
    if len(faces)==0:
        cv2.putText(frame,'Error detecting face!',(20,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255))
    cv2.imshow('Face Blur',frame)
    if cv2.waitKey(1) & 0xff==ord('e'):
        break
       
       
       
camera.release()
cv2.destroyAllWindows()