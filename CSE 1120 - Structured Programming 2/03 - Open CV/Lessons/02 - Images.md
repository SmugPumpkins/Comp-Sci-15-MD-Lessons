# Overview

Loading and saving images is the first step in most OpenCV programs. Images are read from disk into memory, processed as NumPy arrays, and then either saved back to disk or displayed on screen. OpenCV provides simple functions for each of these tasks.

# Important Information

## Loading Images

Images are loaded using `cv.imread()`.

```python
img = cv.imread("red.png")
```

This reads the image file and stores it as a NumPy array. If the file cannot be found or opened, `img` will be `None`.

OpenCV loads color images using **BGR order**, not RGB.

### Loading Modes

You can control how the image is loaded by providing a second argument.
`IMREAD_COLOR` loads the image as a 3-channel color image. This is the default.
```python
img = cv.imread("red.png", IMREAD_COLOR)
```

`IMREAD_GREYSCALE` loads the image as a single-channel grayscale image.
```python
img = cv.imread("red.png", IMREAD_GREYSCALE)
```

`IMREAD_UNCHANGED` loads the image exactly as stored, including any alpha (transparency) channel.
```python
img = cv.imread("red.png", IMREAD_UNCHANGED)
```

The loading mode determines how many channels the image has and how it can be processed later.

## Saving Images

Images are saved using `cv.imwrite()`. When saving an image, you create the name and file extension, and then the source image you are saving.

```python
cv.imwrite("red_copy.png", img)
```

The file format is determined by the file extension. If the file already exists, it will be overwritten.

Saving images is commonly used to store results or convert between formats.

## Displaying Images

Images can be shown in a window using `cv.imshow()`. The string in this function is the name of the window

```python
cv.imshow("Display window", img)
```

This opens a window and displays the image stored in `img`. The program must keep running for the window to remain visible.

### Example
You can even open multiple images at once!
```python
# Import library
import cv2 as cv

# Load images
blue = cv.imread('blue.png')
green = cv.imread('green.png')
red = cv.imread('red.png')

# Show images
# Important: All windows need a different name or this will not work!
cv.imshow('blue', blue)
cv.imshow('red', red)
cv.imshow('green', green)

# Keep showing until keypress
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()
```
