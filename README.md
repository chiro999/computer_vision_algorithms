# computer_vision_algorithms
Exploring computer vision algorithms with OpenCV including Optical Flow, Viola-Jones algorithm and Pose Estimation.

## Optical Flow

Optical flow is a technique used to describe image motion. It is usually applied to a series of images that have a small time step between them, for example, video frames. Optical flow calculates a velocity for points within the images, and provides an estimation of where points could be in the next image sequence. A popular application of Optical Flow is in Nvidia's 
Deep Learning Super Resolution 3 (DLSS3). DLSS 3 uses optical flow to produce motion interpolation providing an increase in frame rate. This is accelerated by a hardware ASIC called the Optical Flow Accelerator exclusive to the 40 series.

## Viola-Jones algorithm

The Viola-Jones algorithm is a fast and efficient object detection framework that was introduced by Paul Viola and Michael Jones in 2001. It is based on the idea of using Haar-like features and AdaBoost to detect faces and facial features in images. One of the key benefits of the Viola-Jones algorithm is its speed. Haar-like features are simple, rectangular features that are calculated by subtracting the sum of the intensity values of the pixels in the white region from the sum of the intensity values of the pixels in the black region.
AdaBoost is a machine learning algorithm that combines multiple weak classifiers to form a strong classifier.

## Pose estimation
Pose Estimation is a computer vision task where the goal is to detect the position and orientation of a person or an object. Usually, this is done by predicting the location of specific keypoints like hands, head, elbows, etc. in case of Human Pose Estimation.
