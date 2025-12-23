# Overview

In this lesson, you will learn how to **test functions using pytest**. Testing allows you to automatically check that your functions work correctly and continue working as your program grows. This lesson will focus on setting up pytest, writing test files, following pytest’s naming rules, using `assert` statements, and running tests inside **PyCharm**.

# Important Information

Testing is a core skill in computer science. Instead of manually running your program and checking output every time, tests allow you to:

* Verify that functions behave as expected
* Catch mistakes early
* Make changes with confidence

In this course, we will use **pytest**, a popular Python testing framework.

## What Is pytest?

`pytest` is an external library that:

* Automatically finds test files
* Runs test functions
* Reports which tests pass or fail

pytest is not included with Python by default, so it must be installed.

## Installing pytest

pytest is installed using `pip`, Python’s package manager.

Common installation command:

```bash
pip install pytest
```

After installation, pytest becomes available to your Python environment.

If pytest is installed correctly, running:

```bash
pytest --version
```

will display the installed version number.

## Project Structure for Testing

A common and clear structure is:

* Your main code in one folder
* Your tests in a separate folder

Example:

```
project_folder/
│
├── functions.py
└── tests/
    └── test_functions.py
```

Keeping tests separate helps keep your project organized.

## pytest Naming Rules

pytest relies heavily on **naming conventions**. If these rules are not followed, pytest will not find your tests.

### Test File Names

* Test files **must start with** `test_`
* Example:

  * `test_functions.py`
  * `test_math.py`

### Test Function Names

* Test functions **must start with** `test_`
* Example:

```python
def test_addition():
    ...
```

If either the file name or function name does not start with `test_`, pytest will ignore it.

## Writing a Simple Test

Suppose you have a function in `functions.py`:

```python
def add(a, b):
    return a + b
```

You can test it in `test_functions.py`:

```python
from functions import add

def test_add():
    result = add(2, 3)
    assert result == 5
```

## The `assert` Statement

`assert` is the core of pytest testing.

Syntax:

```python
assert condition
```

What it means:

* If the condition is `True`, the test passes
* If the condition is `False`, the test fails

Example:

```python
assert add(1, 1) == 2
```

You are **not printing results**.
pytest checks the condition for you.

## Testing Multiple Cases

You can write multiple tests for the same function.

```python
def test_add_with_zeros():
    assert add(0, 0) == 0

def test_add_with_negatives():
    assert add(-2, -3) == -5
```

Each test runs independently.

## What Happens When a Test Fails

If a test fails, pytest will:

* Show which test failed
* Show the expected value
* Show the actual value

This feedback helps you quickly find mistakes.

## Running Tests in PyCharm

PyCharm has built-in support for pytest.

To run tests:

1. Open the project in PyCharm
2. Locate the `tests` folder
3. **Right-click** on the `tests` folder
4. Select **“Run tests”**

PyCharm will:

* Run all test files inside the folder
* Show results in a test window
* Highlight failures clearly

You can also:

* Right-click a single test file
* Right-click an individual test function

## Common Errors and Fixes

### pytest Not Found

**Cause**: pytest is not installed in the active environment
**Fix**: Install pytest using `pip` and confirm the correct interpreter is selected in PyCharm

### No Tests Are Running

**Cause**:

* File name does not start with `test_`
* Function name does not start with `test_`

**Fix**: Rename files and functions to follow pytest rules

### Import Errors

**Cause**: Incorrect import path
**Fix**:

* Check file locations
* Ensure your project structure matches your imports

### Using `print()` Instead of `assert`

**Cause**: Misunderstanding how tests work
**Fix**: Replace prints with `assert` statements

## Why Testing Matters

Using pytest helps you:

* Think clearly about what your function should do
* Catch bugs early
* Write more reliable programs
* Prepare for larger projects later in the course

Testing may feel slower at first, but it saves time and frustration as programs become more complex.

# Bad Test or Bad Function?

Now that you know how to write and run pytest tests, the next step is learning how to **design good tests** and how to **interpret failures correctly**.

When testing, it is very important to understand this rule:

**A failing test does not always mean the test is wrong.**
Sometimes the test is correct, and the function being tested is wrong.

Other times:

* The function is correct
* The test is written incorrectly

As the programmer, **you must know the expected result** before writing a test.

## Thinking Like a Tester

Before writing a test, ask yourself:

* What is this function supposed to do?
* What result should I get for specific inputs?
* Can I verify that result without running the code?

Testing is about certainty, not guessing.

## Creating Simple Math Functions

Let’s start by creating a file called `math_functions.py`.

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

These functions are simple enough that we clearly know the expected results.

## Writing Correct Tests

Create a test file called `test_math_functions.py`.

```python
from math_functions import add, subtract

def test_add_basic():
    assert add(1, 4) == 5

def test_subtract_basic():
    assert subtract(10, 3) == 7
```

These tests:

* Use known inputs
* Compare against known correct outputs
* Should pass if the functions are written correctly

## Example of an Incorrect Test

Now let’s look at a test that is written **incorrectly**, even though the function is correct.

```python
def test_add_incorrect_expectation():
    assert add(1, 4) == 6
```

Why this test fails:

* The function `add(1, 4)` correctly returns `5`
* The test incorrectly expects `6`

This is an example of:

* A **bad test**
* A **good function**

When this test fails, the fix is:

* Correct the test
* Not the function

## Example of an Incorrect Function

Now let’s flip the situation.

Change the `subtract` function so it is wrong:

```python
def subtract(a, b):
    return a + b
```

The test stays the same:

```python
def test_subtract_basic():
    assert subtract(10, 3) == 7
```

What happens:

* The test fails
* The expected value is correct
* The function implementation is wrong

This is an example of:

* A **good test**
* A **bad function**

The correct fix here is to fix the function, not the test.

## Fixing the Function

Correct the function back to:

```python
def subtract(a, b):
    return a - b
```

Now the test will pass again.

## Why This Matters

pytest does not know:

* What your function *should* do
* Whether your math makes sense

pytest only checks:

* “Is the actual result equal to the expected result?”

That means:

* **You are responsible for correctness**
* Tests are only as good as the expectations you write

## Testing Multiple Cases

Good tests often include multiple scenarios.

```python
def test_add_with_zero():
    assert add(5, 0) == 5

def test_add_with_negatives():
    assert add(-2, -3) == -5
```

These tests increase confidence that the function works in more situations.

## Interpreting Test Failures

When a test fails, always ask:

1. Is my expected value correct?
2. If yes, is the function implemented correctly?
3. If no, how should the test be fixed?

Never change code blindly just to make tests pass.

## Key Takeaways

* You must know the expected result before writing a test
* A failing test does not automatically mean the function is wrong
* Tests can be wrong
* Functions can be wrong
* pytest helps you find problems, but **you decide what to fix**

Understanding this distinction is one of the most important skills in learning how to test software effectively.
