# Finger-Detection-and-Counter

## Description
This is a computer vision-based hand tracking system that detects and tracks fingers in real-time using OpenCV and MediaPipe. The program identifies hand landmarks and determines the number of fingers raised.

## Features
- **Real-time hand tracking** using OpenCV and MediaPipe.
- **Finger counting** to determine how many fingers are raised.
- **Interactive display** with an overlay showing the detected number of fingers.
- **Customizable detection settings** for confidence levels and number of hands.

## How It Works
1. The program initializes the webcam to capture video frames.
2. MediaPipe's hand tracking model detects hands and identifies key landmarks.
3. The system determines which fingers are raised based on landmark positions.
4. The number of raised fingers is displayed on the screen.
5. The program continues running until the user presses 'q' to exit.

## Requirements
Ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- MediaPipe (`mediapipe`)

## Installations
Clone the repository:

```bash
git clone https://github.com/your-username/Finger-Detection-and-Counter.git
cd Finger-Detection-and-Counter
