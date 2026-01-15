https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html

# Overview


Assume the following set up for this section:
```python
import cv2 as cv
import numpy as np

blue = cv.imread('blue.png')
green = cv.imread('green.png')
red = cv.imread('red.png')
```
# Changing Color Space
Color spaces are described below.

The syntax is always like this:
```python
# Make sure you have a reference image
input_img = red

# Convert the color with cv.cvtColor()
output_img = cv.cvtColor(input_img, cv.COLOR_BGR2RGB)
```

## BGR (Blue, Green, Red)
This is the default color space.
3 Channels per pixel, one for blue, green, and red

| Code                | Input Color Space                       | Output Color Space                                                       |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_BGR2BGRA` | **BGR** – 3 Channels (Blue, Green, Red) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha)                          |
| `cv.COLOR_BGR2GRAY` | **BGR** – 3 Channels (Blue, Green, Red) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_BGR2HSV`  | **BGR** – 3 Channels (Blue, Green, Red) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |
| `cv.COLOR_BGR2RGB`  | **BGR** – 3 Channels (Blue, Green, Red) | **RGB** – 3 Channels (Red, Green, Blue)                                  |
| `cv.COLOR_BGR2RGBA` | **BGR** – 3 Channels (Blue, Green, Red) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha)                          |

## RGB (Red, Green, Blue)
Common color space with many other programs. Most graphics programs use RGB space.
3 channels per pixel, one for red, green, and blue

| Code                | Input Color Space                       | Output Color Space                                                       |
| ------------------- | --------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_RGB2BGR`  | **RGB** – 3 Channels (Red, Green, Blue) | **BGR** – 3 Channels (Blue, Green, Red)                                  |
| `cv.COLOR_RGB2BGRA` | **RGB** – 3 Channels (Red, Green, Blue) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha)                          |
| `cv.COLOR_RGB2GRAY` | **RGB** – 3 Channels (Red, Green, Blue) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_RGB2HSV`  | **RGB** – 3 Channels (Red, Green, Blue) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |
| `cv.COLOR_RGB2RGBA` | **RGB** – 3 Channels (Red, Green, Blue) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha)                          |

## GRAY (Grayscale)
1 channel per pixel for brightness

| Code                | Input Color Space                                                        | Output Color Space                              |
| ------------------- | ------------------------------------------------------------------------ | ----------------------------------------------- |
| `cv.COLOR_HSV2BGR`  | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **BGR** – 3 Channels (Blue, Green, Red)         |
| `cv.COLOR_HSV2BGRA` | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) |
| `cv.COLOR_HSV2RGB`  | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **RGB** – 3 Channels (Red, Green, Blue)         |
| `cv.COLOR_HSV2RGBA` | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) |

## HSV (Hue, Saturation, Value)
Useful for when you want to control the color with a single channel
3 channels, one for hue (color), saturation (how vibrant or gray the color is), and value (brightness)

| Code                 | Input Color Space                 | Output Color Space                              |
| -------------------- | --------------------------------- | ----------------------------------------------- |
| `cv.COLOR_GRAY2BGR`  | **Gray** – 1 Channel (Brightness) | **BGR** – 3 Channels (Blue, Green, Red)         |
| `cv.COLOR_GRAY2BGRA` | **Gray** – 1 Channel (Brightness) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) |
| `cv.COLOR_GRAY2RGB`  | **Gray** – 1 Channel (Brightness) | **RGB** – 3 Channels (Red, Green, Blue)         |
| `cv.COLOR_GRAY2RGBA` | **Gray** – 1 Channel (Brightness) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) |

## BRGA (Blue, Green, Red, Alpha)
Same as BGR but with transparency
4 channels, one for blue, green, red, and alpha

| Code                 | Input Color Space                               | Output Color Space                                                       |
| -------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_BGRA2BGR`  | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **BGR** – 3 Channels (Blue, Green, Red)                                  |
| `cv.COLOR_BGRA2GRAY` | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_BGRA2HSV`  | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |
| `cv.COLOR_BGRA2RGB`  | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **RGB** – 3 Channels (Red, Green, Blue)                                  |
| `cv.COLOR_BGRA2RGBA` | **BGRA** – 4 Channels (Blue, Green, Red, Alpha) | **RGBA** – 4 Channels (Red, Green, Blue, Alpha)                          |

## RGBA (RED, Green, Blue, Alpha)
Same as RGB but with transparency
4 channels, one for red, green, blue, and alpha

| Code                 | Input Color Space                               | Output Color Space                                                       |
| -------------------- | ----------------------------------------------- | ------------------------------------------------------------------------ |
| `cv.COLOR_RGBA2RGB`  | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **RGB** – 3 Channels (Red, Green, Blue)                                  |
| `cv.COLOR_RGBA2BGR`  | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **BGR** – 3 Channels (Blue, Green, Red)                                  |
| `cv.COLOR_RGBA2BGRA` | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **BGRA** – 4 Channels (Blue, Green, Red, Alpha)                          |
| `cv.COLOR_RGBA2GRAY` | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **Gray** – 1 Channel (Brightness)                                        |
| `cv.COLOR_RGBA2HSV`  | **RGBA** – 4 Channels (Red, Green, Blue, Alpha) | **HSV** – 3 Channels (Hue/Color, Saturation/Intensity, Value/Brightness) |

# Geometric Transformations
## Scale
```python
# Manual pixel size
width = 100 # 100 pixels
height = 100 # 100 pixels
small_blue = cv.resize(blue, (width, height))
```
```python
# Scaling factor
width_factor = 2
height_factor = 2
big_green = cv.resize(green, None, fx=width_factor, fy=height_factor)
```

## Translate
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


