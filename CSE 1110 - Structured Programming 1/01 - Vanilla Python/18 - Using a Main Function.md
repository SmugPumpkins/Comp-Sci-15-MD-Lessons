# Overview

In this lesson, you will learn how to organize programs that use **multiple functions across multiple files**, while preventing code from running when a file is imported as a module. You will learn how and why to use a `main` function, and how Python decides what code should run.

This lesson is designed to make these ideas as **clear and predictable** as possible.

# Important Information

As programs grow, they often:

* Use many functions
* Use helper files (modules)
* Have one clear place where the program *starts*

Without structure, importing files can cause code to run when you do **not** want it to.

## The Problem: Code Running on Import

By default, **Python runs every line of code in a file from top to bottom**.

That includes:

* `print()` statements
* Function calls
* Any code not inside a function

Example:

`helpers.py`

```python
def greet():
    print("Hello!")

print("Helpers file running")
```

`main.py`

```python
import helpers
```

When `main.py` runs, this prints:

```
Helpers file running
```

This happens even though `greet()` was never called.

This is often **not what the programmer intends**.

## The Goal

We want:

* Helper files to define functions
* Code to run **only when we choose**
* One clear starting point for the program

This is done using:

* A `main` function
* A special Python check using `__name__`

## The `main` Function

A common pattern is to put the main logic of a program inside a function called `main`.

Example:

```python
def main():
    print("Program starting")
```

On its own, this function does nothing until it is called.

## How Python Knows What File Is Running

Python keeps track of which file is being run directly.

* If a file is run directly, Python sets a special variable called `__name__` to `"__main__"`
* If a file is imported, `__name__` is set to the file’s name

You do **not** change `__name__`. Python does this automatically.

## Preventing Code From Running on Import

This is the key pattern to remember:

```python
if __name__ == "__main__":
    main()
```

This means:

* “Only run `main()` if this file is the one being run directly”
* “Do not run this code if the file is imported”

## Complete Example

`helpers.py`

```python
def greet():
    print("Hello from helpers")

def add(a, b):
    return a + b
```

No code runs automatically when this file is imported.

`main.py`

```python
from helpers import greet, add

def main():
    greet()
    result = add(3, 4)
    print(result)

if __name__ == "__main__":
    main()
```

What happens:

* `helpers.py` defines functions only
* `main.py` controls when the program runs
* Code does not run accidentally on import

## Why This Helps

Using this pattern:

* Prevents unexpected output
* Makes programs easier to read
* Makes debugging easier
* Makes files safe to import

## Common Errors and Fixes

### Error: Code Runs When Imported

**Cause**: Code is written at the top level
**Fix**: Move the code into `main()` and use the `__name__` check

### Error: Nothing Runs

**Cause**: `main()` exists but is never called
**Fix**:

```python
if __name__ == "__main__":
    main()
```

### Error: NameError for a Function

**Cause**: Function is called before it is defined or imported
**Fix**:

* Define functions above `main()`
* Import functions before using them

### Error: Multiple Files Running Code

**Cause**: More than one file has top-level code
**Fix**:

* Only one file should act as the main program
* Other files should define functions only

# Set Up

Create two Python files:

* `helpers.py`
* `main.py`

# Copy, Change, Challenge

## Copy

`helpers.py`

```python
def say_hi():
    print("Hi!")
```

`main.py`

```python
from helpers import say_hi

def main():
    say_hi()

if __name__ == "__main__":
    main()
```

Run `main.py`.

## Change

Add another function to `helpers.py` and call it from inside `main()`.

## Challenge

Create a program with:

* At least three helper functions
* A `main()` function that calls all of them
* No code that runs automatically when files are imported
