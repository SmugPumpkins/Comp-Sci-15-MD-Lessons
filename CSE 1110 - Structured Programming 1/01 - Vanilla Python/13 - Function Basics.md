# Overview
We have now input values, processed values, and output values. That is a large part of the computer science curriculum.

The other large part comes from breaking the different processes you will program into modules. In this course, the modules we will be focusing on are functions.

# Important Information
A function is a block of code that only runs when it is called. 

Every function has:
- A name
- the `def` keyword
- a pair of parenthesis `()`
- a colon `:` to signify where the block of code begins
- an indented block of code beneath it

Code defined in a function is reusable, and can be added in the program as many times as the user sees fit.

## Definition
Let's look at an example of a function definition.
```python
def greet():
    print("Hello, World!")
```
- `def` tells us this is a function
- the function is named `greet`
- double parenthesis and a colon are required `():`
- `print("Hello World")` is the indented block of code

## Calling Functions
If we wanted to call this function later it would look like this:
```python
greet()
```

Putting it all together we get code that looks like this:
```python
# Define the function here
def greet():
    print("Hello, World!")

# Call the function here
greet()
```

## Order Matters
Another thing that is important to note about functions is that in python, functions ALWAYS need to be defined before they are called. In some languages it doesn't matter where you put your functions, but in python your functions need to be written above the place they are called in your code. 

The following code will run just fine:
```python
# Function definition before function is called
def greet():
    print("Hello, World!")

# Function is called after being defined
greet()
```

However, this code will not:
```python
# Function called before being defined, results in a NameError
greet()

def greet():
    print("Hello, World!")
```

When a function is called before it is defined, we get a `NameError` because the function is trying to be called before it is defined. The easiest fix for this is to ensure the function is defined before it is called.

## Function Scope
Sometimes you will want to use variables inside of functions. In python, functions are a special part of the code that treat variables differently than other parts of the code. This is called variable scope.

At this point, we will focus on local and global scope for variables.

Variables that are declared inside of functions have a local scope. This means that the only place in your code that the variable can be accessed, assigned, compared, or seen by your code is within the function. Variables from a function cannot be accessed outside of that function.
```python
def greet():
    # message is a local variable to the greet function
    message = "Hello, World!"
    # message can be accessed here because it is in the function
    print(message)

# message cannot be accessed here because it is outside of the function. This will result in a NameError
print(message)
```

Variables that are declared outside of functions have global scope, meaning that they can be accessed anywhere in your code.
```python
# message is declared as a global variable
message = "Hello, World!"

def greet():
    print(message)

# message is global so this line does not result in an error
print(message)

# when greet is called we get a NameError even though message is a global variable...
greet()
```

By default, global variables aren't accessed inside of functions. To access a global variable inside of a function, you need to use the `global` keyword.
```python
# message is declared as a global variable
message = "Hello, World!"

def greet():
    # by specifying that we want to use the global message variable, python interprets this variable as intended
    global message
    print(message)

# message is global so this line does not result in an error
print(message)

# no more errors!
greet()
```