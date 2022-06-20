# Hand tracking side project
import cv2                      # OpenCV, for opening the video camera
import mediapipe as mp          # for tracking the joints and key points on each hand

# create a caputre object (open the laptop camera)
cap = cv2.VideoCapture(0)       # initialize the webcam (default is camera 0)
drawer = mp.solutions.drawing_utils     # for drawing on the screen
styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as hands:   # creating the hands object (for detection)
    while True:
        check, frame = cap.read()

        if not check:
            continue      # if we can't read in the image

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # converting to RGB and mirroring
        # media pipe only takes RGB

        results = hands.process(frame)          # named tuples
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                drawer.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS, styles.get_default_hand_landmarks_style(), styles.get_default_hand_connections_style())

        goodFrame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_RGB2BGR)
        cv2.imshow('Hands', goodFrame)
        key = cv2.waitKey(1)
        if key == 27:               # ascii code for ESC
            break
        
    cap.release()                   # releasing the capture object
    cv2.destroyAllWindows()