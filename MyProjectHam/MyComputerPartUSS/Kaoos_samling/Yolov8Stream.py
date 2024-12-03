import cProfile
import cv2
from ultralytics import YOLO

def main():
    # Load the YOLO model
    model_path = r"C:\MyComputerPartUSS\best.pt" 
    model = YOLO(model_path)

    # Set the stream ngrok URL from Raspberry Pi
    stream_url = "https://hamsahashi.ngrok.dev"  

    # Access the video stream
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        exit()

    # Starter real-time object detection loop
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

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
        cv2.imshow("Hamsa's one and only Real-Time Object Detection", frame)

        # Press 'q' to exit the stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cProfile.run("main()")
