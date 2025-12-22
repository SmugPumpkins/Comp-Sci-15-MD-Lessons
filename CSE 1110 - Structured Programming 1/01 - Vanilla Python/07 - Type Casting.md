# Overview
In our last lesson, we looked at how some variable types don't play nice with others. This is especially important to know for when you want to use data retrieved from a user's input.

__ALL USER INPUT IS A STRING EVEN IF THEY TYPED NUMBERS!__

However, sometimes you want to do math with the input a user gave you. That's where type caseing comes in.

# Important Information
When we start off with casting, we are going to assume that our users are nice and cooperative. The first time we use casting, we will assume that our user gave us the information we asked for. 

However, users are not nice. Users break code. This lesson on casting is meant only as a demonstration for changing types, but is not robust enough to be considered "good code".

We will learn more about creating more robust code that users _can't_ break in our next module.

# Copy
Consider a program where we ask for a user's age to determine what year they were born.
```python
age = input("What is your age?")

year_born = 2026 - age

print("You were born in the year" + year_born)
```
Immediately when we run it, we get a `TypeError` because `age` is treated as a string, and `year_born` is trying to subtract a number and a string.

