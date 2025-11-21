# Face-Detection-on-Video-Stream-from-DJI-Tello-Drone-Python-OpenCV-Dlib-
Description: The goal of the project was to develop software capable of detecting human faces in real time on video streamed from a DJI Tello drone. Two detection methods were implemented and compared: Haar Cascades (OpenCV) and the HOG + SVM detector (Dlib).

Key features and implementation details:

Receiving and decoding the Tello H.264 video stream.

Real-time face detection using:
• Haar Cascade (OpenCV),
• HOG + SVM (Dlib).

Drawing detection bounding boxes on each frame.

Support for both recorded videos and live camera/drone stream.

Comparative analysis of detection performance (rotation, lighting, background).


Technologies:
Python, OpenCV, Dlib, Anaconda, Spyder, h264decoder, DJI Tello SDK.
