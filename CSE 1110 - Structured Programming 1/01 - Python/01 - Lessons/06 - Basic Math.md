# Overview
We've taken a brief look at how different variables can have different types, but variables are only really useful to us when we can do something with them.

In this lesson, we will take a closer look at how to do some basic math in python.

We won't do math on variables yet, but this lesson should give you a basic understanding of addition, subtraction, multiplication, and division in python.

## Addition
When we want to add values in python, we use `+`.

## Subtraction
When we want to subtract values in python, we use `-`.

## Multiplication
When we want to multiply a value in python, we use `*`.

## Division
When we want to divide a value in python, we use `/`.

# Set Up
Create a new python file called `basicmath.py`.

# Copy
```python
print(2+2)
```
What do you think will print to the Terminal?

# Change
Alter the value being printed to print a subtraction, multiplication, and a division statement (one at a time).

# Copy
```python
print(0.1+0.2)
```

What do you think will print?

Whoa, that was weird. Why did it add an extra 0.00000000000000004? 

Computers operate in binary, which is a base 2 number system. For integers, this doesn't really matter. However, sometimes decimal values don't behave as expected because the computer approximates the values to the best of it's ability.

This is just a quirk of programming that is important to be aware of.

What do you think will print here?
```python
print(2 + 4 * 2)
```
Will it be 12 or 10? Why do you think that?

What about here?
```python
print(6 / 3 * 2)
```
Will this produce the same outcome?
```python
print(6 / (3 * 2))
```

Brackets can help clarify math, even if they aren't technically needed to get the desired result.