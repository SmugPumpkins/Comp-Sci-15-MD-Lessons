# Overview

In this lesson, you will learn how to make a turtle appear on the screen and how to keep the turtle window open using `turtle.done()`. This is an important step so your turtle drawings do not immediately disappear when the program finishes running.

# Important Information

When using the `turtle` library, Python opens a new window called the **canvas**. This is where the turtle draws.

By default:

* Python runs your code from top to bottom.
* When the program reaches the end, it immediately closes.
* This causes the turtle window to appear briefly and then disappear.

To prevent this, we use:

* `turtle.done()` — this tells Python to keep the turtle window open until the user closes it.

To create a turtle on the canvas, we:

* Import the `turtle` library.
* Create a turtle object using `turtle.Turtle()`.

# Set Up

Create a new Python file called `first_turtle.py`.

# Copy, Change, Challenge

## Copy

Copy the following code exactly and run it.

```python
import turtle

my_turtle = turtle.Turtle()

turtle.done()
```

When you run the program:

* A window should open.
* You should see a turtle (usually an arrow) in the center of the screen.
* The window should stay open until you close it.

## Change

Change the variable name `my_turtle` to something else that makes sense to you.

Run the program again to confirm that it still works.

## Challenge

Add multiple turtles with different variable names. Are there any errors?
