# Overview
We have now assigned some string variables with literals. What if we wanted the user to give us a value to display instead? We can do this with `input`. 

# Set Up
Create a new python file and call it `userinput.py`.

# Important Info
When we are asking for user input, usually we want to save it as a variable.

We can also give a prompt as part of our input code that allows the user to know why we are asking for input.

Input is received through the terminal. To send input, you just type your message and hit `Enter`.

All user input is always processed as a string, even if the user typed in numbers.

# Copy
Copy the following code and run it.

```python
name = input("What is your name?")
print("Hello")
print(name)
```

What happens when you run this program? What happens if you never provide an input? Did you notice that the input from the user is right next to the prompt with no space in between?

# Change
Try and change the code so there is a space between the prompt and the user's input when they are typing.

# Challenge
Create a program that asks for the user's age, and then prints a message saying how old they are.