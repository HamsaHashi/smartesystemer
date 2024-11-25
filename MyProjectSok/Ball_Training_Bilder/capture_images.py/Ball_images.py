import cv2

def main(): 
    cap = cv2.VideoCapture(2)  # ekstern camera (her brukte jeg iphone for å ta bilder siden vanlig ekstern kamera hadde dårlig kvalitet
    for i in range(1, 201):  # tar 200 pictures
        ret, frame = cap.read()
        if ret: 
            cv2.imwrite(f"image_{i}.jpg", frame)
            cv2.waitKey(200)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":  # corrected operator
    main()