# Challenge - Debug Value Errors
The object of this challenge is to practice identifying and debugging value errors.

## Mild 🌶️
Copy and run the following code.
```python
def calculate_age(years):
    return int(years)

age = calculate_age("sixteen")
print(age)
```
Debug the code so it still maintains functionality, but does not raise errors.

## Medium 🌶️🌶️
Copy and run the following code.
```python
def rectangle_dimensions(length, width):
    return float(length), float(width)

l, w = rectangle_dimensions("12.5", "four")
area = l * w
message = float("Total area") + str(area)
print(area)
```
Debug the code so it still maintains functionality, but does not raise errors.

## Spicy 🌶️🌶️🌶️
Copy and run the following code.
```python
def budget_calculator(income, expenses):
    return int(income) - int(expenses)

monthly_balance = budget_calculator("3000", "200,000")
savings_goal = float("one thousand")
months_needed = int("12.5")
final_plan = months_needed * savings_goal
print(final_plan)

```
Debug the code so it still maintains functionality, but does not raise errors.