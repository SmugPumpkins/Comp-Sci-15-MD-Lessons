# Overview

This lesson builds on your understanding of `if` statements by introducing **comparison operators**. You will learn how to compare numbers using operators like less than and greater than, how to check for inequality, and how comparisons work with **non-number values** such as strings.

# Important Information

## What Comparison Operators Are

A **comparison operator** checks the relationship between two values. The result of any comparison is always a **boolean value**: `True` or `False`. These comparisons are most commonly used inside `if` statements to control whether code runs.

```python
if 5 > 3:
    print("This runs")
```

Because `5 > 3` is `True`, the code runs.

## Equality and Inequality

The most basic comparison operator is `==`, which checks if two values are equal.

```python
if 10 == 10:
    print("Equal")
```

The opposite of equality is **inequality**, which uses `!=`.

```python
if 10 != 5:
    print("Not equal")
```

This code runs because `10` is not equal to `5`.

## Greater Than and Less Than

Python allows you to compare numeric values using greater-than and less-than operators.

```python
if 8 > 3:
    print("8 is greater than 3")
```

```python
if 2 < 5:
    print("2 is less than 5")
```

These comparisons are strictly greater or strictly less. Equality does not count.

## Greater Than or Equal To / Less Than or Equal To

Sometimes you want to include equality in the comparison. Python provides `>=` and `<=` for this purpose.

```python
score = 70

if score >= 70:
    print("You passed")
```

This code runs because `70` is equal to `70`.

```python
temperature = 0

if temperature <= 0:
    print("Freezing")
```

This code also runs because `0` meets the condition.

## Using Comparisons in If Statements

Comparison operators are most useful when combined with variables inside `if` statements.

```python
age = 12

if age < 18:
    print("Minor")
```

If the condition is `False`, Python simply skips the block without an error.

```python
age = 20

if age < 18:
    print("Minor")

print("Done")
```

Only `"Done"` prints because the condition is not met.

## Comparing Non-Number Values (Strings)

In Python, **strings are compared using the same operators** as numbers. There is **no** `.equals()` method in Python. Equality is checked using `==`.

```python
name = "Alex"

if name == "Alex":
    print("Name matched")
```

Inequality also works the same way.

```python
password = "guest"

if password != "admin":
    print("Access denied")
```

Strings can also be compared alphabetically using `<` and `>`. Python compares strings letter by letter based on their order in the alphabet.

```python
if "apple" < "banana":
    print("apple comes first")
```

This works because `"a"` comes before `"b"` alphabetically.

String comparisons are **case-sensitive**.

```python
if "Python" == "python":
    print("Same")
```

This condition is `False` because uppercase and lowercase letters are different.

# Set Up

Create a new Python file called `comparison_operators.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
number = 15

if number > 10:
    print("Greater than 10")

if number == 15:
    print("Equal to 15")

if number != 20:
    print("Not equal to 20")
```

Observe which lines print and why.

## Change

Change the value of `number` so that **only one** of the messages prints when the program runs.

## Challenge

Write a program that:

1. Stores a word in a variable.
2. Uses **at least two different comparison operators** to compare that word.
3. Prints messages only when the conditions are `True`.

Test your program by changing the value of the word and observing how the output changes.
