# Overview

This lesson introduces **if statements**, which allow a program to make decisions. You will learn how an `if` statement checks whether something is **true**, how code can run or be skipped based on that check, and how equality comparisons work using `==`.

# Important Information

## What an If Statement Does

An **if statement** controls whether a block of code runs. It evaluates a **condition**, which must result in either `True` or `False`. If the condition is `True`, the indented code below the `if` statement runs. If the condition is `False`, that code is skipped.

```python
if 5 == 5:
    print("This runs")
```

Because `5 == 5` is `True`, the print statement runs.

```python
if 5 == 3:
    print("This does not run")
```

Because `5 == 3` is `False`, the print statement is skipped.

## The Importance of Indentation

In Python, indentation defines which code belongs to the `if` statement. Only the indented lines directly below the `if` statement are controlled by it.

```python
number = 10

if number == 10:
    print("Inside the if")

print("Outside the if")
```

The first message only prints if the condition is `True`. The second message always prints because it is not indented under the `if`.

## Assignment (`=`) vs Comparison (`==`)

The single equals sign `=` is used to **assign** a value to a variable. It stores data.

```python
score = 100
```

The double equals sign `==` is used to **compare** two values. It asks whether they are equal.

```python
score == 100
```

This comparison does not store anything. It evaluates to either `True` or `False`.

Using `=` instead of `==` in an `if` statement is a common beginner mistake that will lead to unexpected outcomes. Assignment sets a value. Comparison checks a value.

## Using Variables in If Conditions

Many `if` statements compare variables to specific values.

```python
age = 13

if age == 13:
    print("You are 13 years old")
```

If the value stored in `age` is `13`, the message prints. If it is any other number, the message does not print.

## When Code Does Not Run

If an `if` condition is `False`, Python simply skips that block of code. The program continues running without errors.

```python
password = "abc123"

if password == "admin":
    print("Access granted")

print("Program finished")
```

Only `"Program finished"` prints because the condition is not `True`.

# Set Up

Create a new Python file called `if_statements.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
number = 10

if number == 10:
    print("The number is 10")

print("Program finished")
```

Now change the value of `number` to something other than `10` and run it again. Notice which lines run and which do not.

## Change

Change the program so that the `if` statement checks whether the variable is equal to `5` instead of `10`. Adjust the value of the variable so the message prints.

## Challenge

Write a program that:

1. Stores a word in a variable.
2. Uses an `if` statement to check if the word is exactly `"python"`.
3. Prints a message only when the condition is `True`.

Run your program twice: once where the message prints, and once where it does not.
