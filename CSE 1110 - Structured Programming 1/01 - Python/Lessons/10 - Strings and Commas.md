# Overview
This next technique is much more user friendly. It allows the programmer to combine strings and numbers without getting a `TypeError`, it looks clean to write, and you don't need to cast all of your non-string values into strings.

# Set Up
Create a new file called `stringsandcommas.py`.

# Copy
Copy the following code and run it.

```python
name = input("What is your name?")
age = int(input("What is your age?"))
year_born = 2026 - age

print("Hello", name, ". Were you born in", year_born, "?")
```
What do you notice about the commas being used.
Are there any errors from combining numbers and strings?
Are any characters added when we use the commas? Does the spacing change at all?

# Change
Add the user's favourite number to the program.

# Challenge
Make a new program that asks the user gor their pet's name, pet's species, and pet's age. Then display a message to them about their pet with the information you collected.