# Drowsiness-Detector
Drowsiness detector model developed using Computer Vision.

This solution can be used in cars to detect drowsiness of the driver while driving. 
By calculating Euclidean distance between eyes it is possible to say whether the driver's eyes are open or closed.
Accordingly Eye Aspect Ratio (EAR) is calculated and when EAR falls below a threshold value, an alarm sound is produced to alert the driver.

![alt text](https://github.com/pumpkinman008/Drowsiness-Detector/images/EyeLandmarkPoints.jpg)

Stack used: OpenCV, dlib, playsound, scipy, imutils.
