import numpy as np
import cv2

# Open a video capture
cap = cv2.VideoCapture('barcelona.mp4')

# Read the first frame
ret, prev_frame = cap.read()
prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    # Read the next frame
    ret, next_frame = cap.read()
    if not ret:
        break
    
    next_frame_gray = cv2.cvtColor(next_frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate optical flow using Farneback method
    flow = cv2.calcOpticalFlowFarneback(prev_frame_gray, next_frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Convert flow to polar coordinates (magnitude and angle)
    magnitude, angle = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    
    # Normalize magnitude for visualization
    magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    magnitude_normalized = np.uint8(magnitude_normalized)
    
    # Create HSV image for visualization
    hsv = np.zeros((prev_frame.shape[0], prev_frame.shape[1], 3), dtype=np.uint8)
    hsv[..., 0] = angle * 180 / np.pi / 2
    hsv[..., 1] = 255
    hsv[..., 2] = magnitude_normalized
    
    # Convert HSV to BGR for displaying
    optical_flow_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    # Display the optical flow image
    cv2.imshow('Optical Flow', optical_flow_image)
    
    # Exit loop on 'q' press
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
    # Update previous frame
    prev_frame_gray = next_frame_gray.copy()

cap.release()
cv2.destroyAllWindows()