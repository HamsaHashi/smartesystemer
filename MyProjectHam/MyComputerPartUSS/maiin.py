import cProfile
from capture_frames import FrameGrabber
from detection import ObjectDetector

def main():
    # Initialize the frame grabber with your stream URL
    stream_url = "https://hamsahashi.ngrok.dev"
    frame_grabber = FrameGrabber(stream_url)
    frame_grabber.start()

    # Initialize the object detector with your model path
    model_path = r"C:\MyComputerPartUSS\best.pt"
    object_detector = ObjectDetector(model_path, frame_grabber, skip_frames=5)
    object_detector.start()

    # Keep the main thread running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        frame_grabber.stop()
        object_detector.stop()

if __name__ == "__main__":
    cProfile.run("main()")
