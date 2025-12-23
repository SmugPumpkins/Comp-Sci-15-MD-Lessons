# Overview

In this lesson, you will learn how to access the underlying **Tk canvas** that the turtle library uses. Instead of drawing only with turtle movement commands, you will store the canvas in a variable and use it directly. This sets the foundation for future lessons where you will draw lines, shapes, and graphics without moving the turtle.

# Important Information

The turtle library is built on top of **Tkinter**, Python’s standard GUI toolkit. When you use turtle, a **Tk canvas** is created behind the scenes. This canvas is the surface that everything is drawn on.

## Turtle Screen vs Canvas

There are two important layers to understand:

* **Screen** → the turtle window
* **Canvas** → the drawable area inside the window

The turtle moves and draws on the canvas, but you can also access that canvas directly.

## Accessing the Screen

First, you create a screen object:

```python
screen = turtle.Screen()
```

This represents the turtle window.

## Accessing the Canvas

Once you have the screen, you can get the canvas:

```python
canvas = screen.getcanvas()
```

Now:

* `canvas` is a Tk canvas object
* You can draw directly on it without using turtle movement commands
* This allows for more precise and flexible drawing later on

## Why Store the Canvas in a Variable

Storing the canvas in a variable allows you to:

* Reuse the canvas throughout your program
* Draw shapes that are not tied to the turtle’s position
* Mix turtle-based drawing with canvas-based drawing

Future lessons will build on this by using the canvas to draw lines, rectangles, circles, and more.

# Set Up

Create a new Python file called `turtle_canvas.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

turtle.done()
```

When you run this program:

* A turtle window opens
* No turtle movement happens
* The canvas is created and stored in the `canvas` variable

Nothing visible is drawn yet, and that is expected.

## Change

Modify the program so that:

* A turtle object is created and stored in a variable
* The turtle appears on the canvas
* The turtle moves forward and turns at least once

Do **not** draw anything directly on the canvas yet. Use only turtle movement commands.

Run the program and confirm that:

* The turtle is visible
* The canvas stays open
* The turtle movement happens on the screen

## Challenge

Extend the program so that:

* The turtle is moved to a new position on the canvas
* The turtle changes direction at least twice
* The turtle ends in a different location than where it started

The canvas variable should still exist in your program, even if you are not using it yet.
