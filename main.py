import cv2
import numpy as np

video = str(input("input an mp4 file"))
capture = cv2.VideoCapture(video)

if (capture.isOpened()==False):
  print("something went wrong!!\ntry again")

while(capture.isOpened()):

  ret,frame=capture.read()
  if ret==True:
    cv2.imshow("Frame",frame)
    if cv2.waitkey(25) and 0xFF==ord("q"):
      break
  else:
    break
capture.release()
cv2.destroyAllWindows()