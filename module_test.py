import cv2
import mediapipe as mp 
from hand_module import HandDetector

handDetector = HandDetector()

cap = cv2.VideoCapture(2)

while True:
    success, img = cap.read()

    img = handDetector.find_hands(img)
    land_mark_list = handDetector.find_position(img, draw=False)
    # print(land_mark_list)
    fingers_up = handDetector.fingers_up()
    # print(fingers_up)

    if fingers_up is not None:
        max_fingers_up_count = fingers_up.count(1)

        cv2.putText(img, f'Fingers up: {str(max_fingers_up_count)}', (100, 100), cv2.FONT_HERSHEY_COMPLEX, 
                    1, (0, 255, 255), 2)

    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
