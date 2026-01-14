# Overview

The Circuit Playground Express includes multiple exposed pins that can be used to **read digital input** from external components such as buttons, switches, and sensors. Digital input pins allow the board to detect simple on-or-off states. In this lesson, you will learn how digital input works, how to wire external inputs correctly, and how to read their values using CircuitPython.

# Important Information

## Pin Details

![Pinout Diagram](https://cdn-learn.adafruit.com/assets/assets/000/139/941/large1024/makecode_circuit_playground_Adafruit_Circuit_Playground_Express_Pinout_2.png?1758740487)

The Circuit Playground Express exposes its pins as large metal pads around the edge of the board. These pads can be configured in software to read signals coming *into* the board from external components.

### Power Pins

![Power pins](https://cdn-learn.adafruit.com/assets/assets/000/047/194/large1024/circuit_playground_powerpads.jpg?1507835537)

Power pins are often used when wiring digital inputs.

They are labeled as:

* `GND` – Ground. This is the reference point for digital signals.
* `3.3V` – A regulated 3.3-volt output used to provide power when needed.
* `VOUT` – The board’s input voltage, typically from USB or battery.

Most digital input circuits will use **GND** and sometimes **3.3V** depending on how the input is wired.

### Input / Output Pins

![IO Pins](https://cdn-learn.adafruit.com/assets/assets/000/047/195/large1024/circuit_playground_iopads.jpg?1507836994)

The I/O pins can be configured as digital inputs. When used this way, the board reads whether the pin is receiving voltage or not.

* `A0` / `D12` – This pin can output true analog signals and is commonly used for audio. It can also act as digital or analog I/O, but using it this way interferes with the built-in speaker. This pin cannot be used for capacitive touch.
* `A1` / `D6` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A2` / `D9` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A3` / `D10` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A4` / `D3` – Can be digital input or output, supports analog input, PWM, capacitive touch, and I2C SCL.
* `A5` / `D2` – Can be digital input or output, supports analog input, PWM, capacitive touch, and I2C SDA.
* `A6` / `D0` – Can be digital input or output, supports analog input, PWM, capacitive touch, and serial receive.
* `A7` / `D1` – Can be digital input or output, supports analog input, PWM, capacitive touch, and serial transmit.

In this lesson, these pins are used strictly as **digital inputs**.

## Importing Libraries

To read digital inputs, the following libraries are required.

```python
import time
import board
import digitalio
```

The `board` library gives access to the physical pins. The `digitalio` library allows pins to be configured and read as digital inputs. The `time` library is useful for adding small delays so input changes are easier to observe.

## Reading Digital Values

### Digital Values

Digital input pins read one of two states:

* `True` – The pin is receiving voltage (HIGH)
* `False` – The pin is not receiving voltage (LOW)

These values are boolean. There are no in-between states when reading a digital input.

### Create a `pin`

To read from a pin, it must first be created as a `DigitalInOut` object.

```python
my_pin = digitalio.DigitalInOut(board.D10)
```

This tells CircuitPython which physical pin you want to read from.

### Set `pin` to Input

Pins must be explicitly configured as inputs before they can be read.

```python
my_pin.switch_to_input()
```

Once configured as an input, the pin’s value reflects the electrical signal applied to it.

### Optional: Pull Resistors

Digital input pins can behave unpredictably if they are not connected to a known voltage. To prevent this, a **pull resistor** is often used.

```python
my_pin.switch_to_input(pull=digitalio.Pull.DOWN)
```

A pull-down resistor forces the pin to read `False` when nothing is connected. When voltage is applied, the pin reads `True`. Pull-up resistors work the opposite way.

### Reading the Value

The current state of the pin can be read using the `value` property.

```python
if my_pin.value:
    print("Pin is HIGH")
else:
    print("Pin is LOW")
```

This allows the program to react to buttons, switches, or other digital signals.

## Breadboarding

When wiring digital inputs, the most important rule is that **the pin must never be left floating**. A floating pin is not connected to ground or power and can randomly switch between `True` and `False`.

A typical digital input wiring setup includes:

* One wire from the input pin to the external component
* One wire connecting the component to **GND** or **3.3V**
* A pull-up or pull-down resistor, either built into the code or physically wired

For example, a button is often wired so that:

* Pressing the button connects the input pin to `3.3V`
* Releasing the button allows the pull-down resistor to pull the pin back to `False`

Correct wiring ensures that the input value is stable and predictable.

## Example

```python
# Import libraries
import time
import board
import digitalio
from adafruit_circuitplayground import cp

# Set up digital input pin
button = digitalio.DigitalInOut(board.D10)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# Main loop
while True:
    if button.value:
        print("External button pressed")
    time.sleep(0.1)
```

In this example, an external button is connected to pin D10. When the button is pressed, the pin reads `True` and a message is printed. When the button is not pressed, the pull-down resistor keeps the pin at `False`. This shows how the Circuit Playground Express can respond to digital input from external hardware.

# Additional Documentation

* [Pin Details](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
* [Pins and Modules](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-pins-and-modules)
* [Digital in and out](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-digital-in-out)
* [DigitalIO API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/digitalio/)
