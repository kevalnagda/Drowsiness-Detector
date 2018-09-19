from scipy.spatial import distance as dist
from imutils import face_utils
from threading import Thread
import numpy as np
import cv2
import dlib
import playsound
import imutils


EAR_THRESHOLD = 0.3
EAR_CONSEC_FRAMES = 40

COUNTER = 0
ALRAM_ON = False

alarm_path = 'alarm.wav'
predictor_path = 'shape_predictor_68_face_landmarks.dat'

def alarm_sound(path):
	playsound.playsound(path)

def eye_aspect_ratio(eye):
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	C = dist.euclidean(eye[0], eye[3])

	ear = (A + B) / (2.0 * C)

	return ear

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

(l_start, l_end) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(r_start, r_end) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

video_capture = cv2.VideoCapture(0)

while (True):
	_,frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	rects = detector(gray, 0)

	for rect in rects:
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		leftEye = shape[l_start:l_end]
		rightEye = shape[r_start:r_end]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)

		ear = (leftEAR + rightEAR) / 2.0

		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (255,0,0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (255,0,0), 1)

		if ear < EAR_THRESHOLD:
			COUNTER += 1

			if COUNTER >= EAR_CONSEC_FRAMES:

				if not ALRAM_ON:
					ALRAM_ON = True

					if alarm_path != "":
						t = Thread(target=alarm_sound, args=(alarm_path,))
						t.deamon = True
						t.start()

				cv2.putText(frame, "ALERT!", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
		
		else:
			COUNTER = 0
			ALRAM_ON = False
		
		cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	if key == ord("q"):
		break

cv2.destroyAllWindows()
video_capture.release()