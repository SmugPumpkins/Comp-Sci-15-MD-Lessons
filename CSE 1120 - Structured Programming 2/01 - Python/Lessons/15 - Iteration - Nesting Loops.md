# Overview

This lesson introduces **nested loops**, which are loops placed inside other loops. You will learn why programmers nest loops, common naming conventions for loop variables, how nesting dramatically increases the amount of work a program performs, and why mastering nested loops is a crucial programming skill.

# Important Information

## What Nesting a Loop Means

A loop is **nested** when one loop runs completely inside another loop. The outer loop controls how many times the inner loop starts, and the inner loop runs fully for each iteration of the outer loop.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

In this example, the inner loop runs **two times** for every single iteration of the outer loop.

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
        print("Row", row, "Seat", seat)
```

This pattern is extremely common when working with grids, tables, game boards, images, or any situation where one action must happen for **every possible pairing** of values.

## How Nested Loops Increase the Number of Steps

Nested loops can dramatically increase how much work a program performs. If one loop runs 5 times and another loop inside it also runs 5 times, the total number of operations is not 10—it is **25**.

```python
for i in range(5):
    for j in range(5):
        print(i, j)
```

The outer loop runs 5 times. Each time it runs, the inner loop also runs 5 times. This results in 5 × 5 total iterations.

As more loops are nested, the number of operations grows even faster. This is why nested loops must be used carefully, especially with large ranges.

## Understanding Execution Order

A key concept with nested loops is understanding **execution order**. The inner loop always completes fully before the outer loop moves to its next iteration.

```python
for i in range(2):
    print("Outer loop:", i)
    for j in range(3):
        print("  Inner loop:", j)
```

The inner loop runs from start to finish for `i = 0`, then runs again from start to finish for `i = 1`. This predictable pattern is essential to understand in order to get the expected output.

## Why Nested Loops Are a Crucial Skill

Knowing how to correctly nest loops allows programmers to solve complex problems using simple logic. Nested loops appear in nearly every area of computer science, including game development, data processing, simulations, image analysis, and artificial intelligence.

Being able to predict how nested loops execute helps prevent bugs, improves performance, and allows you to reason clearly about what your program is doing. Programmers who struggle with nested loops often struggle to scale their solutions to more complex problems.

Mastering nested loops is less about memorization and more about **thinking step by step**, understanding how repeated actions interact, and visualizing how data flows through your program.

# Set Up

Create a new Python file called `nested_loops.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)
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

Your goal is to show that you understand both **why** loops are nested and **how** they execute.
