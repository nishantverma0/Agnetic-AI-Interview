from deepface import DeepFace
import cv2

def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except:
        return "neutral"
