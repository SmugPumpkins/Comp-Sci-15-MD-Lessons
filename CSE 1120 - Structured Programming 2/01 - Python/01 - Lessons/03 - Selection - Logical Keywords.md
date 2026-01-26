# Overview

This lesson introduces **logical operators**, which allow you to combine or modify conditions inside `if` statements. You will learn how `and`, `or`, `not`, and `^` (xor) work, how Python evaluates them, and how brackets can be used to build very precise conditional logic.

# Important Information

## What Logical Operators Do

Logical operators work with **boolean values** (`True` and `False`). They allow you to combine multiple comparisons into a single condition or change the meaning of a condition.

Logical operators do not compare values themselves. Instead, they combine the **results** of comparisons such as `==`, `<`, or `!=`.

```python
age = 15

if age > 10 and age < 18:
    print("Teenager")
```

Each comparison is evaluated first, and then the logical operator decides the final result.

## The `and` Operator

The `and` operator requires **both conditions** to be `True` for the entire expression to be `True`.

```python
age = 16

if age >= 13 and age <= 19:
    print("Teenager")
```

If either comparison is `False`, the code inside the `if` statement will not run.

### Truth Table for `and`

| Condition A | Condition B | A and B |
| ----------- | ----------- | ------- |
| True        | True        | True    |
| True        | False       | False   |
| False       | True        | False   |
| False       | False       | False   |

## The `or` Operator

The `or` operator requires **at least one condition** to be `True`.

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

If either condition is `True`, the entire condition is `True`.

### Truth Table for `or`

| Condition A | Condition B | A or B |
| ----------- | ----------- | ------ |
| True        | True        | True   |
| True        | False       | True   |
| False       | True        | True   |
| False       | False       | False  |

## The `not` Operator

The `not` operator **reverses** a boolean value. If something is `True`, `not` makes it `False`. If something is `False`, `not` makes it `True`.

```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

This code runs because `not False` becomes `True`.

### Truth Table for `not`

| Condition A | not A |
| ----------- | ----- |
| True        | False |
| False       | True  |

## The `^` Operator (XOR)

The `^` operator represents **exclusive or** (xor). It returns `True` only when **exactly one** condition is `True`. If both are `True` or both are `False`, the result is `False`.

```python
hot_outside = True
wearing_coat = False

if hot_outside ^ wearing_coat:
    print("Ah... the perfect temperature!")
```

This code runs because exactly one condition is `True`.

### Truth Table for `^` (XOR)

| Condition A | Condition B | A ^ B |
| ----------- | ----------- | ----- |
| True        | True        | False |
| True        | False       | True  |
| False       | True        | True  |
| False       | False       | False |

## Combining Logical Operators with Brackets

As conditions become more complex, **brackets (parentheses)** are used to control the order in which logic is evaluated. Python evaluates expressions inside brackets first.
### Example 1
```python
age = 11
has_permission = True

if (age >= 13 and age <= 18) or has_permission:
    print("Allowed to participate")
```

* age >= 13 is `False`
* age <= 18 is `True`
```python
if (False and True) or has_permission:
    print("Allowed to participate")
```
* (`False` and `True`) is `False`
```python
if False or has_permission:
    print("Allowed to participate")
```
* has_permission is `True`
```python
if False or True:
    print("Allowed to participate")
```
* `False` or `True` is `True`
```python
if True:
    print("Allowed to participate")
```
In this case, the message __DOES__ print. Because of the way the brackets are placed, the statement evalueates to `True`.
### Example 2
Let's look at what happens if we switch the bracket placement.

```python
age = 11
has_permission = True

if age >= 13 and (age <= 18 or has_permission):
    print("Allowed to participate")
```
* age <= 18 is `True`
* has_permission is `True`
```python
if age >= 13 and (True or True):
    print("Allowed to participate")
```
* (`True` or `True`) is `True`
```python
if age >= 13 and True:
    print("Allowed to participate")
```
* age >= 13 is `False`
```python
if False and True:
    print("Allowed to participate")
```
* `False` and `True` is `False`
```python
if False:
    print("Allowed to participate")
```
In this case, the message __DOES NOT__ print. Because of the way the brackets are placed, the statement evalueates to `False`.

### Example 3

You can also mix `and`, `or`, and `not` together.

```python
username = "admin"
is_banned = False

if username == "admin" and not is_banned:
    print("Full access")
```

Without brackets, Python follows a built-in order of operations, which can be confusing. Using brackets makes your logic **clearer and safer**.

# Set Up

Create a new Python file called `logical_operators.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
age = 17
has_id = True

if age >= 16 and has_id:
    print("Entry allowed")

if age < 16 or not has_id:
    print("Entry denied")

has_key = True
has_code = False

if has_key ^ has_code:
    print("Unlocked")
```

Observe which messages print and explain why each condition is `True` or `False`.

## Change

Change the values of the variables so that **none** of the messages print when the program runs.

## Challenge

Write a program that:

1. Uses **at least three comparisons**.
2. Combines them using **two different logical operators**.
3. Uses **brackets** to control the logic.
4. Produces different output when you change variable values.

Your goal is to create a conditional that only prints a message when very specific requirements are met.
