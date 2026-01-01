# Overview

This lesson introduces **nested loops**, which are loops placed inside other loops. You will learn why programmers nest loops, common naming conventions for loop variables, how nesting dramatically increases the amount of work a program performs, and why mastering nested loops is a crucial programming skill.

# Important Information

## What Nesting a Loop Means

A loop is **nested** when one loop runs completely inside another loop. The outer loop controls how many times the inner loop starts, and the inner loop runs fully for each iteration of the outer loop.

In this example, the inner loop runs **two times** for every single iteration of the outer loop.
```python
for i in range(3):
    for j in range(2):
        print(f"outer loop: {i}, inner loop: {j}")
```
Output:
```
outer loop: 0, inner loop: 0
outer loop: 0, inner loop: 1
outer loop: 1, inner loop: 0
outer loop: 1, inner loop: 1
outer loop: 2, inner loop: 0
outer loop: 2, inner loop: 1
```


## Common Variable Naming in Nested Loops

By convention, programmers often use short variable names like `i`, `j`, `k`, and so on when working with nested loops.

```python
for i in range(2):
    for j in range(3):
        print(i, j)
```

This convention exists because the variables are temporary and represent positions or steps rather than meaningful data. Using short names helps keep the code readable without clutter. However, meaningful names can still be used when clarity is more important than tradition.

## Why a Loop Might Be Nested

Loops are nested when a problem naturally involves **working through combinations of values** or **processing data in layers**.

For example, imagine checking every seat in a movie theatre. One loop could represent rows, and the inner loop could represent seats within each row.

```python
for row in range(3):
    for seat in range(5):
        print(f"Row: {row}, Seat: {seat}")
```
Output
```
Row: 0, Seat: 0
Row: 0, Seat: 1
Row: 0, Seat: 2
Row: 0, Seat: 3
Row: 0, Seat: 4
Row: 1, Seat: 0
Row: 1, Seat: 1
Row: 1, Seat: 2
Row: 1, Seat: 3
Row: 1, Seat: 4
Row: 2, Seat: 0
Row: 2, Seat: 1
Row: 2, Seat: 2
Row: 2, Seat: 3
Row: 2, Seat: 4
```

This pattern is extremely common when working with grids, tables, game boards, images, or any situation where one action must happen for **every possible pairing** of values.

## How Nested Loops Increase the Number of Steps

Nested loops can dramatically increase how much work a program performs. If one loop runs 5 times and another loop inside it also runs 5 times, the total number of operations is not 10—it is **25**.

The outer loop runs 5 times. Each time it runs, the inner loop also runs 5 times. This results in 5 × 5 total iterations.
```python
for i in range(5):
    for j in range(5):
        print(i, j)
```

Output

```
Nice try, I'm not writing out 25 pairs of numbers. If you want to see 25 pairs of numbers just copy the code from above and run it.
```

As more loops are nested, the number of operations grows even faster. This is why nested loops must be used carefully, especially with large ranges.
```python
# This nested loop will run 125 times!
for i in range(5):
    for j in range(5):
        for k in range(5):
            print(i, j, k)

# This one runs 525 times!
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l on range(5):
                print(i, j, k, l)

# This one runs 625 times!
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                print(i, j, k, l)

# This one runs 3125 times!
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    print(i, j, k, l, m)
```

## Understanding Execution Order

A key concept with nested loops is understanding **execution order**. The inner loop always completes fully before the outer loop moves to its next iteration.

The inner loop runs from start to finish for `i = 0`, then runs again from start to finish for `i = 1`. This predictable pattern is essential to understand in order to get the expected output.

```python
for i in range(2):
    print(f"Outer loop: {i}")
    for j in range(3):
        print(f"Inner loop: {j}")
print("Program end.")
```
Output:
```
Outer loop: 0
Inner loop: 0
Inner loop: 1
Inner loop: 2
Outer loop: 1
Inner loop: 0
Inner loop: 1
Inner loop: 2
Program end.
```


## Why Nested Loops Are a Crucial Skill

Knowing how to correctly nest loops allows programmers to solve complex problems using simple logic. Nested loops appear in nearly every area of computer science, including game development, data processing, simulations, image analysis, and artificial intelligence.

Mastering nested loops is less about memorization and more about **thinking step by step**, understanding how repeated actions interact, and visualizing how data flows through your program.

# Set Up

Create a new Python file called `nested_loops.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

Observe how many total lines are printed and how the values of `i` and `j` change.

## Change

Modify the program so that:

* The outer loop runs 4 times
* The inner loop runs 3 times
* The output clearly shows which loop is outer and which is inner

## Challenge

Write a program that:

* Uses **nested loops**
* Prints a grid-like pattern (for example, rows and columns)
* Clearly demonstrates that the inner loop finishes completely before the outer loop continues
