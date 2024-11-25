import cv2
from ultralytics import YOLO
import queue
import time

# Assuming the frame_queue is defined in frame_receiver.py and imported here
import Kaoos_samling.receive_stream as receive_stream  # Import the frame queue

def perform_object_detection():
    # Load the YOLO model
    model_path = r"C:\MyComputerPartUSS\best.pt" 
    model = YOLO(model_path)

    while True:
        # Check if there are frames in the queue
        if not receive_stream.frame_queue.empty():
            frame = receive_stream.frame_queue.get()

            # Perform YOLO object detection
            results = model(frame)

            # Annotate detected objects
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                    confidence = box.conf[0]
                    class_id = int(box.cls[0])

                    # Draw bounding box and label on the frame
                    if confidence > 0.6:  # Display only if confidence > 0.6
                        label = f"{model.names[class_id]} {confidence:.2f}"
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Show the annotated frame
            cv2.imshow("Real-Time Object Detection", frame)

            # Press 'q' to exit the stream
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Close OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    perform_object_detection()
