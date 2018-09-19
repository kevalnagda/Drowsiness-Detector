# Drowsiness-Detector
Drowsiness detector model developed using OpenCV and dlib.

This solution can be used in vehicles to detect drowsiness of the driver while driving.
By calculating Euclidean distance between the eyes it is possible to say whether the driver's eyes are open or closed.
Accordingly Eye Aspect Ratio (EAR) is calculated from Euclidean distance obtained.
If the Eye Aspect Ratio (EAR) of the driver crosses a threshold value then an alarm sound is generated to alert the driver.

 Below is the visual representation from Soukupová and Čech’s 2016 paper, [Real-Time Eye Blink Detection using Facial Landmarks:](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf)

![Alt text](EyeLandmarkPoints.jpg?raw=true "Eye Landmark Positions")

<b>Details of Libraries</b>
<ul>
  <li>Live webcam feed is obtained using OpenCV.</li>
  <li>dlib detector and predictor is used to obtain Frontal Facial Landmark points.</li>
  <li>Scipy is used for Euclidean distance calculation.</li>
  <li>Playsound is a python library that helps generate sound.</li>
</ul>

<b>Desciption of files</b>
<ul>
  <li>alarm.wav - Audio file used for alarm sound</li>
  <li>DrowsinessDetector.py - Python file used for Drowsiness Detection</li>
  <li>shape_predictor_68_face_landmarks.dat - Training data</li>
 </ul>
 
 Other factors like head posture of the driver or person wearing sunglasses have not been considered. 
