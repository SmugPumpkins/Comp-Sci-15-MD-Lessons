# Overview

This lesson builds on your understanding of `for` loops by introducing **`break`** and **`continue`**. You will learn how each keyword changes the flow of a loop, how they are different from one another, and why they only affect the **loop they are currently inside**, even when used within an `if` statement or other control structure.

# Important Information

## Controlling a Loop While It Is Running

Up to this point, every `for` loop you have written has followed a predictable pattern: it starts at the beginning, runs through every iteration, and then ends. In real programs, this is not always what you want. Sometimes you need to stop a loop early, or skip certain values while letting the rest of the loop continue normally.

Python provides two keywords that allow you to control a loop while it is running: `break` and `continue`. Although they are often taught together, they have very different effects on how a loop behaves.

## What `break` Does

The `break` keyword immediately ends the loop it is inside. When Python encounters a `break` statement, it stops the loop entirely and jumps to the first line of code after the loop. No further iterations of that loop will run.

```python
for i in range(10):
    if i == 5:
        break
    print(i)

print("Loop finished")
```

Output:

```
0
1
2
3
4
Loop finished
```

In this example, the loop begins normally, but as soon as `i` becomes `5`, the `break` statement runs. The loop stops immediately, and Python moves on to the code after the loop.

## What `continue` Does

The `continue` keyword does not stop the loop. Instead, it stops only the **current iteration**. When Python encounters `continue`, it skips the rest of the code in that iteration and moves directly to the next iteration of the loop.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```
0
1
3
4
```

Here, the loop still runs the same number of times, but when `i` is `2`, the `print` statement is skipped for that iteration only. The loop then continues normally with the next value.

## The Key Difference Between `break` and `continue`

The most important distinction to remember is that `break` ends the loop completely, while `continue` only skips part of the loop once. A `break` means “stop looping,” whereas a `continue` means “skip this turn and keep going.” Mixing these up can dramatically change how your program behaves.

The `break` keyword is commonly used when a loop no longer needs to continue, such as when a desired value has been found or when further work would be unnecessary. Ending the loop early can make programs faster and easier to reason about.

The `continue` keyword is useful when certain values should be ignored but the loop should otherwise continue as normal. This often appears when filtering data or skipping invalid input while processing the rest.

## Using `break` and `continue` Inside `if` Statements

In practice, `break` and `continue` are almost always used inside conditional statements. Even when they are nested inside an `if`, they still apply to the loop, not to the `if` itself.

```python
for letter in "python":
    if letter == "h":
        break
    print(letter)
```

As soon as the letter `"h"` is reached, the `break` statement runs and the loop ends.

```python
for letter in "python":
    if letter == "h":
        continue
    print(letter)
```

In this version, only the iteration where the letter is `"h"` is skipped. All other letters are printed as normal.

## `break` and `continue` Only Affect the Current Loop

Both `break` and `continue` apply only to the loop they are directly inside. If loops are nested, these keywords affect the **inner loop**, not any outer loops.

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

In this example, the `break` statement stops the inner loop when `j` equals `1`, but the outer loop continues to run. This rule is extremely important when working with nested loops.

## Using `return` Inside a Loop That Is Inside a Function

When a loop is inside a **function**, there is a third keyword that can stop the loop: `return`. The `return` keyword behaves differently from `break` and `continue` because it does **more than just control the loop**.

When Python encounters a `return` statement, three things happen immediately. First, the current loop stops running. Second, the function stops executing entirely. Third, the function sends a value back to wherever it was called (if a value is specified).

This means that `return` exits **both the loop and the function at the same time**.

```python
def find_number(numbers):
    for number in numbers:
        if number == 5:
            return "Found 5"
    return "5 not found"
```

In this example, if the value `5` is found, the loop stops and the function immediately returns `"Found 5"`. The loop does not continue checking the remaining values, and no other code in the function runs.

If the loop finishes without finding `5`, the function reaches the final `return` statement instead.

It is important to understand that `return` is **stronger than `break`**. A `break` only exits the loop and then continues running the rest of the function. A `return` exits the loop **and** exits the function.

```python
def example():
    for i in range(10):
        if i == 3:
            return i
        print(i)
    print("Loop finished")
```

In this case, when `i` becomes `3`, the function immediately returns `3`. The message `"Loop finished"` is never printed because the function has already ended.

This behavior makes `return` especially useful when a function’s job is complete as soon as a certain condition is met. However, it also means you must use it carefully. If you use `return` inside a loop unintentionally, your function may stop much earlier than you expect.

The key idea to remember is this:
`break` exits a loop, `continue` skips an iteration, but `return` exits the **entire function**, taking the loop with it.


# Set Up

Create a new Python file called `break_continue.py`.

# Copy, Change, Challenge

## Copy

Copy and run the following code.

```python
for i in range(10):
    if i == 4:
        break
    print(i)
```

Then run this version.

```python
for i in range(10):
    if i == 4:
        continue
    print(i)
```

Observe exactly how the output changes.

## Change

* Modify the second loop so that it skips **all numbers less than 3**
* Make sure the loop still prints the remaining numbers normally

## Challenge

Write a program that:

* Iterates over a string
* Uses `break` to stop the loop when a specific character is found
* Uses `continue` to skip a different character
* Clearly demonstrates that the loop still behaves normally otherwise
