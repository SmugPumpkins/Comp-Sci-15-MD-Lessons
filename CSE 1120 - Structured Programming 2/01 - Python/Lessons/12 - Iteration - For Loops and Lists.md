# Overview

This lesson builds on your understanding of `for` loops by focusing on **iterating over lists and strings**. You will learn how to loop through each value directly, why this style of loop does **not automatically provide a counter**, when that behavior is useful, and how to use **`enumerate()`** when both the position and the value matter.

# Important Information

## Iterating Over a List

When you iterate over a list, the loop variable represents **each value in the list**, one at a time.

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(color)
```

In this loop, `color` is not a number. It is the actual value stored in the list. The loop runs once for each item.

This style of loop is useful when you care about **what the values are**, not where they are stored.

## Iterating Over a String

Strings are sequences of characters, which means they can also be iterated over.

```python
word = "python"

for letter in word:
    print(letter)
```

Each time the loop runs, `letter` stores one character from the string. This is especially useful when you want to inspect or analyze text character by character.

## No Automatic Counter Is Provided

When using the syntax:

```python
for thing in collection:
```

Python does **not** automatically give you a number that tracks how many times the loop has run. You only receive the current value from the collection.

This is different from `for i in range()`, where `i` is a number by design.

## When This Is Useful

Not having a counter is often a **feature**, not a problem.

For example, checking each character in a string:

```python
password = "abc123"

for char in password:
    if char == "!":
        print("Invalid character found")
```

In this case, the position of the character does not matter. Only the value matters.

Another example is processing values in a list:

```python
scores = [85, 90, 72, 88]

for score in scores:
    if score < 75:
        print("Low score detected")
```

You care about the scores themselves, not their index.

## Iterating Over Other Data Structures

Many data structures that store multiple values can be iterated over using the same pattern. Lists and strings are just the most common examples. This idea will apply again when you learn about other collections later.

The key idea is that **iteration works on sequences of values**, not just numbers.

## When the Index *Is* Important

Sometimes you need to know **both**:

* the position of a value (index)
* the value itself

This is where `enumerate()` is used.

## Using `enumerate()` With a List

The `enumerate()` function provides **two values** each time the loop runs:

1. The index (position)
2. The value at that position

```python
names = ["Alex", "Jordan", "Sam"]

for index, name in enumerate(names):
    print(index, name)
```

On each loop:

* `index` is the position (starting at 0)
* `name` is the value from the list at that position

Both variables can be used inside the loop.

## Using `enumerate()` With a String

`enumerate()` also works with strings.

```python
word = "code"

for index, letter in enumerate(word):
    print(index, letter)
```

This allows you to examine characters while also knowing **where** they appear in the string.

## Why `enumerate()` Is Better Than Manual Counting

You might think about creating your own counter variable, but `enumerate()` is clearer and safer.

```python
for index, score in enumerate(scores):
    print("Score", index, "is", score)
```

This avoids mistakes and clearly communicates your intent to anyone reading your code.

# Set Up

Create a new Python file called `iterating_collections.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
animals = ["cat", "dog", "bird"]

for animal in animals:
    print(animal)
```

Then run this version.

```python
for index, animal in enumerate(animals):
    print(index, animal)
```

Compare the output and identify what extra information `enumerate()` provides.

## Change

Modify the program so that:

* The list contains at least five items
* The loop prints a message like:
  `"Item 2 is apple"`

## Challenge

Write a program that:

1. Iterates over a **string**
2. Uses `enumerate()`
3. Prints a message when a specific character appears, including its index

Your goal is to demonstrate that you understand how to use **both the index and the value** inside the same loop.
