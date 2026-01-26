# Overview

OpenCV is a widely used library for **computer vision**, which is the field of computing that focuses on understanding images and video. It is commonly used for tasks such as image editing, face detection, motion tracking, and object recognition.

OpenCV was originally written in C++, which makes it very fast. OpenCV-Python allows you to use this powerful library through Python while still benefiting from the underlying C++ performance. This means you can write clear, readable Python code while OpenCV handles the heavy processing efficiently behind the scenes.

One of OpenCV’s strengths is that it works directly with **NumPy arrays**. Images are represented as arrays of numbers, which makes OpenCV easy to combine with scientific computing, data analysis, and visualization tools already used in Python.

# Install

To install OpenCV for Python, use `pip`:

```
pip install opencv-python
```

This command installs the core OpenCV functionality needed for image and video processing. It includes precompiled binaries, so no manual building or configuration is required.

After installation, OpenCV can be imported using the name `cv2`, which is the standard convention in Python programs.

# Test

The following test confirms that OpenCV is installed correctly and demonstrates some basic concepts.

```python
# Import modules
import cv2 as cv
import numpy as np

# Print current version of open cv to console
print("OpenCV:", cv.__version__)

# Create blank image 400 * 120 (height and width are reversed)
img = np.zeros((120, 400, 3), dtype=np.uint8)

# Add text to image
cv.putText(img, "OpenCV OK", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 3)

# Save image to confirm
cv.imwrite("hello.png", img)
```

If this script runs without errors and creates the image file, OpenCV-Python is installed and working correctly.

# Pictures Used
During this part of the module, the example code I have will use the following images, and calls them `red.png`, `green.png`, and `blue.png`. I would recommend downloading them to follow allong. You can either save them from this page or [download this folder](/Images/OpenCV%20Images/).

![Red](/Images/OpenCV%20Images/red.png)

![Green](/Images/OpenCV%20Images/green.png)

![Blue](/Images/OpenCV%20Images/blue.png)
