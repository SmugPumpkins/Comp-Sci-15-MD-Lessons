# Challenge - Area and Volume Calculator
The object of this challenge is to create functions that can accept arguments and return values.

## Mild 🌶️
Create 2 functions from the following choices:

|Function|Input|Output|
|---|---|---|
|Rectangle Area|`l` (length)<br>`w` (width)|`area`|
|Triangle Area|`b` (base)<br>`h` (height)|`area`|
|Circle Area|`r` (radius)|`area`|

Then create a program that satisfies the following requirements:

* For each function you created:
    * The user provides input.
    * The program uses your function to calculates the area of that shape.
    * The program outputs a message displaying the calculated area and what shape that area is for.

## Medium 🌶️🌶️
Create the following function:

|Function|Input|Output|
|---|---|---|
|Circle Area|`r` (radius)|`area`|

For your function create 3 tests using `pytest`:

* The function must have at least one test that `asserts` that 2 values are approximately equal.
* The function must have at least one test that `asserts` that 2 values are not approximately equal.

Then create a program that satisfies the following requirements:

* For each function you created:
    * The user provides an input.
    * The program uses your function to calculate slope.
    * The program outputs a message displaying the calculated area.

## Spicy 🌶️🌶️🌶️
Create the following 2 functions:

|Function|Input|Output|
|---|---|---|
|Cylinder Volume|`r` (radius)<br>`h` (height)|`volume`|
|Cylinder Surface Area|`r` (radius)<br>`h` (height)|`surface_area`|

For each of your functions create 2 tests using `pytest`:

* Each function must have one test that `asserts` that 2 values are approximately equal.
* Each function must have one test that `asserts` that 2 values are not approximately equal.

Then create a program that satisfies the following requirements:

* For each function you created:
    * The user provides an input.
    * The program uses your function to calculate slope.
    * The program outputs a message displaying the calculated value and what the value is *(for example, volume of a cylinder)*.