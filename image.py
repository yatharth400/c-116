import cv2
img=cv2.imread('poster.jpg')
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
text="Space Times"
cv2.putText(img,text,(20,200),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255))
cv2.imshow("rocket",img)
cv2.waitKey(0)


















