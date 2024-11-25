import cv2
import queue
import threading

# Define a thread-safe queue to store frames
frame_queue = queue.Queue(maxsize=10)  # Adjust maxsize as needed

def receive_frames(stream_url):
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Add frame to the queue if not full
        if not frame_queue.full():
            frame_queue.put(frame)

    # Release resources when done
    cap.release()

if __name__ == "__main__":
    # Start frame receiving in a separate thread
    stream_url = "https://hamsahashi.ngrok.dev"
    receiver_thread = threading.Thread(target=receive_frames, args=(stream_url,))
    receiver_thread.start()
    receiver_thread.join()
