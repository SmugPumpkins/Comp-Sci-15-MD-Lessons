# Overview

Loading and saving images is the first step in most OpenCV programs. Images are read from disk into memory, processed as NumPy arrays, and then either saved back to disk or displayed on screen. OpenCV provides simple functions for each of these tasks.

# Important Information

## Loading Images

Images are loaded using `cv.imread()`.

```python
img = cv.imread(cv.samples.findFile("starry_night.jpg"))
```

This reads the image file and stores it as a NumPy array. If the file cannot be found or opened, `img` will be `None`.

OpenCV loads color images using **BGR order**, not RGB.

### Loading Modes

You can control how the image is loaded by providing a second argument.
`IMREAD_COLOR` loads the image as a 3-channel color image. This is the default.
```python
img = cv.imread(cv.samples.findFile("starry_night.jpg"), IMREAD_COLOR)
```

`IMREAD_GREYSCALE` loads the image as a single-channel grayscale image.
```python
img = cv.imread(cv.samples.findFile("starry_night.jpg"), IMREAD_GREYSCALE)
```

`IMREAD_UNCHANGED` loads the image exactly as stored, including any alpha (transparency) channel.
```python
img = cv.imread(cv.samples.findFile("starry_night.jpg"), IMREAD_UNCHANGED)
```

The loading mode determines how many channels the image has and how it can be processed later.

## Saving Images

Images are saved using `cv.imwrite()`.

```python
cv.imwrite("starry_night.png", img)
```

The file format is determined by the file extension. If the file already exists, it will be overwritten.

Saving images is commonly used to store results or convert between formats.

## Displaying Images

Images can be shown in a window using `cv.imshow()`.

```python
cv.imshow("Display window", img)
```

This opens a window and displays the image stored in `img`. The program must keep running for the window to remain visible.
