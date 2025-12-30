# Overview

In this lesson, you will learn how to change basic turtle settings. You will control how the turtle **looks**, how **big** it is, how **fast** it moves, and what **color** it appears on the screen. These settings affect the turtle itself, not the lines it draws.

# Important Information

The turtle is an object, and many of its properties can be changed using built-in methods. Changing these settings helps make programs easier to understand and more visually interesting.

## Changing the Turtle’s Shape

The turtle can appear in different predefined shapes. You can change the shape using:

```python
t.shape("shape_name")
```

Python’s turtle library includes these built-in shapes:

* `"classic"` – the default arrow-style turtle
* `"arrow"` – a sharper arrow pointer
* `"turtle"` – a turtle icon with legs and a shell
* `"circle"` – a circle
* `"square"` – a square
* `"triangle"` – a triangle

The shape only affects how the turtle looks, not how it moves.

## Changing the Turtle’s Color

You can change the turtle’s color using:

```python
t.color("color_name")
```

Examples of common color names include:

* `"black"`
* `"red"`
* `"blue"`
* `"green"`
* `"purple"`
* `"orange"`

The color you set applies to the turtle itself and (later) to the lines it draws.

## Changing the Turtle’s Size

You can resize the turtle using:

```python
t.shapesize(stretch_wid, stretch_len)
```

* `stretch_wid` controls the height
* `stretch_len` controls the width

Example:

* `t.shapesize(2, 2)` makes the turtle twice as large
* `t.shapesize(1, 3)` makes it wider but not taller

The size values are **scale factors**, not pixels.

## Changing the Turtle’s Speed

You can control how fast the turtle moves using:

```python
t.speed(value)
```

Valid speed values are:

* `1` → slowest
* `10` → fastest animated speed
* `0` → **instant movement (no animation)**

Important notes:

* Lower numbers move more slowly.
* Higher numbers move faster.
* Speed `0` ignores animation and is the fastest possible option.

# Set Up

Create a new Python file called `turtle_settings.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

t = turtle.Turtle()

t.shape("turtle")
t.color("blue")
t.shapesize(2, 2)
t.speed(5)

turtle.done()
```

Observe how the turtle looks and how quickly it moves.

## Change

Modify the program so that:

* The turtle uses a different shape
* The turtle is a different color
* The turtle is either taller or wider than before
* The speed is noticeably faster or slower

Run the program again and observe the changes.

## Challenge

Create a turtle that:

* Uses the fastest possible speed
* Is much larger than the default size
* Uses a shape that is **not** `"classic"`

Be ready to explain which settings you changed and what each one does.
