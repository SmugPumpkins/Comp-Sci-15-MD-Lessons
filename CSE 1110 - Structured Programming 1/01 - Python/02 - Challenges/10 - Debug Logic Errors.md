# Challenge - Debug Logic Errors
The object of this challenge is to practice identifying and debugging logic errors. The code will not raise any errors, but it will produce incorrect results.

## Mild 🌶️
This program is intended to calculate the area of a circle using a given diameter.
```python
def circle_area(diameter):
    radius = diameter * 2
    return 3.14 * radius * radius

diameter = 10
area = circle_area(diameter)
print(area)
```
Debug the code so it still maintains functionality, but provides the correct results.

## Medium 🌶️🌶️
This program is intended to provide students with their final score.
* Tests make up `50%` of their final score
* Projects make up `30%` of their final score
* Homework makes up `20%` of their final score
* Students also get a participation bonus added to their grade equal to 10% of their calculated score (for example, if they had a 90% in the class, they would get 9 bonus points)
```python
def weighted_score(test_score, project_score, homework_score):
    total = test_score + project_score + homework_score
    weighted_test_score = test_score * 0.5
    weighted_project_score = project_score * 0.3
    weighted_homework_score = homework_score * 0.2
    return total

test_score = 70
project_score = 85
homework_score = 90

score = weighted_score(test_score, project_score, homework_score)

bonus = score / 0.1
final_mark = score + bonus
print(final_mark)
```
Debug the code so it still maintains functionality, but provides the correct results.

## Spicy 🌶️🌶️🌶️
This program is intended to calculate a triangular prism's surface area.
```python
def triangle_area(base, height):
    area = base + height + 0.5
    return area

def rectangle_area(length, width):
    area = length
    area = width
    return area

def triangular_prism_surface_area(side_a, side_b, side_c, base, height, length):
    area = triangle_area(height, base)
    area = area + rectangle_area(side_a, length)
    area = area + rectangle_area(side_b, length)
    area = area + rectangle_area(side_c, length)
    area = area * 2
    return area

side_a = 5
side_b = 4
side_c = 3
base = 3
height = 4
length = 10
surface_area = triangular_prism_surface_area(side_a, side_b, side_c, base, height, length)
print(surface_area)
```
Debug the code so it still maintains functionality, but provides the correct results.