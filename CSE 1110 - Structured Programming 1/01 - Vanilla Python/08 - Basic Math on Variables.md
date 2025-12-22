# Overview
So now we know how to get the user to input variables, and we've learned some basic math for python. To make our variables more useful, we can look at how to change them.

# Important Information
To do math with a variable in python, the variable always needs to be declared. When we give a variable a name and a value, this is called declaring the variable. A variable cannot be used until it has been declared.

Later, when we want to change the value of the variable, we call it __assigning__ a value to the variable. A variable can be assigned a new value as often as needed and as many times as needed.

## Assigning with a Literal
When we want to assign a new value to a variable, we can always just use a literal (when we literally type the value).
```python
# Declare the variable.
my_variable = 7

# Assign a new value with a literal
my_variable = 100
```

## Assigning with an Expression
We can also use an expression to assign the value of a variable. The expression can use literals or other variables.
```python
# Assigning with a literal expression
my_variable = 50 + 40

# Assigning with a variable as part of the expression
my_second_variable = my_variable + 10

# Assigning with just a variable as the expression
my_third_variable = my_second_variable
```

## Assigning By Changing The Variable
Sometimes we want to change the variable by a certain amount. A common case for this is incrementing the variable (increasing it by 1) or decrementing the variable (decreasing it by 1).

To change a variable by a particular amount, you need to use the variable you want to change as part of the expression.
```python
# Declaring the variable with a starting value of 0
my_variable = 0

# Increase my_variable by 10
my_variable = my_variable + 10 # new value is 10

# Decrease my_variable by 3
my_variable = my_variable - 3 # new value is 7

# Multiply my variable by 5
my_variable = my_variable * 5 # new value is 35

# Divide my variable by 7
my_variable = my_variable / 7 # new value is 5
```

## Assigning with Shorthand
Changing a variable by a specific amount is a very common thing to do in programming. Because of this, programmers will often use shorthand to program when a value is changing by a specific amount.
```python
# Declaring the variable with a starting value of 0
my_variable = 0

# Increase my_variable by 10
my_variable += 10 # new value is 10

# Decrease my_variable by 3
my_variable -= 3 # new value is 7

# Multiply my variable by 5
my_variable *= 5 # new value is 35

# Divide my variable by 7
my_variable /= 7 # new value is 5
```
# Set Up
Create a new file called `basicmathvariables.py`.
# Copy
Let's start with a variable that we will add to and then print.
```python
my_number = 100
my_number = my_number + 200
print(my_number)
```

# Change
Make it so that `200` is added to `my_number` with shorthand.

# Challenge
Start with a number.
Add `0` to it and print it.
Subtract `50` from it and print it.
Multiply it by `17` and print it.
Divide it by `20` and print it.

# Copy
Let's try one more thing. Run the following code and see what happens (even if you have a red line, try running the code).
```python
my_number = 100
my_number += another_number
print(my_number)
```

You just discovered a new kind of error! A `NameError` happens when a variable (or function, which we will learn about later) is used in the code without being declared.

To fix a `NameError`, all you need to do is make sure the variable is declared before being used in the code.

# Change
Fix the error so that `another_number` is declared.