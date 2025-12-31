# Overview

This lesson introduces the **`match` / `case` statement** in Python. You will learn how to write a `match` statement, how Python checks cases from top to bottom, how to handle a default case, and how `match` compares to using a long chain of `elif` statements.

# Important Information

## What a Match Case Is

A `match` statement allows Python to compare a single value against multiple possible patterns. It is often described as being similar to a **switch statement** in other programming languages.

A `match` statement checks each `case` **from top to bottom**. As soon as a matching case is found, that block of code runs and the `match` statement ends.

```python
match value:
    case pattern_1:
        # code
    case pattern_2:
        # code
```

Only one case will ever run.

## Basic Match Case Syntax

Here is the simplest possible example.

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the week")
    case "Sunday":
        print("Weekend")
```

If `day` is `"Monday"`, only the first case runs. The rest are skipped.

## Ordering of Cases Matters

Just like `if` / `elif`, cases are checked **in order**. The first matching case wins.

```python
number = 5

match number:
    case 5:
        print("Exactly five")
    case _:
        print("Something else")
```

If Python finds a match, it does **not** check the remaining cases.


## The Default Case (`_`)

A `match` statement should almost always include a **default case**. The underscore `_` is used to represent “anything else.”

```python
command = "save"

match command:
    case "open":
        print("Opening file")
    case "close":
        print("Closing file")
    case _:
        print("Unknown command")
```

If none of the earlier cases match, the `_` case runs. This prevents your program from silently doing nothing.

## Match Case Example: Menu Selection

```python
choice = 3

match choice:
    case 1:
        print("Play game")
    case 2:
        print("Settings")
    case 3:
        print("Quit")
    case _:
        print("Invalid option")
```

This is a common and clean use of `match`, especially when checking fixed options.

## Match Case vs `elif`

### Advantages of `match`

A `match` statement is often **clearer and easier to read** when you are checking one value against many exact options.

```python
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Pass")
    case _:
        print("Fail")
```

This is cleaner than a long chain of `elif` statements that all compare the same variable.

### Disadvantages of `match`

A `match` statement is **not always the best tool**.

* It works best with **exact matches**, not ranges
* It is less flexible than complex boolean logic
* It requires **Python 3.10 or newer**

For example, numeric ranges are usually clearer with `if` / `elif`.

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
```

Using `match` for this would be awkward and unclear.

## When to Use Match vs Elif

|Use `match` when:|Use `if` / `elif` when:|
|-|-|
|You are comparing **one value**|You need **ranges**|
|You have many **fixed options**|You are combining **logical operators**|
|You want clean, readable structure|Conditions are not simple equality checks|

# Set Up

Create a new Python file called `match_case.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following program.

```python
command = "help"

match command:
    case "start":
        print("Starting program")
    case "help":
        print("Showing help menu")
    case "quit":
        print("Exiting program")
    case _:
        print("Unknown command")
```

Change the value of `command` and observe how the output changes.

## Change

Add **two more cases** to the program. One should trigger a new message, and one should fall through to the default case.

## Challenge

Create a program that:

1. Uses `match` to handle **at least five different options**
2. Includes a **default case**
3. Would be more difficult or messy to write using `elif`

Test each option to make sure the correct case runs and no unexpected code executes.
