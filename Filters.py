import cv2

path = r'c:\Users\PC\Downloads\WhatsApp Video 2023-11-21 at 7.59.19 PM.mp4'
video = cv2.VideoCapture(path)

while True:
    state,frame = video.read()
    if not state :break
    frame = cv2.resize(frame ,(0,0), fx =.35,fy =.35)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)

    cv2.imshow('video',frame)
    cv2.imshow('video b/w',gray)
    cv2.imshow('video rgb',rgb)
    cv2.imshow('video hsv',hsv)

# stacking frame
    s1 = cv2.hconcat([frame, cv2.merge([gray,gray,gray])])
    s2 = cv2.hconcat([rgb,hsv])
    f = cv2.vconcat([s1,s2])

    h,w,_ = f.shape
    #adding text
    f= cv2.putText(f'Original',(50,100),cv2.FONT_HARSHEY_SIMPLEX,2 (255,255,255),5)
    f = cv2.putText(f'Grayscale' , (w//2 + 50, 100),
                    cv2.FONT_HERSHEY_PLAIN)
    f = cv2.putText(f'RGB' , (50 ,h//2+100 )
                    cv2.FONT_HERSHY_SIMPLEX,2, (200,200,200),4)
    f = cv2.putText(f'Grayscale' , (w//2 + 50, 100))

    cv2.imshow('frame', f) 



    if cv2.waitKey(10) == ord('q'):
        break