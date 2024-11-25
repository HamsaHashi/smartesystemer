import cv2
import numpy as np

class VideoSMottakerRTSP:
    def __init__(self, rtsp_url):
        # Initialize the RTSP stream URL
        self.rtsp_url = rtsp_url
        # Initialize the OpenCV video capture
        self.cap = cv2.VideoCapture(rtsp_url)

        if not self.cap.isOpened():
            print(f"Failed to open RTSP stream at {rtsp_url}")
            exit()

    # Capture and return frames from the RTSP stream
    def Motta_Frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame from RTSP stream.")
            return None
        return frame
    
    # Release the video capture resource
    def close(self):
        print("Closing RTSP stream...")
        self.cap.release()
        cv2.destroyAllWindows()

# Use the IP address of your Raspberry Pi RTSP stream
rtsp_url = 'rtsp://192.168.1.128:8554'  # Adjust if needed

# Initialize the RTSP stream receiver
video_receiver = VideoSMottakerRTSP(rtsp_url)

try:
    while True:
        # Get a frame from the RTSP stream
        frame = video_receiver.Motta_Frame()
        if frame is None:
            print("No frame received, exiting...")
            break

        # Display the frame
        cv2.imshow("RTSP Stream", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(f"Error during stream handling: {e}")
finally:
    video_receiver.close()
