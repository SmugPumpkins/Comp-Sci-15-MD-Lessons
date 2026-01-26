# Overview

OpenCV can work with **video streams** the same way it works with images. A video stream is simply a sequence of images (frames) shown quickly one after another. These frames can come from a **live camera** or from a **saved video file**.

In OpenCV, video input is handled using the `VideoCapture` class. The same core ideas apply whether the source is a webcam or a video file: open the source, read frames in a loop, display or process each frame, and clean up when finished.

# Important Information

## Capturing Video

To capture live video from a camera, OpenCV uses a camera index. On most systems, `0` refers to the default webcam.

```python
cap = cv.VideoCapture(0)
```

This line attempts to connect to the camera and prepare it for reading frames.

Before continuing, it is important to check that the camera opened successfully.

```python
if not cap.isOpened():
    print("Cannot open camera")
    exit()
```

If the camera cannot be accessed, the program should stop. This prevents errors later when trying to read frames.

Once the camera is open, frames are read inside a loop.

```python
while True:
    success, frame = cap.read()

    if not success:
        print("Can't receive frame. Exiting ...")
        break
```

The `read()` function returns two values:

* `success`: a boolean indicating whether a frame was captured
* `frame`: the image data for that frame

If `success` is `False`, the video stream has stopped or failed.

Each frame can be displayed using `imshow()`.

```python
cv.imshow('Live Camera Feed', frame)
```

When video capture is finished, resources must be released.

```python
cap.release()
cv.destroyAllWindows()
```

Releasing the camera and closing windows is important so the camera is not locked by the program after it exits.

## Capturing Video Example

```python
# Import modules
import numpy as np
import cv2 as cv
 
# Start camera feed
cap = cv.VideoCapture(0)

# If there is no feed, quit the program
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Main loop
while True:
    # Check to see if the camera feed is still running and save the frame
    success, frame = cap.read()

    # If the camera feed stops, break out of the loop
    if not success:
        print("Can't receive frame. Exiting ...")
        break

    # Show the camera feed in a window called "Live Camera Feed"
    cv.imshow("Live Camera Feed", frame)

    # If ESC is pressed, break out of the loop
    if cv2.waitKey(0) == 27:
        break

# Release the camera feed
cap.release()

# Close all the created windows
cv.destroyAllWindows()
```

This program continuously reads frames from the camera and displays them in a window. The loop exits when the camera stops sending frames or when the ESC key is pressed.

## Loading a Video File

Instead of using a camera index, a video file path can be passed to `VideoCapture`.

```python
cap = cv.VideoCapture("test.avi")
```

This opens the video file and prepares it for frame-by-frame reading.

Frames are read in the same way as with a live camera.

```python
while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("Can't receive frame. Exiting ...")
        break
```

When the end of the file is reached, `success` becomes `False`, and the loop exits.

## Loaded Video File Example

```python
# Import modules
import numpy as np
import cv2 as cv
 
# Load the video file
cap = cv.VideoCapture("test.avi")

# Main loop
while cap.isOpened():
    # Check to see if the camera feed is still running and save the frame
    success, frame = cap.read()

    # If the camera feed stops, break out of the loop
    if not success:
        print("Can't receive frame. Exiting ...")
        break

    # Show the camera feed in a window called "Live Camera Feed"
    cv.imshow("Saved Video Feed", frame)

    # If ESC is pressed, break out of the loop
    if cv2.waitKey(0) == 27:
        break

# Release the camera feed
cap.release()

# Close all the created windows
cv.destroyAllWindows()
```

This example plays a saved video file frame by frame. The logic is nearly identical to live video capture, which is why OpenCV makes it easy to switch between camera input and video files.

Both live and saved video are processed one frame at a time, allowing the same techniques used for images to be applied to video streams.
