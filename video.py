#library import
# object of videocapture class
# use it inside while loop
import os
import cv2 
import sys

path = r'c:\Users\PC\Downloads\WhatsApp Video 2023-10-18 at 8.25.16 PM.mp4'
if not os.path.exists(path):
    print(f'File not found : {path}')
    sys.exist(1)

cam = cv2.VideoCapture(path)
while True:
    state, frame= cam.read()
    if not state:
        break
    #resize
    frame1 = cv2.resize(frame,(1250,600))
    frame2 = cv2.resize(frame,(0,0),fx=1,fy = .85)
    cv2.imshow('Video Resized',frame1)
    cv2.imshow('Video resized by scale ',frame2)
    if cv2.waitKey(10) == ord('q'):
        break
