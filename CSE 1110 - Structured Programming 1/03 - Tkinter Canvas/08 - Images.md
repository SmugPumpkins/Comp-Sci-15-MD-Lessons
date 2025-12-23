# Overview

In this lesson, you will learn how to add **images to the Tkinter canvas** when using the turtle library. This will be your first time working with image files in Python. You will learn how Python finds image files, how to load them, and how to display them on the canvas.

# Important Information

When working with images in turtle graphics, you are actually using **Tkinter images** behind the scenes. Images are drawn on the **canvas**, not by the turtle itself.

## Image Files and Python

Python does **not** automatically know where your images are. You must:

* Place the image file where Python can find it
* Use the correct **file path**
* Load the image before drawing it

### Recommended Folder Structure

For beginners, the easiest setup is:

```
project_folder/
├── canvas_images.py
└── image.png
```

This means:

* Your Python file and image file are in the **same folder**
* You can refer to the image by its filename only

## Supported Image Types

Tkinter supports:

* `.png` (recommended)
* `.gif`

Other formats like `.jpg` are **not supported** by default.

## Loading an Image

Images are loaded using `PhotoImage`:

```python
image = turtle.PhotoImage(file="image.png")
```

Important rules:

* The filename must match exactly
* The file must exist in the correct location
* The image must be stored in a variable

If the image is not stored in a variable, it may not display.

## Adding an Image to the Canvas

Once the image is loaded, you draw it using:

```python
canvas.create_image(x, y, image=image)
```

* `(x, y)` is the position of the image
* By default, the image is centered on that point
* `(0, 0)` is the **center of the canvas**

## Why the Image Must Be Stored in a Variable

If you do this:

```python
canvas.create_image(0, 0, image=turtle.PhotoImage(file="image.png"))
```

The image may **not appear**.

This happens because:

* Python deletes the image object when it is not stored
* The canvas loses access to the image

Always store the image in a variable.

# Set Up

1. Create a new Python file called `canvas_images.py`.
2. Place a `.png` or `.gif` image in the **same folder**.
3. Make sure you know the exact filename.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

image = turtle.PhotoImage(file="image.png")

canvas.create_image(0, 0, image=image)

turtle.done()
```

If everything is set up correctly, you should see the image appear in the center of the canvas.

## Change

Modify the program so that:

* The image appears in a different position on the canvas
* The image is **not** centered at `(0, 0)`

Run the program again and observe where the image appears.

## Challenge

Add a second image to the canvas by:

* Loading a second image file
* Storing it in a different variable
* Placing it at a different location on the canvas

Make sure **both image variables remain in the program**, or the images may disappear.
