import cv2



def capture_image():
    video_capture = cv2.VideoCapture(0)

    
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  
    video_capture.set(cv2.CAP_PROP_FPS, 30)  


    
    ret, frame = video_capture.read()

    
    video_capture.release()

    
    return frame if ret else None


