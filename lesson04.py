import cv2
import numpy as np

img=cv2.imread("messi5.jpg")

print(img.shape)                # Resmin satır, sütun ve kanal sayısını ekrana bastırıyoruz
print(img.size)                 # Resmin piksel sayısını ekrana bastırıyoruz
b,g,r=cv2.split(img)            # Resmin 3 kanallı olduğu için bunu "b", "g", "r" şeklinde 3 değişken içine atıyoruz
img=cv2.merge((b,g,r))          # cv2.split() ile ayırdığımız resmi birleştiriyoruz
cv2.imshow("Image",img)

ball=img[280:340,330:390]       # Resimdeki topun koordinatlarını "ball" isimli değişkenin içine attık
                                #--------------------------------------------------------------------------------------------
img[100:160,150:210]=ball       # Resimdeki belirlediğimiz koordinatlara "ball"un içindeki resmi yerleştirdik
                                # Burada önemli olarak "ball" içinden aldığımız koordinat ile yerleştireceğimiz yerin kordinatlarını özellikle ayarlamamız gerekiyor yoksa hata verir
                                # [x1:y1,x2:y2] ile yeni oluşturduğumuz [nx1:ny1,nx2:ny2] ile orantılı olmalı
                                #--------------------------------------------------------------------------------------------
cv2.imshow("Ball Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()