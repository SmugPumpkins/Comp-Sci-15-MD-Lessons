# Overview

Analog input allows the Circuit Playground Express to **measure a range of values**, rather than just detecting on or off states. This makes it possible to read sensors like potentiometers, light sensors, flex sensors, and other components that produce varying voltages. In this lesson, you will learn which pins support analog input, how analog input works, how to wire analog sensors correctly, and how to read analog values using CircuitPython.

# Important Information

## Pin Details

![Pinout Diagram](https://cdn-learn.adafruit.com/assets/assets/000/139/941/large1024/makecode_circuit_playground_Adafruit_Circuit_Playground_Express_Pinout_2.png?1758740487)

Analog input pins measure **voltage levels** between 0 V and 3.3 V and convert them into numbers that your program can use. These values are continuous, meaning they can represent many possible states rather than just two.

### Power Pins

![Power pins](https://cdn-learn.adafruit.com/assets/assets/000/047/194/large1024/circuit_playground_powerpads.jpg?1507835537)

Power pins are commonly used when working with analog sensors.

* `GND` – Ground reference for voltage measurements.
* `3.3V` – Supplies power to analog sensors.
* `VOUT` – Board supply voltage, not typically used for analog input circuits.

All analog input readings are measured **relative to ground**.

### Analog Input Pins

![IO Pins](https://cdn-learn.adafruit.com/assets/assets/000/047/195/large1024/circuit_playground_iopads.jpg?1507836994)

The following pins can be used as analog inputs:

* `A0` / `D12` – This pin can output true analog signals and is commonly used for audio. It can also act as digital or analog I/O, but using it this way interferes with the built-in speaker. This pin cannot be used for capacitive touch.
* `A1` / `D6` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A2` / `D9` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A3` / `D10` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A4` / `D3` – Can be digital input or output, supports analog input, PWM, capacitive touch, and I2C SCL.
* `A5` / `D2` – Can be digital input or output, supports analog input, PWM, capacitive touch, and I2C SDA.
* `A6` / `D0` – Can be digital input or output, supports analog input, PWM, capacitive touch, and serial receive.
* `A7` / `D1` – Can be digital input or output, supports analog input, PWM, capacitive touch, and serial transmit.

In this lesson, these pins are used strictly for **reading analog values**.

## Importing Libraries

To read analog input values, the following libraries are required.

```python
import time
import board
import analogio
```

The `board` library gives access to physical pins. The `analogio` library allows pins to be configured as analog inputs. The `time` library is useful for slowing the program down so values can be observed clearly.

## Reading Analog Values

### What Analog Input Measures

Analog input reads a **voltage level** between 0 V and 3.3 V and converts it into a number. This number represents how strong the signal is.

On the Circuit Playground Express:

* `0` represents 0 V
* `65535` represents 3.3 V

Values in between represent proportional voltages.

### Creating an `AnalogIn` Pin

To read analog values, a pin must be created as an `AnalogIn` object.

```python
sensor = analogio.AnalogIn(board.A1)
```

This configures pin A1 to measure voltage instead of sending it.

### Reading the Value

Once the pin is set up, its value can be read using the `value` property.

```python
reading = sensor.value
print(reading)
```

This number changes as the voltage on the pin changes.

### Converting to Voltage (Optional)

If you want the actual voltage instead of a raw number, it can be calculated.

```python
voltage = sensor.value * 3.3 / 65535
```

This step is optional. Most programs work directly with the raw analog value.

## Breadboarding

Analog input wiring must be done carefully to produce meaningful readings.

A typical analog input circuit includes:

* One wire from the analog input pin to the sensor’s output
* One wire from the sensor to `GND`
* One wire from the sensor to `3.3V` (if the sensor requires power)

Many analog sensors work as **voltage dividers**, meaning they output a voltage somewhere between 0 V and 3.3 V based on their state. For example:

* A potentiometer changes voltage as it is turned
* A light sensor changes voltage based on brightness

The analog input pin must **never** be connected directly to voltages higher than 3.3 V, as this can permanently damage the board.

## Example

```python
# Import libraries
import time
import board
import analogio

# Set up analog input pin
sensor = analogio.AnalogIn(board.A1)

# Main loop
while True:
    value = sensor.value
    print(value)
    time.sleep(0.1)
```

In this example, the program continuously reads the voltage level on pin A1 and prints the result. As the connected sensor changes, the printed value updates in real time. This demonstrates how analog input allows the Circuit Playground Express to sense gradual changes rather than just on and off states.

# Additional Documentation

* [Pin Details](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
* [Pins and Modules](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-pins-and-modules)
* [Analog Input Guide](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-analog-input)
* [AnalogIn API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/analogio/)
