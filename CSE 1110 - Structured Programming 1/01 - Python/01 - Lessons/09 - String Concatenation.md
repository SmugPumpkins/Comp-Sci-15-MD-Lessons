# Overview
Now that we have some experience with taking input and a little bit of processing our data, the next 3 lessons will focus on formatting out output when we print to the Terminal.

# Important Information
This first technique is called string concatenation (kon-kat-uh-NAY-shun). It is as simple as jamming strings together.

The big benefit to concatenation is that the programmer has full control of the way the string comes out.

The downside is that it's inefficient to code and leads to code that is challenging to maintain. Every value you concatenate needs to be turned into a string, and that takes a lot of work.

This technique is also the hackiest way to do it. It technically works, but it's a very brute force way to do it.

# Set Up
Create a new file called `stringconcatenation.py`.

# Copy
Run the following code and see what happens.
```python
message = "Hello"
name = "Mr. Forsyth"
print(message + name)
```
Does the message display the way you think the user intended it to?

# Change
Add another variable called `space` and concatenate it into the print function so the message displays properly.

# Challenge
Write a haiku where each syllable is it's own string variable. Add the syllables together and print your haiku.