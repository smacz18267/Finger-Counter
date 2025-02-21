import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self, mode=False, hands_to_track=2,
                 detection_confidence=0.5, tracking_confidence=0.5) -> None:

        self.mode = mode
        self.hands_to_track = hands_to_track
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mp_hand = mp.solutions.hands
        self.hands = self.mp_hand.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.hands_to_track,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )

        self.mp_drawing_utils = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

    def find_hands(self, img, draw=True):
        self.result = self.hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if self.result.multi_hand_landmarks:
            if draw:
                for hand_landmark in self.result.multi_hand_landmarks:
                    self.mp_drawing_utils.draw_landmarks(
                        img,
                        hand_landmark,
                        self.mp_hand.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style()
                    )
        return img 
                
                  
