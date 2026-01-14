# Overview

The Circuit Playground Express includes multiple exposed pins that allow it to interact with external components such as LEDs, motors, and other circuits. These pins can be used to send digital signals, which are simple on or off values. In this lesson, you will learn what the different pins are used for, how to safely connect external components, and how to control those components using digital output in CircuitPython.

# Important Information

## Pin Details

![Pinout Diagram](https://cdn-learn.adafruit.com/assets/assets/000/139/941/large1024/makecode_circuit_playground_Adafruit_Circuit_Playground_Express_Pinout_2.png?1758740487)

The Circuit Playground Express exposes its pins as large metal pads around the edge of the board. These pads are designed to be easy to connect to using alligator clips or conductive materials. Each pin can serve a different purpose depending on how it is configured in code.

### Power Pins

![Power pins](https://cdn-learn.adafruit.com/assets/assets/000/047/194/large1024/circuit_playground_powerpads.jpg?1507835537)

The power pins provide electricity to external components. These pins should be used carefully, as incorrect connections can damage components or the board.

They are labeled as:

* `GND` – Ground. This is the reference point for all voltages and must be connected for most circuits to work.
* `3.3V` – A regulated 3.3-volt power output. This is used to power low-voltage components.
* `VOUT` – A higher volt output (for example, 5 volts). The voltage supplied to the board, usually from USB or battery. 

Any external component that needs power will usually connect to one power pin and one other pin for control.

### Input / Output Pins

![IO Pins](https://cdn-learn.adafruit.com/assets/assets/000/047/195/large1024/circuit_playground_iopads.jpg?1507836994)

The remaining pads are input/output pins, often called I/O pins. These pins can send signals out to components or read signals coming in, depending on how they are configured in code.

* A0 / `D12` – This pin can output true analog signals and is commonly used for audio. It can also act as digital or analog I/O, but using it this way interferes with the built-in speaker. This pin cannot be used for capacitive touch.
* A1 / `D6` – This pin can be used for digital I/O or analog input.
* A2 / `D9` – This pin can be used for digital I/O or analog input.
* A3 / `D10` – This pin can be used for digital I/O or analog input.
* A4 / `D3` – This pin can be used for digital I/O or analog input.
* A5 / `D2` – This pin can be used for digital I/O or analog input.
* A6 / `D0` – This pin can be used for digital I/O or analog input.
* A7 / `D1` – This pin can be used for digital I/O or analog input.

In this lesson, we focus only on using these pins as **digital outputs**.

## Importing Libraries

To work with pins as digital outputs, a few libraries must be imported.

```python
import time
import board
import digitalio
```

The `digitalio` library allows pins to be configured and controlled as digital inputs or outputs.

## Writing Digital Values

### Digital Values

Digital signals have only two possible states. These states can be described in several equivalent ways:

* `1` or `0`
* `HIGH` or `LOW`
* `ON` or `OFF`
* `True` or `False`

In CircuitPython, digital pins use `True` and `False` to represent these states. When a pin is set to `True`, it outputs voltage. When it is set to `False`, it outputs no voltage.

### Create a `pin`

Before a pin can be used, it must be created as a `DigitalInOut` object.

```python
my_pin = digitalio.DigitalInOut(board.D10)
```

This line tells CircuitPython which physical pin you want to control. In this case, `board.D10` refers to the pad labeled A3 / D10 on the board.

### Set `pin` to Output

Pins can be used for input or output, but they must be explicitly configured. To send signals out to a component, the pin must be set as an output.

```python
my_pin.switch_to_output()
```

Once a pin is configured as an output, the program is allowed to control its voltage level.

### Write Value to `pin`

After the pin is set as an output, its value can be changed.

```python
# Turn pin on
my_pin.value = True

# Turn pin off
my_pin.value = False
```

Setting the value to `True` sends voltage out of the pin. Setting it to `False` stops the voltage. This is how LEDs, relays, and other digital components are controlled.

## Breadboarding

![Connecting Alligator Clips](/Images/cpx_clips.png)

Because the Circuit Playground Express has large exposed pads, external components are often connected using alligator clips instead of a traditional breadboard. One clip usually connects a component to a power pin or ground, while another connects it to a digital I/O pin.

It is important to ensure that clips do not touch each other accidentally, as this can cause short circuits.

## Example

```python
# Import libraries
import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up digital pin
led = digitalio.DigitalInOut(board.D10)

# Change pin to be digital output
my_pin.switch_to_output()

# Main loop
while True:
    # Turn pin on when A is pressed
    if cp.button_a:
        led.value = True

    # Turn pin off when B is pressed
    if cp.button_b:
        led.value = False
```

In this example, a digital pin is used to control an external LED. When button A on the Circuit Playground Express is pressed, the pin outputs voltage and turns the LED on. When button B is pressed, the voltage is turned off and the LED turns off. This demonstrates how physical input on the board can control external hardware using digital output.

# Additional Documentation

* [Pin Details](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
* [Pins and Modules](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-pins-and-modules)
* [Digital in and out](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-digital-in-out)
* [DigitalIO API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/)
