# Overview

In this lesson, you will learn how to draw **arcs directly on the Tk canvas** using the turtle library. Arcs are curved shapes that are drawn inside a bounding box and can be used to create curves, partial circles, and pie-like shapes.

# Important Information

Arcs are created on the canvas in a similar way to ovals, but instead of drawing the entire oval, you draw **only part of it**.

## Canvas Coordinates Reminder

When using the turtle canvas:

* `(0, 0)` is the **center of the canvas**
* Positive **x** moves right
* Negative **x** moves left
* Positive **y** moves down
* Negative **y** moves up

## Creating an Arc

Arcs are created using:

```python
canvas.create_arc(x1, y1, x2, y2)
```

* `(x1, y1)` and `(x2, y2)` define a **bounding rectangle**
* The arc is drawn along the edge of an invisible oval that fits inside that rectangle

By default, the arc will not be visible unless additional settings are applied.

## Start Angle

The `start` setting controls **where the arc begins**, measured in degrees.

```python
canvas.create_arc(x1, y1, x2, y2, start=0)
```

Angle rules:

* Angles are measured in **degrees**
* `0` degrees starts on the **right side** of the oval
* Angles increase **counterclockwise**

Examples:

* `start=0` → right
* `start=90` → up
* `start=180` → left
* `start=270` → down

## Extent (Arc Length)

The `extent` setting controls **how far the arc goes** from the start angle.

```python
canvas.create_arc(x1, y1, x2, y2, start=0, extent=90)
```

* `extent` is measured in degrees
* `90` draws a quarter circle
* `180` draws a half circle
* `360` draws a full circle

## Arc Style

The `style` setting controls **how the arc is drawn**.

### ARC

```python
style="arc"
```

* Draws only the curved outline
* No lines to the center
* No fill

### PIESLICE

```python
style="pieslice"
```

* Draws a curved edge plus two lines to the center
* Can be filled
* Looks like a slice of pie

### CHORD

```python
style="chord"
```

* Draws a curved edge and a straight line connecting the ends
* Can be filled
* Does not connect to the center

## Outline Color

You can change the arc’s outline color using:

```python
outline="blue"
```

## Fill Color

Fill works only with `pieslice` and `chord` styles:

```python
fill="yellow"
```

## Border Thickness

You can control how thick the arc outline is using:

```python
width=4
```

## Dashed Arcs

You can create dashed arc outlines using:

```python
dash=(8, 4)
```

This affects only the outline.

## Combining Arc Settings

All arc settings can be combined in a single call:

```python
canvas.create_arc(
    -100, -100, 100, 100,
    start=0,
    extent=120,
    style="pieslice",
    outline="blue",
    fill="lightblue",
    width=3
)
```

# Set Up

Create a new Python file called `canvas_arcs.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

canvas.create_arc(
    -100, -100, 100, 100,
    start=0,
    extent=180,
    style="arc",
    outline="black",
    width=3
)

turtle.done()
```

You should see a curved arc drawn on the canvas.

## Change

Modify the arc so that:

* The arc starts at a different angle
* The arc covers a different extent
* The outline color is changed
* The arc is dashed

Run the program again and observe the differences.

## Challenge

Add multiple arcs so that:

* One arc uses `pieslice` style with a fill color
* One arc uses `chord` style
* One arc forms a half circle
* One arc forms a quarter circle
