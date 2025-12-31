# Overview

This lesson introduces **`while` loops**. You will learn how `while` loops are similar to `for` loops, how they are different, when a `while` loop is the better choice, and why infinite `while` loops are sometimes used intentionally. You will also learn why it is important to include a clear way to **exit** a loop that runs continuously.

# Important Information

## What a While Loop Does

A **while loop** repeatedly runs a block of code **as long as a condition remains `True`**. Unlike a `for` loop, a `while` loop does not automatically count or stop. It keeps checking its condition before every iteration and only stops when that condition becomes `False`.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

In this example, the loop runs while `count < 5` is `True`. Each time the loop runs, `count` increases by `1`. Eventually, the condition becomes `False`, and the loop stops.

## How While Loops Are Similar to For Loops

Both `while` loops and `for` loops are used to **repeat code**. They can both use conditions, work with variables, and contain `if` statements, `break`, and `continue`. In fact, many `for` loops can be rewritten as `while` loops.

A `for` loop like this:

```python
for i in range(5):
    print(i)
```

Can be rewritten using a `while` loop:

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

Both loops produce the same output. The main difference is how much control you have over the loop’s behavior.

## How While Loops Are Different from For Loops

A `for` loop is typically used when you know **ahead of time** how many times the loop should run. The counting, stopping, and incrementing are handled automatically by `range()`.

A `while` loop is used when you **do not know** how many times the loop will run. The loop depends entirely on a condition, and it is your responsibility to make sure that condition eventually becomes `False`.

This makes `while` loops more flexible, but also more dangerous if not written carefully.

## Basic While Loop Syntax

Every `while` loop has three essential parts, even if they are not written on the same line.

1. An initialization before the loop
2. A condition in the `while` statement
3. A change inside the loop that affects the condition

```python
number = 1

while number <= 3:
    print(number)
    number += 1
```

If you forget to change the variable that controls the condition, the loop may never end.

## Infinite While Loops

An **infinite loop** is a loop that never stops on its own. This happens when the condition is always `True`.

```python
while True:
    print("Running forever")
```

At first, this may look like a mistake, but infinite loops are sometimes used **intentionally**, especially in programs that are meant to keep running.

Examples include:

* Games
* Servers
* Live camera feeds
* Real-time computer vision programs

These programs are designed to keep running until the user or system tells them to stop.

## Breaking Out of an Infinite Loop

When a `while` loop is designed to run continuously, a **best practice** is to include a clear way to exit the loop. This is usually done with a `break` statement tied to a condition.

```python
while True:
    user_input = input("Type 'quit' to exit: ")

    if user_input == "quit":
        break

    print("You typed:", user_input)
```

In this example, the loop runs forever unless the user types `"quit"`. When that happens, `break` exits the loop and the program ends cleanly.

This pattern is extremely important and will come up again when working with tools like **OpenCV**, where programs often run continuously until a specific exit condition is met.

## Choosing Between For and While Loops

A `for` loop is usually the better choice when:

* You know how many times the loop should run
* You are iterating over a list, string, or range

A `while` loop is usually the better choice when:

* The loop depends on user input
* The loop should run until something specific happens
* The number of iterations is unknown ahead of time

Understanding when to use each type of loop is a key skill in writing clear and effective programs.

# Set Up

Create a new Python file called `while_loops.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
count = 0

while count < 5:
    print("Count is", count)
    count += 1
```

Observe how the condition is checked before each loop iteration.

## Change

Modify the program so that:

* The loop counts **downwards** instead of upwards
* The loop stops at `0`

## Challenge

Write a program that:

* Uses an **infinite `while` loop**
* Repeatedly asks the user for input
* Uses a condition and `break` to safely exit the loop

Your goal is to create a loop that can run continuously but still shut down cleanly when instructed.
