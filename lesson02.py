import cv2

cap=cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,frame=cap.read()                        # ret, "True" veya "False" değeri alır
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # Alınan görüntünün genişliğini gösterdik
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # Alınan görüntünün yüksekliğini gösterdik
    cv2.imshow('Camera',frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Camera',gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()