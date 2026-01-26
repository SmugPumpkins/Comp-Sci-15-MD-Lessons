# Challenge - Slope Calculator
The object of this challenge is to create functions that can accept arguments and return values.

## Mild 🌶️
Create a function for calculating slope with the following inputs and output:
|Function|Input|Output|
|-|-|-|
|Calcumate `m` (slope)|`Δx`<br>`Δy`|`m` (slope)|

Then create a program that satisfies the following requirements:
* The user provides input.
* The program uses your function to calculate slope.
* The program outputs a message displaying the calculated slope of the line.

## Medium 🌶️🌶️
Create the following 3 functions for calculating slope with the following inputs and outputs:
|Function|Input|Output|
|-|-|-|
|Calculate `m` (slope)|`Δx`<br>`Δy`|`m` (slope)|
|Calculate `Δx`|`m` (slope)<br>`Δy`|`Δx`|
|Calculate `Δy`|`Δx`<br>`m` (slope)|`Δy`|

Then create a program that satisfies the following requirements:
* For each function you created:
    * The user provides input.
    * The program uses your function to calculate slope.
    * The program outputs a message displaying the calculated value and what the value is *(for example, the change in x)*.

## Spicy 🌶️🌶️🌶️
Create a function for calculating the y-intercept of a slope:
|Function|Input|Output|
|-|-|-|
|Calculate `b` (y-intercept)|`x`<br>`y`<br>`m` (slope)|`b` (y-intercept)|

For your function create 3 tests using `pytest`:
* The function must have at least one test that `asserts` that 2 values are equal.
* The function must have at least one test that `asserts` that 2 values are not equal.

Then create a program that satisfies the following requirements:
* The user provides input.
* The program uses your function to calculate the y-intercept of the slope.
* The program outputs a message displaying the y-intercept of the slope.