# Overview

This lesson builds on your understanding of `for` loops by introducing **multiple parameters in `range()`**. You will learn what each parameter represents, how programmers describe loops using terms like **initialization**, **condition**, and **increment**, and how changing these values allows a loop to count **forwards or backwards**.

# Important Information

## Thinking About a For Loop Like a Process

Every `for` loop follows the same basic structure, even if it looks simple on the surface. Programmers often describe loops using three core ideas:

* **Initialization** – where the loop starts counting
* **Condition** – when the loop should stop
* **Increment** – how the loop changes each time it runs

In Python, all of these are controlled by the values you pass into `range()`.

## Using One Parameter in `range()`

When `range()` is given **one value**, Python fills in the rest automatically.

```python
for i in range(5):
    print(i)
```

This loop behaves as if it were defined like this:

* **Initialization:** `0`
* **Condition:** stop before `5`
* **Increment:** `1`

So the loop counts:

```
0, 1, 2, 3, 4
```

This is the most common form of `range()` and is used when you simply want to repeat something a certain number of times.

## Using Two Parameters in `range(start, stop)`

When `range()` is given **two values**, the first value becomes the initialization, and the second value becomes the condition.

```python
for i in range(2, 6):
    print(i)
```

This loop works as follows:

* **Initialization:** `2`
* **Condition:** stop before `6`
* **Increment:** `1` (default)

The output is:

```
2, 3, 4, 5
```

The loop always starts at the first number and stops **one less than** the second number.

## Using Three Parameters in `range(start, stop, step)`

When `range()` is given **three values**, you control everything.

```python
for i in range(0, 10, 2):
    print(i)
```

This loop works as follows:

* **Initialization:** `0`
* **Condition:** stop before `10`
* **Increment (step):** `2`

The output is:

```
0, 2, 4, 6, 8
```

The increment determines how much the loop variable changes each time the loop runs.

## Counting Backwards with a Negative Increment

The increment does not have to be positive. If the increment is **negative**, the loop counts backwards.

```python
for i in range(5, 0, -1):
    print(i)
```

This loop works as follows:

* **Initialization:** `5`
* **Condition:** stop before `0`
* **Increment:** `-1`

The output is:

```
5, 4, 3, 2, 1
```

When counting backwards, the initialization must be **greater than** the condition, or the loop will never run.

## Why Understanding These Parameters Matters

By controlling initialization, condition, and increment, you can:

* Count forwards or backwards
* Skip values
* Start and stop at specific numbers
* Avoid unnecessary calculations

This gives you precise control over how many times your code runs and what values are used during each repetition.

# Set Up

Create a new Python file called `range_parameters.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
for i in range(1, 10, 3):
    print(i)
```

Identify the initialization, condition, and increment based on the output.

## Change

Modify the loop so that it:

* Starts at `10`
* Ends at `0`
* Counts backwards by `2`

## Challenge

Write **three separate `for` loops**:

1. One that uses **one parameter** in `range()`
2. One that uses **two parameters**
3. One that uses **three parameters** and counts backwards

For each loop, add a comment explaining the initialization, condition, and increment.
