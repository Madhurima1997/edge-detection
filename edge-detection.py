import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting to grayscale
    img = cv2.medianBlur(img,5) #removing noise
    final=cv2.Laplacian(img,cv2.CV_8U)*6 #edge detection
    cv2.imshow("Edge",final) #displaying image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
