import cv2
import os
import time
import argparse
from renderer import render_ascii

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=100)
    parser.add_argument("--mode", type=str, default="normal",
                        choices=["normal", "edge", "blocks"])
    args = parser.parse_args()

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Camera not found")
        return

    prev_time = time.time()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            ascii_frame = render_ascii(frame, args.width, args.mode)

            # FPS calculation
            current_time = time.time()
            fps = 1 / (current_time - prev_time)
            prev_time = current_time

            os.system("cls")

            print(f"AsciiVision | Mode: {args.mode} | FPS: {fps:.2f}")
            print(ascii_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()