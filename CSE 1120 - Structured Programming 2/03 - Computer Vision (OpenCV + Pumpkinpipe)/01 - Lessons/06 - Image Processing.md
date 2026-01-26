# Overview

This section builds on earlier OpenCV skills by introducing **color spaces**, **geometric transformations**, **thresholding**, and **edge detection**. You will learn how images are represented internally, how to convert between different color formats, how to resize, move, and rotate images, and how to extract useful information like edges or high-contrast regions.

Assume the following setup is already completed. These imports give us access to OpenCV and NumPy, and the images are loaded into variables so they can be reused throughout the lesson.

```python
import cv2 as cv
import numpy as np

blue = cv.imread('blue.png')
green = cv.imread('green.png')
red = cv.imread('red.png')
grey = cv.imread('grey.png')
```

# Changing Color Space

Images in OpenCV are stored as arrays of pixel values. Each pixel contains one or more **channels**, and the meaning of those channels depends on the **color space** being used. A color space defines how color information is stored and interpreted.

OpenCV provides a single function, `cv.cvtColor()`, to convert an image from one color space to another. You always provide the input image and a conversion code that describes how the conversion should happen.

The general pattern for converting color spaces looks like this:

```python
# Make sure you have a reference image
input_img = red

# Convert the color with cv.cvtColor()
output_img = cv.cvtColor(input_img, cv.COLOR_BGR2RGB)
```

The conversion code always follows the pattern `cv.COLOR_<INPUT>2<OUTPUT>`.

## BGR (Blue, Green, Red)

BGR is the **default color space used by OpenCV**. Each pixel has three channels, representing blue, green, and red values. Even though RGB is more common in other programs, OpenCV loads images as BGR by default.

The table below shows common conversions that start from BGR:

| Code                | Input Color Space                       | Output Color Space                                                       |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_BGR2BGRA` | **BGR** – 3 Channels (Blue, Green, Red) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha)                          |
| `cv.COLOR_BGR2GRAY` | **BGR** – 3 Channels (Blue, Green, Red) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_BGR2HSV`  | **BGR** – 3 Channels (Blue, Green, Red) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |
| `cv.COLOR_BGR2RGB`  | **BGR** – 3 Channels (Blue, Green, Red) | **RGB** – 3 Channels (Red, Green, Blue)                                  |
| `cv.COLOR_BGR2RGBA` | **BGR** – 3 Channels (Blue, Green, Red) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha)                          |

## RGB (Red, Green, Blue)

RGB is the most common color space used by graphics software, image editors, and displays. Like BGR, it uses three channels, but the order of those channels is red, green, then blue.

These conversions are useful when working with other libraries that expect RGB instead of BGR:

| Code                | Input Color Space                       | Output Color Space                                                       |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_RGB2BGR`  | **RGB** – 3 Channels (Red, Green, Blue) | **BGR** – 3 Channels (Blue, Green, Red)                                  |
| `cv.COLOR_RGB2BGRA` | **RGB** – 3 Channels (Red, Green, Blue) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha)                          |
| `cv.COLOR_RGB2GRAY` | **RGB** – 3 Channels (Red, Green, Blue) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_RGB2HSV`  | **RGB** – 3 Channels (Red, Green, Blue) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |
| `cv.COLOR_RGB2RGBA` | **RGB** – 3 Channels (Red, Green, Blue) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha)                          |

## GRAY (Grayscale)

Grayscale images store only **brightness information**. Each pixel has a single channel, where lower values are darker and higher values are brighter. Grayscale images are commonly used for thresholding and edge detection because they remove color complexity.

The following conversions show how grayscale images can be converted back into multi-channel formats:

| Code                | Input Color Space                                                        | Output Color Space                              |
| ------------------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| `cv.COLOR_HSV2BGR`  | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **BGR** – 3 Channels (Blue, Green, Red)         |
| `cv.COLOR_HSV2BGRA` | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) |
| `cv.COLOR_HSV2RGB`  | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **RGB** – 3 Channels (Red, Green, Blue)         |
| `cv.COLOR_HSV2RGBA` | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) |

## HSV (Hue, Saturation, Value)

HSV separates color information into three more intuitive components: hue (the color itself), saturation (how intense the color is), and value (brightness). This makes HSV very useful when you want to isolate or adjust colors.

| Code                 | Input Color Space                 | Output Color Space                              |
| -------------------- | --------------------------------- | ----------------------------------------------- |
| `cv.COLOR_GRAY2BGR`  | **Gray** – 1 Channel (Brightness) | **BGR** – 3 Channels (Blue, Green, Red)         |
| `cv.COLOR_GRAY2BGRA` | **Gray** – 1 Channel (Brightness) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) |
| `cv.COLOR_GRAY2RGB`  | **Gray** – 1 Channel (Brightness) | **RGB** – 3 Channels (Red, Green, Blue)         |
| `cv.COLOR_GRAY2RGBA` | **Gray** – 1 Channel (Brightness) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) |

## BRGA (Blue, Green, Red, Alpha)

BGRA is the same as BGR but with an additional **alpha channel**. The alpha channel controls transparency, where lower values are more transparent and higher values are more opaque.

| Code                 | Input Color Space                               | Output Color Space                                                       |
| -------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_BGRA2BGR`  | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **BGR** – 3 Channels (Blue, Green, Red)                                  |
| `cv.COLOR_BGRA2GRAY` | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_BGRA2HSV`  | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |
| `cv.COLOR_BGRA2RGB`  | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **RGB** – 3 Channels (Red, Green, Blue)                                  |
| `cv.COLOR_BGRA2RGBA` | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha)                          |

## RGBA (RED, Green, Blue, Alpha)

