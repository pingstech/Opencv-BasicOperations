import cv2
import datetime

cap=cv2.VideoCapture(0)
print("Original Width:",cap.get(cv2.CAP_PROP_FRAME_WIDTH))       # Alınan görüntünün genişliğini gösterdik
print("Original Height:",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))     # Alınan görüntünün yüksekliğini gösterdik
cap.set(3,1280)                                                  # Alınan görüntünün genişliğini değiştirdik
cap.set(4,960)                                                   # Alınan görüntünün yüksekliğini değiştirdik    
print("New Width:",cap.get(cv2.CAP_PROP_FRAME_WIDTH))            # Alınan görüntünün genişliğini gösterdik
print("New Height:",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))          # Alınan görüntünün yüksekliğini gösterdik

while (cap.isOpened()):
    ret,frame=cap.read()

    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX                                                 # Görüntüye ekleyeceğimiz yazı fontunu belirledik
        text="Width:"+ str(cap.get(3)) + " Height:"+ str(cap.get(4))                  # Götüntüye ekleyeceğimiz yazıyı belirledik
        frame=cv2.putText(frame,text,(10,50),font,1,(0,255,0),1,cv2.LINE_AA)          # Götüntüye ekleme yaptık
        dateAndTime=str(datetime.datetime.now())                                      # Görüntüye tarih/zaman ekledik
        frame=cv2.putText(frame,dateAndTime,(10,80),font,1,(0,255,0),1,cv2.LINE_AA)   # Götüntüye ekleme yaptık
        cv2.imshow("Camera",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()