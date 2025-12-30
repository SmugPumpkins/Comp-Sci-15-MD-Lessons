# Overview

In this lesson, you will learn how to add **text directly to the Tkinter canvas** when working with the turtle library. Drawing text on the canvas allows you to display labels, titles, instructions, and other information without using the turtle’s writing commands.

# Important Information

When you access the canvas through turtle, you can draw text using canvas methods instead of turtle movement.

## Canvas Coordinates Reminder

In turtle graphics:

* `(0, 0)` is the **center of the canvas**
* Positive **x** moves right
* Negative **x** moves left
* Positive **y** moves down
* Negative **y** moves up

Text is placed using these coordinates.

## Creating Text on the Canvas

Text is created using:

```python
canvas.create_text(x, y, text="Your text here")
```

* `(x, y)` is the position of the text
* The text is centered on that point by default

## Changing the Text Content

The `text` setting controls what is displayed:

```python
text="Hello, World!"
```

The text can be:

* A single word
* A sentence
* Multiple words with spaces

## Changing the Text Color

You can change the text color using the `fill` setting:

```python
fill="blue"
```

Common color names include:

* `"black"`
* `"red"`
* `"blue"`
* `"green"`
* `"purple"`

## Changing the Font

Fonts are controlled using the `font` setting:

```python
font=("Arial", 20, "bold")
```

The font setting has three parts:

1. Font family (e.g. `"Arial"`, `"Courier"`, `"Times"`)
2. Font size (number)
3. Font style (`"normal"`, `"bold"`, `"italic"`)

You can omit the style if you want normal text.

## Text Alignment (Anchor)

By default, text is centered on the `(x, y)` position. You can control how the text is anchored using `anchor`:

```python
anchor="center"
```

Common anchor options:

* `"center"` → text is centered on the point
* `"n"` → text appears below the point
* `"s"` → text appears above the point
* `"e"` → text appears left of the point
* `"w"` → text appears right of the point

Anchors are useful for lining up text precisely.

## Combining Text Settings

All text settings can be combined in one call:

```python
canvas.create_text(
    0, 0,
    text="Canvas Text",
    fill="blue",
    font=("Arial", 24, "bold"),
    anchor="center"
)
```

# Set Up

Create a new Python file called `canvas_text.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
import turtle

screen = turtle.Screen()
canvas = screen.getcanvas()

canvas.create_text(0, 0, text="Hello, Canvas!")

turtle.done()
```

You should see text displayed in the center of the canvas.

## Change

Modify the text so that:

* The text content is different
* The text color changes
* The font size is larger or smaller

Run the program again and observe the changes.

## Challenge

Add multiple pieces of text so that:

* One piece of text is centered
* One piece of text appears above the center
* One piece of text appears to the left or right of the center
* At least one piece of text uses a different font style

