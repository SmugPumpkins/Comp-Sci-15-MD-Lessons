# Overview

This lesson introduces **`elif` statements** in Python. You will learn how `elif` allows a program to check **multiple conditions**, why Python checks conditions **from top to bottom**, and how the order of your conditions can completely change your program’s results.

# Important Information

## What `elif` Means

The keyword `elif` is short for **else if**. It is used when you want to check **more than one condition**, but still ensure that **only one block of code runs**.

An `elif` statement must always come **after an `if`** and **before an `else`** (if an `else` is included).

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 is False and condition_2 is True
else:
    # runs if all conditions above are False
```

Python checks these conditions **in order, from top to bottom**. As soon as it finds a condition that is `True`, it runs that block and **skips the rest**.

## Top-to-Bottom Execution Is Critical

Once a condition is matched, Python stops checking the remaining conditions. This means the **order of your conditions matters**.

```python
number = 5

if number > 0:
    print("Positive")
elif number > 3:
    print("Greater than 3")
```

Even though `number > 3` is also `True`, it never runs because `number > 0` is checked first and already matches.

## Using `elif` to Categorize Values

`elif` is commonly used to place values into categories, such as ranges of numbers.

```python
temperature = 25

if temperature > 30:
    print("Hot")
elif temperature > 20:
    print("Warm")
else:
    print("Cold")
```

Only one message prints because only one condition is allowed to succeed.

## Grade Calculator — Correct Order

In this example, a numeric score is converted into a letter grade. The conditions are written **from highest to lowest**, which ensures correct results.

```python
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
```

A score of `82` correctly results in a **B**. Each condition only applies if all previous conditions were `False`.

## Grade Calculator — Incorrect Order

Now look at the same logic written in the **wrong order**.

```python
score = 82

if score >= 60:
    grade = "D"
elif score >= 70:
    grade = "C"
elif score >= 80:
    grade = "B"
elif score >= 90:
    grade = "A"
else:
    grade = "F"

print("Grade:", grade)
```

This program assigns a **D**, which is incorrect. The problem occurs because `score >= 60` is `True`, so Python stops checking and never reaches the better grades.

This demonstrates why `elif` conditions must be ordered **carefully**, especially when working with ranges.

## Key Rule to Remember

When using `elif`:

* Conditions are checked **top to bottom**
* The **first matching condition wins**
* More specific or higher-value conditions should usually come **first**

# Set Up

Create a new Python file called `elif_statements.py`.

# Copy, Change, Challenge

## Copy

Copy and run the **correct** grade calculator example.

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
```

Change the value of `score` and verify that the output makes sense.

## Change

Reorder the conditions so that the program produces an **incorrect result** for at least one score. Run the program and observe what goes wrong.

## Challenge

Write your own program that uses `if`, `elif`, and `else` to categorize a number into **at least four different ranges**. Test it with multiple values to ensure the conditions are ordered correctly.
