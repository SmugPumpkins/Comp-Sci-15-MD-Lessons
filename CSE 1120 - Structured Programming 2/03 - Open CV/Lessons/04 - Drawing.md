# Overview

OpenCV includes a set of drawing functions that allow you to draw shapes and text directly onto images or video frames. These tools are commonly used for visual debugging, overlays, annotations, and highlighting detected features. All drawing functions modify the image **in place**, meaning the original image array is changed.

All coordinates are pixel-based and use the format `(x, y)`, where `(0, 0)` is the top-left corner of the image.

# Important Information

## Draw Line

**Function parameters:**

* `target_img` – The image or video frame to draw on.
* `start_pos` – The starting point of the line `(x, y)`.
* `end_pos` – The ending point of the line `(x, y)`.
* `bgr_color` – The line color in **BGR** format.
* `thickness` – The width of the line in pixels.

```python
target_img = np.zeros((512,512,3), np.uint8) # This could also be the frame of a video feed
start_pos = (0,0)
end_pos = (511, 511)
bgr_color = (255, 0, 0) # Blue
thickness = 5

cv.line(
    target_img,
    start_pos,
    end_pos,
    bgr_color,
    thickness
)
```

## Draw Rectangle

**Function parameters:**

* `target_img` – The image or video frame to draw on.
* `top_left_corner` – The top-left corner of the rectangle `(x, y)`.
* `bottom_right_corner` – The bottom-right corner of the rectangle `(x, y)`.
* `bgr_color` – The rectangle color in **BGR** format.
* `thickness` – Border thickness in pixels. Use `-1` to fill the rectangle.

```python
target_img = np.zeros((512,512,3), np.uint8) # This could also be the frame of a video feed
top_left_corner = (50,50)
bottom_right_corner = (100, 100)
bgr_color = (0, 255, 0) # Green
thickness = 3 # If thickness is -1 then it fills the shape

cv.rectangle(
    target_img,
    top_left_corner,
    bottom_right_corner,
    bgr_color,
    thickness
)
```

## Draw Circle

**Function parameters:**

* `target_img` – The image or video frame to draw on.
* `center_pos` – The center of the circle `(x, y)`.
* `radius` – Radius of the circle in pixels.
* `bgr_color` – The circle color in **BGR** format.
* `thickness` – Border thickness in pixels. Use `-1` to fill the circle.

```python
target_img = np.zeros((512,512,3), np.uint8) # This could also be the frame of a video feed
center_pos = (400, 400)
radius = 75
bgr_color = (0, 0, 255) # Red
thickness = 8 # If thickness is -1 then it fills the shape

cv.circle(
    target_img,
    center_pos,
    radius,
    bgr_color,
    thickness
)
```

## Draw Ellipse

**Function parameters:**

* `target_img` – The image or video frame to draw on.
* `center_pos` – The center of the ellipse `(x, y)`.
* `width_height` – Half-width and half-height of the ellipse axes.
* `rotation_angle` – Rotation of the ellipse in degrees.
* `arc_start_angle` – Starting angle of the arc in degrees.
* `arc_end_angle` – Ending angle of the arc in degrees.
* `bgr_color` – The ellipse color in **BGR** format.
* `thickness` – Border thickness in pixels. Use `-1` to fill the ellipse.

```python
target_img = np.zeros((512,512,3), np.uint8) # This could also be the frame of a video feed
center_pos = (200, 300)
width_height = (75, 150)
rotation_angle = 45
arc_start_angle = 0
arc_end_angle = 320
bgr_color = (0, 255, 255) # Yellow
thickness = 8 # If thickness is -1 then it fills the shape

cv.ellipse(
    target_img,
    center_pos,
    width_height,
    rotation_angle,
    arc_start_angle,
    arc_end_angle,
    bgr_color,
    thickness
)
```

## Draw Polygon

**Function parameters:**

* `target_img` – The image or video frame to draw on.
* `points` – A list of point arrays defining the polygon vertices.
* `connect_first_and_last_point` – Whether the shape should be closed.
* `bgr_color` – The polygon color in **BGR** format.
* `thickness` – Line thickness in pixels. Use `-1` to fill the polygon.

```python
unformatted_points = [[10,5], [100, 50], [100, 200], [200, 100]]
points = [np.array(unformatted_points, dtype=np.int32).reshape((-1,1,2))]

target_img = np.zeros((512,512,3), np.uint8) # This could also be the frame of a video feed
connect_first_and_last_point = True
bgr_color = (255, 255, 0) # Cyan
thickness = 2 # If thickness is -1 then it fills the shape

cv.polylines(
    target_img,
    points,
    connect_first_and_last_point,
    bgr_color,
    thickness
)
```

## Draw Text

**Function parameters:**

* `target_img` – The image or video frame to draw on.
* `message` – The text string to display.
* `bottom_left_corner_pos` – Position of the text baseline `(x, y)`.
* `font` – Font type used to draw the text.
* `size` – Font scale factor.
* `bgr_color` – Text color in **BGR** format.
* `thickness` – Thickness of the text strokes.
* `line_type` – How the text edges are rendered.

```python
target_img = np.zeros((512,512,3), np.uint8) # This could also be the frame of a video feed
message = "Hello World!"
bottom_left_corner_pos = (10, 300)
font = cv.FONT_HERSHEY_SIMPLEX
size = 2
bgr_color = (255, 0, 255) # Magenta
thickness = 1 # If thickness is -1 then it fills the shape
line_type = cv.Line_AA

cv.circle(
    target_img,
    center_pos,
    radius,
    bgr_color,
    thickness
)
```

### Fonts

| Code                             | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| `cv.FONT_HERSHEY_SIMPLEX`        | Simple, clean sans-serif font.                 |
| `cv.FONT_HERSHEY_PLAIN`          | Small sans-serif font with minimal styling.    |
| `cv.FONT_HERSHEY_DUPLEX`         | Slightly thicker sans-serif font.              |
| `cv.FONT_HERSHEY_COMPLEX`        | Serif-style font with more detail.             |
| `cv.FONT_HERSHEY_TRIPLEX`        | More detailed serif font with thicker strokes. |
| `cv.FONT_HERSHEY_COMPLEX_SMALL`  | Smaller version of `FONT_HERSHEY_COMPLEX`.     |
| `cv.FONT_HERSHEY_SCRIPT_SIMPLEX` | Simple handwriting-style font.                 |
| `cv.FONT_HERSHEY_SCRIPT_COMPLEX` | More detailed handwriting-style font.          |
| `cv.FONT_ITALIC`                 | Modifier flag that applies italics.            |

### Line Types

| Code         | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| `cv.FILLED`  | Fills the shape completely with color.                      |
| `cv.LINE_4`  | Line drawn using 4-connected pixels (blocky edges).         |
| `cv.LINE_8`  | Line drawn using 8-connected pixels (smoother than LINE_4). |
| `cv.LINE_AA` | Anti-aliased line for smooth edges.                         |
