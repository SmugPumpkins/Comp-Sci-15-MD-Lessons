# Overview

In this lesson, you will learn how to draw **ovals directly on the Tk canvas** using the turtle library. Ovals are created by defining a rectangular boundary, and the oval is drawn to fit perfectly inside that space. You will also learn how to control common oval settings such as **outline color**, **fill color**, **border thickness**, and **dash style**.

# Important Information

When drawing ovals on the canvas, you are working directly with pixel coordinates instead of turtle movement commands.

## Creating an Oval

Ovals are drawn using:

```python
canvas.create_oval(x1, y1, x2, y2)
```

* `(x1, y1)` is one corner of an invisible bounding rectangle
* `(x2, y2)` is the opposite corner
* The oval fills the space inside that rectangle

Canvas coordinates work like this:

* `(0, 0)` is the **center** of the canvas
* X values increase to the right
* Y values increase downward

If the bounding box is a square, the oval will be a **circle**.
If the bounding box is a rectangle, the oval will be **stretched**.

## Outline Color

The border color of the oval is controlled using the `outline` setting:

```python
canvas.create_oval(x1, y1, x2, y2, outline="black")
```

Common outline colors include:

* `"black"`
* `"red"`
* `"blue"`
* `"green"`
* `"purple"`

## Fill Color

You can fill the inside of the oval using the `fill` setting:

```python
canvas.create_oval(x1, y1, x2, y2, fill="yellow")
```

Notes:

* The fill affects only the inside of the oval
* The outline remains a separate color

## Border Thickness

You can control how thick the oval’s outline is using `width`:

```python
canvas.create_oval(x1, y1, x2, y2, width=5)
```

* Larger numbers make thicker outlines
* Smaller numbers make thinner outlines

## Dashed Outlines

You can create dashed oval outlines using the `dash` setting:

```python
canvas.create_oval(x1, y1, x2, y2, dash=(10, 5))
```

* First number: dash length
* Second number: space between dashes

Dashed settings affect only the outline, not the fill.

## Combining Settings

All common oval settings can be combined:

```python
canvas.create_oval(
    x1, y1, x2, y2,
    outline="blue",
    fill="lightblue",
    width=4,
    dash=(8, 4)
)
```

# Set Up

Create a new Python file called `canvas_ovals.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

canvas.create_oval(50, 50, 200, 150)

turtle.done()
```

You should see a simple oval drawn on the canvas.

## Change

Modify the oval so that:

* The outline color is different
* The oval has a fill color
* The outline is thicker
* The outline is dashed

Run the program again and observe how each setting changes the oval.

## Challenge

Add additional ovals so that:

* One oval is a perfect circle
* One oval is stretched wide
* One oval has no fill
* One oval has a thick dashed outline

