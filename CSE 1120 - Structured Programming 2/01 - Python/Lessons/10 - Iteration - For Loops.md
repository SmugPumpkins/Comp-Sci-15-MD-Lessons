# Overview

This lesson introduces the basics of **`for` loops** in Python using the `for i in range()` pattern. You will learn how a `for` loop repeats code, what the loop variable means, how counting works in `range`, and why this kind of loop is one of the most useful tools in programming.

# Important Information

## What a For Loop Does

A **for loop** is used to repeat a block of code a specific number of times. Instead of writing the same code over and over, a loop allows you to write it once and let the computer handle the repetition.

```python
for i in range(5):
    print("Hello")
```

This code prints `"Hello"` five times.

## Understanding `for i in range()`

The syntax `for i in range()` is made of three important parts.

* `for` starts the loop
* `i` is the loop variable
* `range()` controls how many times the loop runs

```python
for i in range(3):
    print(i)
```

This loop runs three times and prints the value of `i` each time.

## The Loop Variable (`i`)

The variable `i` is just a **name**. It is commonly used by programmers, but it is not special. You can use **any valid variable name**.

```python
for count in range(4):
    print(count)
```

This loop works exactly the same way. The name `count` may even make the code clearer.

The loop variable stores a **number** that changes each time the loop runs. You can use it like any other number inside the loop.

```python
for i in range(5):
    print(i * 2)
```

## How `range()` Counts

The `range()` function always follows two important rules.

1. It **starts counting at 0**
2. It **stops one number before** the value given

```python
for i in range(5):
    print(i)
```

This prints:

```
0
1
2
3
4
```

Even though `5` is used, it is **not included**. The loop stops at `4`.

This behavior is very important to remember and will appear throughout programming.

## Using the Loop Variable Inside the Loop

Because the loop variable is a number, it can be used in calculations, messages, and logic.

```python
for i in range(3):
    print("Loop number", i)
```

Each time the loop runs, `i` updates automatically.

## Common Situations Where This Loop Is Useful

A `for i in range()` loop is useful whenever you know **how many times** something should happen.

One common use is repeating an action a fixed number of times.

```python
for i in range(10):
    print("Jumping jacks")
```

Another common use is counting or numbering items.

```python
for i in range(5):
    print("Item number", i)
```

A third common use is performing math that changes step by step.

```python
total = 0

for i in range(5):
    total = total + i

print(total)
```

This adds the numbers `0` through `4` together.

These patterns appear everywhere in programming, from games and animations to data processing and simulations.

# Set Up

Create a new Python file called `for_loops.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
for i in range(6):
    print("i is:", i)
```

Pay close attention to where the counting starts and where it stops.

## Change

Change the loop so that:

* It runs 10 times
* It uses a variable name other than `i`
* It prints the variable multiplied by `3`

## Challenge

Write a program that:

1. Uses a `for` loop with `range()`
2. Prints a message that includes the loop variable
3. Clearly shows that counting starts at `0` and ends one number before the value in `range()`

Your goal is to prove, using output, that you understand how `range()` and the loop variable work together.
