import cv2                      # for the webcam access
import mediapipe as mp          # for the finger recognition

def counter(frame, results):

    # need to continuosly draw the numbers to the screen
    # frame:    np.array that contains the current screen capture
    # results:  results from .process() within main
    # need to distinguish between left and right hand
