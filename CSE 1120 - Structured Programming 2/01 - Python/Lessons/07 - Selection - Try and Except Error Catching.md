# Overview

This lesson introduces **`try` / `except`**, a tool used to **prevent programs from crashing** when something goes wrong. You will learn how `try` / `except` builds on the idea of `if` / `else`, why user input is one of the most common sources of errors, and how handling errors is an important skill for thinking like a computer scientist.

# Important Information

## Why Programs Crash

So far, most of your programs have worked as expected because **you controlled the data**. As soon as users start typing their own input, your program becomes vulnerable to errors. You have been giving your programs nice data to work with. __Users are not nice. Users break things.__

For example, this code assumes the user types a number:

```python
age = int(input("Enter your age: "))
print(age + 1)
```

If the user types `15`, the program works.

If the user types `fifteen`, the program crashes with a `ValueError` and stops running completely.

This is not because the program logic is wrong. It is because the program was **not prepared** for invalid input.

## Thinking Like an If / Else

You can think of `try` / `except` as a different kind of decision structure.

* `if` / `else` handles **expected conditions**
* `try` / `except` handles **unexpected errors**

Instead of asking “is this condition true?”, `try` / `except` asks “did something go wrong?”

## Basic Try / Except Structure

A `try` block contains code that **might fail**.
An `except` block contains code that runs **only if an error occurs**.

```python
try:
    # code that might cause an error
except:
    # code that runs if an error happens
```

## Simple Example with User Input

```python
try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)
except:
    print("That was not a valid number")
```

If the user enters a number, the program runs normally.

If the user enters invalid data, the program does **not crash**. Instead, the error is caught and handled.

## What Happens Internally

Python runs the code inside the `try` block line by line. If no error occurs, the `except` block is skipped. If an error __DOES__ occur, Python immediately jumps to the `except` block, but keeps all of the valid data it used from the `try` block. Then, the program continues running afterward.

This allows your program to handle an error and keep going instead of stopping.

## Catching Specific Errors (_Technically_ Optional, But Use Them Most of the Time)

Different mistakes cause different errors. You can catch specific ones.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("You must enter a whole number")
```

This is safer than a generic `except` because it avoids hiding unexpected bugs. Whenever possible, you should specify the type of error you are expecting to handle.

There is a list of common errors and what they mean available on the [Debugging Common Errors](/Debugging%20Common%20Errors.md) page.

## Why Error Handling Matters in Computer Science

Handling errors is not just about avoiding crashes. It is about **anticipating failure**.

Good programmers assume users will make mistakes or intentionally push programs to their limits. Data will be messy and needs to be monitored. Programs will be used in ways they did not expect. A lot.

Error handling shows careful planning, defensive thinking, and professional responsibility. These skills are used everywhere in computer science, from game development to cybersecurity to medical software.

## Common Invalid Inputs to Think About

When asking for user input, ask yourself:

* What if the user types letters instead of numbers?
* What if they press Enter without typing anything?
* What if they type a negative number or a decimal?
* What if they copy-paste something unexpected?
* What if they misunderstand the prompt?

At this level of computer science, the possible errors that could show up are __all preventable__. Your code should be able to handle __any kind of error that it encounters__ because we are working with limited amounts and types of data.

## Try / Except vs If / Else

|`if` / `else`|`try` / `except`|
|-|-|
|You can check the condition ahead of time.|You cannot know in advance if the code will fail.|
|You are comparing values.|You are converting input or accessing data.|

Both tools are essential, and they are often used together.

# Set Up

Create a new Python file called `try_except.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following program.

```python
try:
    number = int(input("Enter a number: "))
    print("Double your number is", number * 2)
except:
    print("Invalid input. Please enter a number.")
```

Test the program with valid and invalid inputs.

## Change

Modify the program so that:

* The calculation adds `10` instead of doubling
* The error message clearly explains what the user did wrong

## Challenge

Write a program that:

1. Asks the user for **two numbers**
2. Uses `try` / `except` to prevent crashes
3. Prints the result of adding the two numbers
4. Displays a helpful error message if either input is invalid

Your goal is to make a program that **never crashes**, no matter what the user types.



