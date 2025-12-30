# Overview

In this lesson, you will learn how to draw **rectangles directly on the Tk canvas** using the turtle library. Instead of moving a turtle, you will create rectangles by defining corner points and adjusting common rectangle settings such as **outline color**, **fill color**, **line thickness**, and **dash style**.

# Important Information

When drawing rectangles on the canvas, you are working directly with pixel coordinates rather than turtle movement commands.

## Creating a Rectangle

Rectangles are drawn using:

```python
canvas.create_rectangle(x1, y1, x2, y2)
```

* `(x1, y1)` is one corner of the rectangle
* `(x2, y2)` is the opposite corner
* These points define the rectangle’s width and height

Canvas coordinates work as follows:

* `(0, 0)` is the **center** of the canvas
* X values increase to the right
* Y values increase downward

## Outline Color

The rectangle’s border color is controlled using the `outline` setting:

```python
canvas.create_rectangle(x1, y1, x2, y2, outline="black")
```

Common outline colors include:

* `"black"`
* `"red"`
* `"blue"`
* `"green"`
* `"purple"`

If `outline` is not specified, it defaults to black.

## Fill Color

You can fill the inside of the rectangle using the `fill` setting:

```python
canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")
```

Important notes:

* The fill color affects only the interior
* The outline color remains separate

## Border Thickness

You can control how thick the rectangle’s border is using `width`:

```python
canvas.create_rectangle(x1, y1, x2, y2, width=5)
```

* Larger numbers create thicker borders
* Smaller numbers create thinner borders

## Dashed Borders

You can create dashed rectangle borders using `dash`:

```python
canvas.create_rectangle(x1, y1, x2, y2, dash=(10, 5))
```

* The first number is the dash length
* The second number is the space between dashes

Dashed settings affect only the outline, not the fill.

## Combining Settings

Rectangle settings can be combined in a single call:

```python
canvas.create_rectangle(
    x1, y1, x2, y2,
    outline="blue",
    fill="lightblue",
    width=4,
    dash=(8, 4)
)
```

# Set Up

Create a new Python file called `canvas_rectangles.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

canvas.create_rectangle(50, 50, 200, 150)

turtle.done()
```

You should see a simple rectangle drawn on the canvas.

## Change

Modify the rectangle so that:

* The outline color is different
* The rectangle has a fill color
* The border is thicker
* The border is dashed

Run the program again and observe how each setting changes the rectangle.

## Challenge

Add additional rectangles so that:

* Each rectangle uses a different combination of outline, fill, and width
* At least one rectangle has no fill
* At least one rectangle has a thick dashed border

