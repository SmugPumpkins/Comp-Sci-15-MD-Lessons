# Overview

In this lesson, you will learn how to use **multiple Python files together** in a single program. You will learn how to organize code using helper files, different ways to import code, how naming works when importing, and why importing files can sometimes cause unexpected behavior.

# Important Information

As programs grow larger, keeping all code in one file becomes difficult to manage. A common solution is to split code across multiple Python files.

Each Python file is called a **module**.

Using multiple files helps you:

* Keep related code together
* Reuse helper functions
* Make programs easier to read and debug

## Helper Files

A helper file is a Python file that contains functions meant to be used by another file.

For example:

* One file might handle calculations
* Another file might handle text output
* The main file connects everything together

Helper files usually contain **function definitions only**, not code that runs automatically.

## Importing an Entire File

You can import an entire Python file using the `import` keyword.

Example file structure:

* `helpers.py`
* `main.py`

`helpers.py`

```python
def say_hello():
    print("Hello from helpers!")
```

`main.py`

```python
import helpers

helpers.say_hello()
```

When you import the whole file:

* You must use the file name as a prefix
* This prefix is called a **namespace**
* It helps avoid name conflicts

## Importing a File With an Alias

Sometimes file names are long or awkward to type. Python allows you to rename a module when importing it using `as`.

```python
import helpers as h

h.say_hello()
```

This:

* Shortens the namespace
* Makes code faster to write
* Still keeps names organized

Aliases are especially useful when:

* Module names are long
* Multiple modules have similar names

## Code Runs on Import

A very important rule in Python:

**When a file is imported, all top-level code in that file runs immediately.**

Example:

`helpers.py`

```python
print("Helpers file is running")

def add(a, b):
    return a + b
```

`main.py`

```python
import helpers

print("Main file is running")
```

Output:

```
Helpers file is running
Main file is running
```

Even though `add()` was never called, the `print()` statement ran because it was not inside a function.

For now, the safest rule is:

* Helper files should mostly contain function definitions
* Avoid code that runs automatically at the top level

## Importing Specific Functions

Instead of importing an entire file, you can import only the functions you need.

```python
from helpers import add
```

Now you can call the function directly:

```python
result = add(3, 4)
print(result)
```

Notice:

* No file name prefix is needed
* The function name is placed directly into your program’s namespace

## Importing Multiple Specific Functions

You can import more than one function at a time.

```python
from helpers import add, subtract
```

Calling the functions:

```python
total = add(5, 2)
difference = subtract(5, 2)
print(total)
print(difference)
```

This is useful when:

* You only need a handful of functions
* You want clean, readable code
* You want to avoid long namespaces

## Importing Everything With `*`

Python also allows importing **everything** from a file.

```python
from helpers import *
```

After this:

* All functions and variables in `helpers.py` are available
* You can call them directly without a prefix

Example:

`helpers.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

`main.py`

```python
from helpers import *

print(add(4, 2))
print(subtract(4, 2))
```

### Use With Caution

While `import *` can be convenient, it has drawbacks:

* It is unclear where functions come from
* Name conflicts are more likely
* Code becomes harder to read

In this course:

* `import *` should only be used in **small, controlled programs**
* Prefer importing specific functions whenever possible

## Choosing How to Import

General guidelines:

* `import helpers` → clear structure and namespaces
* `import helpers as h` → same clarity with shorter names
* `from helpers import add` → best when using a few functions
* `from helpers import *` → use sparingly and carefully

# Set Up

Create two Python files:

* `helpers.py`
* `main.py`

# Copy, Change, Challenge - Importing Helpers

## Copy

`helpers.py`

```python
def multiply(a, b):
    return a * b
```

`main.py`

```python
import helpers as h

result = h.multiply(4, 5)
print(result)
```

## Change

Rename the alias `h` to something else and update the function call.

## Challenge

Add two more functions to `helpers.py` and call all of them using the alias.


# Copy, Change, Challenge - Importing  Functions Directly
## Copy

`helpers.py`

```python
def greet():
    print("Hello!")

print("Helpers loaded")
```

`main.py`

```python
from helpers import greet

greet()
```

Run `main.py` and observe what prints.

## Change

Move the `print("Helpers loaded")` line into a function so it no longer runs automatically.

## Challenge

Rewrite the program using `from helpers import *` and call at least two functions directly.
