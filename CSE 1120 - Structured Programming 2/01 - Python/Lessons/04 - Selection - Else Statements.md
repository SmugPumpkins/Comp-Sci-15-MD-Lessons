# Overview

This lesson introduces the **else statement**, which works together with an `if` statement. You will learn how `else` allows your program to choose **one of two paths** so that something happens whether a condition is `True` or `False`.

# Important Information

## Why Else Exists

An `if` statement only runs code when its condition is `True`. If the condition is `False`, the code is skipped and nothing happens unless you tell the program what to do instead.

The `else` statement solves this problem. It defines a block of code that runs **when the `if` condition is not true**.

An `if` + `else` structure guarantees that **exactly one** block of code will run.

## Basic If / Else Structure

An `else` statement must always come **after** an `if` statement and must be aligned with it.

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

The `else` statement does not have a condition. It automatically runs when the `if` condition fails.

## Simple Example with Numbers

```python
number = 5

if number == 5:
    print("The number is 5")
else:
    print("The number is not 5")
```

If `number` is equal to `5`, the first message prints. If it is anything else, the second message prints.

Only one of these messages can run.

## Simple Example with Strings

```python
password = "guest"

if password == "admin":
    print("Access granted")
else:
    print("Access denied")
```

If the password matches `"admin"`, access is granted. Otherwise, access is denied. The program always responds with one clear result.

## Else Depends on the If Statement

The `else` block is directly tied to the `if` statement above it. Indentation is critical.

```python
score = 80

if score >= 50:
    print("Pass")
else:
    print("Fail")

print("Done")
```

The `else` only applies to the `if`. The final print statement always runs, regardless of the condition.

# Set Up

Create a new Python file called `else_statements.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
age = 18

if age >= 18:
    print("You are allowed in")
else:
    print("You are not allowed in")
```

Change the value of `age` and run the program again. Notice how the output switches.

## Change

Change the condition so that the program checks whether `age` is **less than** `18` instead. Update the messages so they still make sense.

## Challenge

Write a program that:

1. Stores a word in a variable.
2. Uses an `if` statement to check if the word matches a specific value.
3. Uses an `else` statement to handle all other cases.

Your program should always print **exactly one message**, no matter what value the variable contains.
