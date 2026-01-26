# Overview

This lesson builds on your ability to prevent errors by introducing **null checks**. You will learn what a null value is in Python, why using a null value incorrectly can cause errors, and how checking for null values can prevent crashes before they happen.

# Important Information

## What a Null Value Is in Python

In Python, a **null value** is represented by the keyword `None`. A variable set to `None` means it does not currently refer to any usable data.

```python
name = None
```

This is not the same as an empty string (`""`) or the number `0`. `None` means “no value at all.”

## Why Null Values Cause Errors

Many operations in Python assume that a value exists and has certain properties. When a variable is `None`, those assumptions break.

For example, strings have a length, but `None` does not.

```python
name = None
print(len(name))
```

This causes a runtime error because Python cannot determine the length of something that does not exist.

Similarly, you cannot call methods on `None`.

```python
text = None
print(text.lower())
```

This crashes because `None` does not have string methods like `.lower()`.

These errors are common when working with user input, optional data, or values that may or may not be set yet.

## Checking for Null Before Using a Value

To prevent these errors, programmers perform a **null check** before using a variable.

```python
name = None

if name != None:
    print(len(name))
```

In this example, `len(name)` is only evaluated if `name` actually contains a value. If `name` is `None`, the code inside the `if` statement is skipped safely.

This approach prevents errors **before they happen**, rather than reacting to them afterward.

## Null Checks vs Try / Except

Null checks and `try` / `except` both prevent crashes, but they serve different purposes.

A null check is used when you **expect** that a value might be missing and want to handle that case intentionally.

```python
if user_input != None:
    print(user_input)
```

A `try` / `except` block is used when an operation might fail in ways you cannot fully predict.

```python
try:
    number = int(user_input)
except:
    print("Invalid number")
```

Good programs often use **both**. Null checks prevent obvious errors, while `try` / `except` protects against unexpected ones.

## Common Situations Where Null Checks Are Needed

Null checks are especially important when:

* A variable is meant to be optional
* User input might be empty or cancelled
* Data comes from an external source
* A value is assigned later in the program

In all of these cases, assuming a value exists can cause your program to crash.

## Why Null Checking Is an Important Programming Skill

Checking for null values is part of **defensive programming**. Instead of assuming everything will go perfectly, you plan for missing or invalid data.

This mindset is essential in real software development, where programs must handle messy input, incomplete data, and unpredictable user behavior without failing.

# Set Up

Create a new Python file called `null_checks.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
message = None

if message != None:
    print(message.upper())
else:
    print("No message provided")
```

Confirm that the program runs without crashing.

## Change

Change `message` to a string value and verify that the output changes.

## Challenge

Write a program that:

* Uses a variable that might be `None`
* Performs a null check before using the value
* Would crash if the null check were removed

Your goal is to show that you understand how null checks prevent errors **before** they occur.
