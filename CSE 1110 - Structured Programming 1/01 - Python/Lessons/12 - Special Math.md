# Overview
Previously we learned how to do some basic math operations. However, there will be times where the math you want to do is not covered with addition, subtraction, multiplication, or division.

There are some simple math operations included with python that allow for common math to take place without needing to program it all manually.

# Important Information
There are 3 special operations we will look at right now. Hopefully these are tools that make your tool belt a little more useful.

## Floor Division
One thing you might want to do is divide by a number, but only look at the integer value and ignore the decimal. 

This is useful for calculations where you are dealing with objects that can't exist as partial values.

Consider a situation where you have 28 jelly beans, and 9 friends. The jellybeans can't be cut, and everyone needs the same amount. How many jelly beans should each person have? 3!

To express floor division in python we use this symbol `//`. It's like the division symbol but twice (wow, so cool!).

## Exponential Multiplication
Sometimes you want to multiply a value by a power. Instead of writing 3\*3\*3*3 (which would be 3 to the power of 4) we can right 3**4 which represents an exponent.

To express exponential multiplication we use `**`, which just like floor division is just two of our multiplication symbols.

## Modulo Division
The last circumstance we might find ourselves in is needing a remainder.

Remember our 28 jelly beans and 9 friends? When each person gets 3 jelly beans, that only divides 27 of our original 28 jelly beans! We have a remainder of 1!

Modulo division can give us the remainder of a division. If we did 28%9, we would get 1 because 28/9 is 3, remainder 1.

Modulo division uses the `%` symbol. It is really important to remember that in programming `%` does not represent percent, it represents a remainder.

# Set Up
Create a new file called `specialmath.py`.

# Copy
Run the following program
```python
friends = 9
jelly_beans = 28
each_person_gets = 28 // 9
remainder = 28 % 9
print(f"Each person gets {each_person_gets} jelly beans and there are {remainder} left over")
```

# Change 
Change the values so that the remainder jelly beans will be greater than the number of jelly beans each person gets.

# Challenge
Create you own situation where you use floor division and modulo division to determine how some kind of object id divided.
