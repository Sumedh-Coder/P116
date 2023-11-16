import cv2
img=cv2.imread("C:/Users/ASUS/Downloads/P116/solar-system.jpg")

  
cv2.putText(img,"Sun",(50,100),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255))
cv2.putText(img,"Mercury",(100,160),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Venus",(200,160),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Earth",(300,160),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Mars",(400,160),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(500,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Saturn",(750,120),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Uranus",(950,140),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,140),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(255,255,255))
cv2.imwrite("solar-system.jpg",img)
cv2.imshow("solar-system",img) 
cv2.waitKey(0)