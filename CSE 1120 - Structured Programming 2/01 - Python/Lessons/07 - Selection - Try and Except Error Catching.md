# Overview

This lesson introduces **`try` / `except`**, a tool used to **prevent programs from crashing** when something goes wrong. You will learn how `try` / `except` builds on the idea of `if` / `else`, why user input is one of the most common sources of errors, and how handling errors is an important skill for thinking like a computer scientist.

# Important Information

## Why Programs Crash

So far, most of your programs have worked as expected because **you controlled the data**. As soon as users start typing their own input, your program becomes vulnerable to errors.

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

Only one of these blocks will run.

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

Python runs the code inside the `try` block line by line.

* If no error occurs, the `except` block is skipped
* If an error occurs, Python immediately jumps to the `except` block
* The program continues running afterward

This allows your program to **recover gracefully** instead of stopping.

## Catching Specific Errors (Optional but Important)

Different mistakes cause different errors. You can catch specific ones.

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("You must enter a whole number")
```

This is safer than a generic `except` because it avoids hiding unexpected bugs.

There is a list of common errors and what they mean available on the [Debugging Common Errors](/Debugging%20Common%20Errors.md) page.

## Why Error Handling Matters in Computer Science

Handling errors is not just about avoiding crashes. It is about **anticipating failure**.

Good programmers assume:

* Users will make mistakes
* Data will be messy
* Programs will be used in ways they did not expect

Error handling shows:

* Careful planning
* Defensive thinking
* Professional responsibility

These skills are used everywhere in computer science, from game development to cybersecurity to medical software.

## Common Invalid Inputs to Think About

When asking for user input, ask yourself:

* What if the user types letters instead of numbers?
* What if they press Enter without typing anything?
* What if they type a negative number?
* What if they copy-paste something unexpected?
* What if they misunderstand the prompt?

You do not need to catch **every** possible mistake, but you should catch the **most likely ones**.

## Try / Except vs If / Else

`if` / `else` is best when:

* You can check the condition ahead of time
* You are comparing values

`try` / `except` is best when:

* You cannot know in advance if the code will fail
* You are converting input or accessing data

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



