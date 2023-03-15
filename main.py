import cv2

##함수 선언부
from canny import cannyEdge
from gray import grayScale 

##전역 변수부
src=None #원본 이미지 
dst1,dst2,dst3=None,None,None #영상처리 결과 

##메인 코드부
stc=cv2.imread("c:/images/picture01.jpg")#이미지 읽기
dst1=grayScale(stc)



cv2.imshow("Src",src) #화면출력
cv2.imshow("Dst1",dst1)


##마무리
cv2.waitKey(0)
cv2.destoryAllWindows()
