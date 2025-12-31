# Overview

This lesson introduces **nesting conditionals**, which means placing one `if` statement inside another. You will learn why nested conditionals exist, how they are different from using logical operators like `and`, and when nesting is the **better and safer choice**, especially when dealing with missing or invalid values.

# Important Information

## What Nesting Conditionals Means

A conditional is **nested** when an `if` statement appears inside the body of another `if` statement. The inner condition is only checked **after** the outer condition has already been confirmed to be `True`.

```python
age = 16

if age >= 13:
    if age < 18:
        print("Teenager")
```

In this example, Python first checks whether `age >= 13`. Only if that condition is `True` does it move on to check the second condition.

## Why Nest Conditionals at All?

At first glance, nested conditionals can seem unnecessary because many conditions can be combined using logical operators like `and`.

```python
if age >= 13 and age < 18:
    print("Teenager")
```

This version works, and in simple cases it is perfectly fine. However, nesting conditionals becomes important when **some checks must happen before others** to keep the program safe or readable.

## Nesting vs `and`

When you use `and`, Python evaluates both sides of the condition as part of a single expression. When you nest conditionals, Python evaluates conditions **one at a time**, in a specific order that you control.

```python
if condition_a and condition_b:
    do_something()
```

This reads as “check both conditions together.”

```python
if condition_a:
    if condition_b:
        do_something()
```

This reads as “only check the second condition if the first one is already true.”

That difference becomes critical in certain situations.

## Nesting Is Safer for Null Checks

One of the most important reasons to nest conditionals is when checking values that **might not exist** or **might be empty**.

Consider this example:

```python
name = None

if name != None and len(name) > 0:
    print("Name provided")
```

This code is dangerous. If `name` is `None`, Python will still attempt to evaluate `len(name)`, which causes an error because `None` has no length.

Now look at the nested version:

```python
name = None

if name != None:
    if len(name) > 0:
        print("Name provided")
```

Here, `len(name)` is only evaluated **after** Python confirms that `name` is not `None`. This prevents the program from crashing.

This pattern is extremely common in real-world programming and is one of the strongest reasons to use nested conditionals instead of `and`.

## Nesting Improves Readability for Complex Logic

Nested conditionals can also make complex logic easier to understand by breaking decisions into **clear steps**.

```python
user_logged_in = True
is_admin = False

if user_logged_in:
    if is_admin:
        print("Admin access granted")
```

This reads naturally: first check whether the user is logged in, then check whether they are an admin. Using `and` here would work, but nesting can make the intent clearer, especially as conditions become more complex.

## Nested Conditionals with `else`

Nested conditionals can include `else` blocks as well, allowing you to handle different outcomes at different levels.

```python
score = 85

if score >= 50:
    if score >= 80:
        print("High pass")
    else:
        print("Pass")
else:
    print("Fail")
```

This structure allows the program to make layered decisions instead of trying to describe everything in a single condition.

## When to Prefer Nesting Over `and`

Nesting conditionals is usually the better choice when:

* A later check depends on an earlier check being valid
* You are protecting against invalid or missing values
* The logic is easier to understand step by step
* You want to avoid runtime errors

Using `and` is usually better when:

* All conditions are simple and safe to evaluate
* No condition depends on another existing first
* Readability is not harmed

Understanding when to nest conditionals is a key skill that separates beginner code from **robust, defensive code**.

# Set Up

Create a new Python file called `nested_conditionals.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
username = "admin"

if username != None:
    if username == "admin":
        print("Welcome, admin")
```

Change `username` to `None` and confirm that the program does not crash.

## Change

Rewrite the program using a single `if` statement with `and`. Then test it with `username = None`. Observe what happens and explain why.

## Challenge

Write a program that:

* Uses **nested conditionals**
* Performs a **safety check** before a more specific check
* Would be unsafe or unclear if written using only `and`

Your goal is to demonstrate that you understand **why** nesting conditionals exists, not just how to write them.
