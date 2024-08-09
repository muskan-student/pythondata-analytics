import cv2 
cam = cv2.VideoCapture(0)
def no_action(x):
    pass
cv2.namedWindow('result')
cv2.createTrackbar('blocksize','result',2,10,no_action)
cv2.createTrackbar('ksize','result',3,10,no_action)
cv2.createTrackbar('k','result', 4, 100 ,no_action)
while cam.isOpened():
    state,frame = cam.read()
    if not state :
        break
    #logic
    gray  =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bs= cv2.getTrackbarPos('blocksize','result')
    ks= cv2.getTrackbarPos('ksize','result')
    k= cv2.getTrackbarPos('k','result')
    try:
        result = cv2.cornerHarris(gray,2,3,0.04)
        result = cv2.dilate(result,None)
        frame[result>0.01*result.max()] = [0,0,255]
    except:
        h, w, _ = frame.shape
        cv2.rectangle(
            img = frame,
            pt1 = (100,100),
            pt2 = (w-100,h-100),
            color = (0,0,255),
            thickness = -1
        )
    cv2.imshow("result" ,frame)
    if cv2.waitKey(10) == ord ('q'):
        break