RGBA is commonly used in graphics applications where transparency is required. It is identical to RGB, with an added alpha channel.

| Code                 | Input Color Space                               | Output Color Space                                                       |
| -------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_RGBA2RGB`  | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **RGB** – 3 Channels (Red, Green, Blue)                                  |
| `cv.COLOR_RGBA2BGR`  | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **BGR** – 3 Channels (Blue, Green, Red)                                  |
| `cv.COLOR_RGBA2BGRA` | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha)                          |
| `cv.COLOR_RGBA2GRAY` | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_RGBA2HSV`  | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |

# Geometric Transformations

Geometric transformations change the **shape, size, or position** of an image. OpenCV provides built-in tools for scaling, translating, and rotating images.

## Scale

Scaling changes the size of an image. You can do this by explicitly setting a new width and height, or by using scale factors.

In the first example, the image is resized to a specific pixel size:

```python
# Manual pixel size
width = 100 # 100 pixels
height = 100 # 100 pixels
small_blue = cv.resize(blue, (width, height))
```

In the second example, the image is scaled relative to its original size using factors:

```python
# Scaling factor
width_factor = 2
height_factor = 2
big_green = cv.resize(green, None, fx=width_factor, fy=height_factor)
```

## Translate

Translation moves an image horizontally and/or vertically. This is done using a **transformation matrix** and the `cv.warpAffine()` function.

The code below first determines the size of the output image, then defines how far the image should move in each direction.

```python
# In this example the image we create will be the same size as our start image
red_height, red_width, _ = red.shape
red_size = (red_width, red_height)

# Store translation amounts as variables for clarity
translate_x = 50
translate_y = 100

# Matrix used by OpenCV for translation (all you really need to know is that translate_x and translate_y are used here)
translation_matrix = np.float32([[1, 0, translate_x], [0, 1, translate_y]])

# cv.warpAffine() is used to create a new translated image
moved_red = cv.warpAffine(red, translation_matrix, red_size)
```

## Rotate

Rotation spins an image around a point, usually its center. OpenCV requires a rotation matrix that includes the rotation angle and scale.

This example rotates the image by 45 degrees around its center:

```python
# In this example the image we create will be the same size as our start image
green_height, green_width, _ = green.shape
green_size = (green_width, green_height)

# Store rotation for clarity
angle = 45

# Calculate rotation point (in this case the center of the image)
rotation_point = (green_width // 2, green_width // 2)

# Matrix used by OpenCV for rotation (all you really need to know is that rotation_point and angle are used here)
rotation_matrix = cv.getRotationMatrix2D(rotation_point, angle, 1)

# cv.warpAffine() is used to create a new rotated image
rotated_green = cv.warpAffine(green, rotation_matrix, green_size)
```

# Thresholding

Thresholding converts a grayscale image into a high-contrast image by deciding which pixels should be considered black or white. This technique is commonly used for object detection and image segmentation.

Thresholding only works on grayscale images.

![Grey](/Images/OpenCV%20Images/grey.png)

The code below first converts the image to grayscale, then applies a binary threshold.

```python
# Convert the image you want to threshold to greyscale
grey_img = cv.cvtColor(grey, cv.COLOR_BGR2GRAY)

# The threshold value is the number used to determine what is white and what is black. 
# Pixels less than this value will be black.
# Pixels greater than his value will be white.
threshold_value = 127

# Determines what color to display as "white" in the output.
# 255 will produce a threshold that is black (0) and white (255).
# A value less than 255 will result in a black and grey image
white = 255

# There are different types of thresholding that are outlined later. Binary is the most basic and intuitive one.
threshold_type = cv.THRESH_BINARY

# cv.threshold() returns an image. '_' is used to store the boolean for whether or not an image was successfully produced.
_, grey_threshold = cv.threshold(grey_img, threshold_value, white, threshold_type)
```

## Threshold Types

| Code                   | Description                                                                                                               | Output                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `cv.THRESH_BINARY`     | Pixels greater than `threshold_value` are *white*. Pixels les than `threshold_value` are *black*.                         | ![Binary](/Images/OpenCV%20Output%20Images/threshold_binary.png)              |
| `cv.THRESH_BINARY_INV` | Pixels greater than `threshold_value` are *black*. Pixels les than `threshold_value` are *black*.                         | ![Binary Inverted](/Images/OpenCV%20Output%20Images/threshold_binary_inv.png) |
| `cv.THRESH_TRUNC`      | Pixels less than `threshold_value` are *unchanged*. Pixels greater than `threshold_value` are set to *`threshold_value`*. | ![Truncate](/Images/OpenCV%20Output%20Images/threshold_truncate.png)          |
| `cv.THRESH_TOZERO`     | Pixels less than `threshold_value` are set to *black*. Pixels greater than `threshold_value` are *unchanged*.             | ![To Zero](/Images/OpenCV%20Output%20Images/threshold_to_zero.png)            |
| `cv.THRESH_TOZERO_INV` | Pixels greater than `threshold_value` are set to *black*. Pixels less than `threshold_value` are *unchanged*.             | ![Binary](/Images/OpenCV%20Output%20Images/threshold_to_zero_inv.png)         |

# Edge Detection

Edge detection finds areas of **rapid brightness change**, which often correspond to object boundaries. The Canny edge detector is one of the most common algorithms used for this purpose.

Before detecting edges, the image must be converted to grayscale. Two threshold values are then used to control how strong an edge must be to appear in the final result.

```python
# Convert the color space to grayscale.
grey_red = cv.cvtColor(red, cv.COLOR_BGR2GRAY)

# Define the weak and strong edges.
weak_edge = 100
strong_edge = 200

# Create the image that has edge detection.
edge_image = cv.Canny(grey_red, min_threshold, max_threshold)
```
