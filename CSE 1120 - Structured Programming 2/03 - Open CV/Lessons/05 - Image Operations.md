# Overview

OpenCV treats images as **NumPy arrays**, which means every image is made up of rows, columns, and color channels containing numeric values. Understanding how to inspect and manipulate these arrays is essential for image processing tasks such as editing pixels, copying regions, blending images, and analyzing image data.

This lesson focuses on **core image operations** in OpenCV: examining image properties, accessing and modifying pixels, working with color channels, and combining images.

# Important Information

For the following code examples, assume we have the following libraries and images initialized.

```python
# Libraries
import numpy as np
import cv2 as cv

# Load images
img = cv.imread('blue.png')
img_1 = cv.imread('red.png')
img_2 = cv.imread('green.png')
```

Each image loaded with `cv.imread()` is stored as a NumPy array with a specific shape, size, and data type.

## Image Properties

OpenCV images have several useful properties that describe their structure.

```python
img.shape
```

`shape` returns a tuple describing the image dimensions. For a color image, this is `(height, width, channels)`. The number of channels is usually `3` for BGR images.

```python
img.size
```

`size` returns the total number of values stored in the array. This equals `height × width × channels`.

```python
img.dtype
```

`dtype` shows the data type used for each divergência. Most OpenCV images use `uint8`, meaning each channel value ranges from `0` to `255`.

These properties are often used to verify image dimensions or ensure compatibility when combining images.

## Accessing and Modifying Pixel Values

Individual pixels can be accessed using array indexing.

```python
pixel = img[100,100]
```

This returns the pixel at row `100` and column `100`. Because OpenCV uses **BGR color order**, the result is a three-value array: `[blue, green, red]`.

You can also access individual color channels directly.

```python
pixel_blue_channel = img[100,100,0]
pixel_green_channel = img[100,100,1]
pixel_red_channel = img[100,100,2]
```

Each channel value ranges from `0` to `255`.

Pixel values can be modified by assigning new values.

```python
img[100,100] = [255, 0, 0]
```

This sets the pixel to pure blue (maximum blue channel, no green or red). Pixel manipulation like this is useful for marking points, debugging, or drawing simple indicators.

## Modifying Regions of Pixels

Instead of working with a single pixel, OpenCV allows entire **regions of interest (ROIs)** to be copied and modified.

![Blue With 3 Eyes](/Images/blue_3_eye.png)

This example gives blue a third eye on their forehead.

```python
eye_region = img[85:121, 67:104]
img[43:79, 109:146] = eye_region
cv.imshow('blue', img)
```

The first line extracts a rectangular region from the image using slicing. The second line pastes that region into a new location. This works because both regions are the same size.

Region-based operations are very fast because they use NumPy slicing instead of looping over pixels.

## Splitting and Merging Channels

Color images contain separate color channels that can be manipulated independently.

```python
b,g,r = cv.split(img)
```

`cv.split()` separates the image into its blue, green, and red channels. Each channel is a grayscale image representing the intensity of that color.

```python
img = cv.merge((b,g,r))
```

`cv.merge()` combines separate channels back into a single color image. Channels must be merged in BGR order.

### With NumPy Indexing (Advanced)

Channels can also be accessed directly using NumPy slicing.

```python
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
```

The colon `:` means “all rows” and “all columns,” while the last index selects the channel.

This approach is faster and more commonly used in advanced image processing.

This would turn the green channel on all the pixels to 255, making the image greener.

```python
g = 255
```

Direct channel manipulation is often used for color filtering, masking, and visual effects.

## Adding Images

OpenCV provides functions to combine images mathematically. These operations require images to be the same size and data type.

### `cv.add`

```python
added_img = cv.add(img_1, img_2)
```

`cv.add()` performs **saturated addition**, meaning values above `255` are clipped instead of wrapping around. This prevents unexpected color artifacts and is preferred over normal NumPy addition for images.

### `cv.addWeighted()`

```python
img_1_weight = 0.4
img_2_weight = 1 - img_1_weight # Weights should add to 1, so instead of calculating it by hand we can just subtract the first weight from 1
scalar = 0 # Just use 0 for this to keep the colors as is

weighted_added_img = cv.addWeighted(img_1, img_1_weight, img_2, img_2_weight, scalar)
```

`cv.addWeighted()` blends two images together using weights. Each image contributes a percentage of its color to the final result. The scalar value is an optional brightness offset and is usually set to `0`.

This function is commonly used for overlays, fades, and blending effects.

## Example

```python
# Import library
import cv2 as cv

# Load images
green = cv.imread('green.png')
red = cv.imread('red.png')

# Set weights
red_weight = 0.4
green_weight = 1 - red_weight
scalar = 0 

# Add images together
weighted = cv.addWeighted(red, red_weight, green, green_weight, scalar)

# Display image to user
cv.imshow('Weighted', weighted)

# Close all windows when a key is pressed
cv.waitKey(0)
cv.destroyAllWindows()
```

![Add Weighted Example](/Images/weighted.png)

This example blends a red image and a green image together using weighted addition. The result is a combined image where each original image contributes proportionally to the final color. This technique is widely used for transparency effects, visual comparisons, and overlays in computer vision projects.
