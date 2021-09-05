import cv2

img=cv2.imread("lena.jpg")
img2=cv2.imread("teyze.jpg")
img2=cv2.resize(img2,(512,512))              # Eğer resmin satır ve sütun boyutları eşit olsaydı bunu yapmayacaktık, eşit olmadığı için ikinci resmi yeniden ölçeklendirdik
newImg=cv2.add(img,img2)                     # İki resmi üst üste ekledik
newImg2=cv2.addWeighted(img,0.7,img2,0.3,0)  # Burada yukarıdaki birleştirme komutu dışında iki fotoğrafın yüzde kaç ağırlıklı birleştirileceğini belirliyebiliyoruz
newImg3=cv2.addWeighted(img,0.3,img2,0.7,0)
cv2.imshow("Added Image",newImg)
cv2.imshow("Add Weighted Image",newImg2)
cv2.imshow("Add Weighted Image 2",newImg3)
cv2.waitKey(0)
cv2.destroyAllWindows()