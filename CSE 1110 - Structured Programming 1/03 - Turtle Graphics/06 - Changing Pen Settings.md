# Overview

In this lesson, you will learn how to control **pen settings** for the turtle. Pen settings determine how lines are drawn on the screen, including their **thickness**, their **color**, and how to **fill in shapes**. This lesson avoids loops and focuses only on direct turtle commands.

# Important Information

The turtle’s pen is responsible for drawing lines as the turtle moves. Changing pen settings affects the drawing, not how the turtle moves or looks.

## Changing the Pen Size

You can control how thick the turtle’s lines are using:

```python
t.pensize(size)
```

or

```python
t.width(size)
```

* `size` is a number
* Larger numbers make thicker lines
* Smaller numbers make thinner lines

Example:

* `t.pensize(1)` draws a thin line
* `t.pensize(6)` draws a thick line

## Changing the Pen Color

You can change the color of the lines using:

```python
t.pencolor("color_name")
```

Examples of color names include:

* `"black"`
* `"red"`
* `"blue"`
* `"green"`
* `"purple"`
* `"orange"`

This only affects the lines drawn by the turtle.

## Filling Shapes

The turtle can fill in closed shapes with color.

Filling always follows this process:

1. Set the fill color
2. Start the fill
3. Draw a **closed shape**
4. End the fill

### Setting the Fill Color

```python
t.fillcolor("color_name")
```

### Starting and Ending the Fill

```python
t.begin_fill()
# draw the shape here
t.end_fill()
```

Important rules:

* The shape must be closed for the fill to work
* Everything drawn between `begin_fill()` and `end_fill()` is filled
* The fill appears when `end_fill()` is called

# Set Up

Create a new Python file called `turtle_pen_settings.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

t = turtle.Turtle()

t.pensize(5)
t.pencolor("blue")
t.fillcolor("yellow")

t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

turtle.done()
```

Observe:

* The thickness of the lines
* The outline color
* The filled color inside the shape

## Change

Modify the program so that:

* The pen size is different
* The outline color changes
* The fill color changes

Run the program again and observe the differences.

## Challenge

Create a filled shape that:

* Uses a thick pen
* Uses different colors for the outline and the fill
* Is clearly a closed shape

Do not use loops. Use only direct movement and turn commands.
