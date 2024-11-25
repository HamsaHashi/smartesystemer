import cv2
import requests

def main():
    # Angi ngrok URL fra Raspberry Pi
    stream_url = "https://hamsahashi.ngrok.dev/video_feed"
    capture_url = "https://hamsahashi.ngrok.dev/capture"  # URL for bildeopptak

    # Åpne videostrøm
    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        print("Error: Could not open video stream.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Vis strømmen i et OpenCV-vindu
        cv2.imshow("Raspberry Pi Camera Stream", frame)

        # Sjekk for tastetrykk
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # Space-tasten for å ta bilde
            # Send POST-forespørsel til Raspberry Pi for å ta et bilde
            response = requests.post(capture_url)
            if response.status_code == 204:
                print("Bilde tatt og lagret på Raspberry Pi.")
            else:
                print("Feil ved bildeopptak.")
        elif key == ord('q'):  # 'q' for å avslutte
            break

    # Frigjør ressurser
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 