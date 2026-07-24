import cv2
import mediapipe as mp


class HandDetector:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(

            static_image_mode=False,

            max_num_hands=2,

            model_complexity=1,

            min_detection_confidence=0.70,

            min_tracking_confidence=0.70

        )

        self.drawer = mp.solutions.drawing_utils

        self.styles = mp.solutions.drawing_styles



    def process(self, frame):

        rgb = cv2.cvtColor(

            frame,

            cv2.COLOR_BGR2RGB

        )

        results = self.hands.process(rgb)

        hand_count = 0

        if results.multi_hand_landmarks:

            hand_count = len(results.multi_hand_landmarks)

            for hand in results.multi_hand_landmarks:

                self.drawer.draw_landmarks(

                    frame,

                    hand,

                    self.mp_hands.HAND_CONNECTIONS,

                    self.styles.get_default_hand_landmarks_style(),

                    self.styles.get_default_hand_connections_style()

                )

        return frame, hand_count
