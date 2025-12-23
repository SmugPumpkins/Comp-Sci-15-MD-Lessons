# Overview

In this lesson, you will learn how to control whether the turtle draws lines as it moves. This is done by changing the turtle’s **pen state**. Understanding pen up and pen down is essential for controlling when lines appear on the screen.

# Important Information

The turtle has a pen attached to it, similar to a real pen touching paper.

There are two pen states:

* **Pen down** → the turtle draws lines as it moves
* **Pen up** → the turtle moves without drawing

By default, the turtle starts with the pen **down**.

## Pen Down

To ensure the turtle is drawing, use:

```python
t.pendown()
```

When the pen is down:

* Any movement creates a visible line
* This includes `forward`, `backward`, `goto`, and rotations combined with movement

## Pen Up

To move the turtle without drawing, use:

```python
t.penup()
```

When the pen is up:

* The turtle moves normally
* No lines are drawn
* This is useful for repositioning the turtle before drawing something new

## Shorthand Commands

There are also shorter versions of these commands:

* `pu()` → pen up
* `pd()` → pen down

These work exactly the same as the full versions.

# Set Up

Create a new Python file called `turtle_pen.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

t = turtle.Turtle()

t.forward(100)

t.penup()
t.forward(100)

t.pendown()
t.forward(100)

turtle.done()
```

Observe:

* The first movement draws a line
* The second movement does not
* The third movement draws again

## Change

Modify the program so that:

* The turtle lifts the pen before moving backward
* The turtle puts the pen down before moving forward again

Run the program and observe where lines do and do not appear.

## Challenge

Create a program where the turtle:

* Moves to at least three different locations
* Draws lines in some places
* Moves without drawing in others

