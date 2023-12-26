import cv2

alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)

camera= cv2.VideoCapture(0)

while True:
    wd,img =camera.read()
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in face :
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0,),2)
    cv2.imshow("FACEDETECTION",img)
    key=cv2.waitKey(10)
    if key ==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()    
