import cv2
import mediapipe as mp
from excerciseType import excerciseType
from utils import score_table

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)

counter = 0
status = True

def process_frame(frame, exercise_type="squat"):
    global counter, status

    frame = cv2.resize(frame, (800, 480))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame.flags.writeable = False

    results = pose.process(frame)

    frame.flags.writeable = True
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    try:
        landmarks = results.pose_landmarks.landmark
        counter, status = excerciseType(landmarks).calculate_exercise(
            exercise_type, counter, status)
    except:
        pass

    frame = score_table(exercise_type, frame, counter, status)

    mp_drawing.draw_landmarks(
        frame,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS
    )

    return frame