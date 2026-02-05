# Challenge - Debug Type Errors
The object of this challenge is to practice identifying and debugging type errors.

## Mild 🌶️
Copy and run the following code.

```python
def rectangular_prism_volume(length, width, height):
    return length * width * height

length = 5
width = "4"
height = 3

volume = rectangular_prism_volume(length, width, height)
print(volume)
```

Debug the code so it still maintains functionality, but does not raise errors.

## Medium 🌶️🌶️
Copy and run the following code.

```python
def rectangular_prism_surface_area(length, width, height):
    lw = length * width
    lh = length * height
    wh = width * height
    return 2 * (lw + lh + wh)

length = "10"
width = 4
height = "2"

area = rectangular_prism_surface_area(length, width, height)
total = area + " cm^2"
print(total)
```

Debug the code so it still maintains functionality, but does not raise errors.

## Spicy 🌶️🌶️🌶️
Copy and run the following code.

```python
def shipping_cost(weight, rate):
    return weight * rate

box_length = "30"
box_width = 20
box_height = "10"

volume = box_length * box_width * box_height

density = 0.5
mass = volume * density

cost = shipping_cost(mass, "1.25")
final_cost = cost + 10
print(final_cost)
```

Debug the code so it still maintains functionality, but does not raise errors.