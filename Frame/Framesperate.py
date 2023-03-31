import cv2

# Open video filea
cap = cv2.VideoCapture('video.mp4')

# Set frame rate
fps = float(input("enter the frame rate please"))
cap.set(cv2.CAP_PROP_FPS, fps)

# Set frame count and time limit
frame_count = 0
time_limit = 3

# Loop through video frames
while (cap.isOpened()):
    # Read frame
    ret, frame = cap.read()

    # Break if end of video or time limit exceeded
    if not ret or frame_count >= fps * time_limit:
        break

    # Save frame to file
    cv2.imwrite(f"storage/frame_{frame_count}.jpg", frame)

    # Increment frame count
    frame_count += 1

# Release video capture object
cap.release()
