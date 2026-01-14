# Overview

Analog output allows the Circuit Playground Express to send **varying voltage levels**, not just fully on or fully off signals. This makes it possible to control things like brightness, speed, and sound smoothly instead of in steps. In this lesson, you will learn which pins support analog output, how analog output works on the Circuit Playground Express, and how to write analog values using CircuitPython.

# Important Information

## Pin Details

![Pinout Diagram](https://cdn-learn.adafruit.com/assets/assets/000/139/941/large1024/makecode_circuit_playground_Adafruit_Circuit_Playground_Express_Pinout_2.png?1758740487)

The Circuit Playground Express does **not** have true analog voltage output on most pins. Instead, it uses a technique called **PWM (Pulse Width Modulation)** to simulate analog output. One pin, however, is special.

### Power Pins

![Power pins](https://cdn-learn.adafruit.com/assets/assets/000/047/194/large1024/circuit_playground_powerpads.jpg?1507835537)

Power pins are often used alongside analog output pins.

* `GND` – Ground reference for the circuit.
* `3.3V` – Maximum voltage level that analog output can simulate.
* `VOUT` – Board supply voltage, not typically used for analog control.

Analog output signals always operate **relative to ground**.

### Output Pins (Analog Capable)

![IO Pins](https://cdn-learn.adafruit.com/assets/assets/000/047/195/large1024/circuit_playground_iopads.jpg?1507836994)

Analog output is available in two different forms:

* **True analog output**

  * **`A0` / `D12`** – This pin can produce a real analog voltage using a DAC (Digital-to-Analog Converter).
  * Commonly used for audio output.
  * Using this pin for analog output interferes with the built-in speaker.

* **PWM-based analog output**

* `A1` / `D6` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A2` / `D9` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A3` / `D10` – Can be digital input or output, supports analog input, PWM, and capacitive touch.
* `A4` / `D3` – Can be digital input or output, supports analog input, PWM, capacitive touch, and I2C SCL.
* `A5` / `D2` – Can be digital input or output, supports analog input, PWM, capacitive touch, and I2C SDA.
* `A6` / `D0` – Can be digital input or output, supports analog input, PWM, capacitive touch, and serial receive.
* `A7` / `D1` – Can be digital input or output, supports analog input, PWM, capacitive touch, and serial transmit.

These pins simulate analog output using PWM.

## Importing Libraries

To write analog values, the following libraries are required.

```python
import time
import board
import analogio
import pwmio
```

The `analogio` library is used for **true analog output** via the DAC. The `pwmio` library is used for **PWM-based analog output**. The `board` module provides access to the physical pins, and `time` is used for timing and delays.

## Understanding Analog Output

### What “Analog” Means

An analog value represents a **range**, not just two states. Instead of only `ON` or `OFF`, analog output can represent values like:

* dim → medium → bright
* slow → medium → fast
* quiet → loud

On the Circuit Playground Express, analog output always ranges between **0 volts and 3.3 volts**.

### True Analog vs PWM

* **True analog (DAC)** produces a steady voltage.
* **PWM analog** rapidly turns a pin on and off, changing how long it stays on during each cycle.

To most components (LEDs, motors), PWM behaves like real analog voltage.

## Writing True Analog Output (DAC)

True analog output is done using the `analogio.AnalogOut` class and is only available on pin A0 / D12.

### Creating an `AnalogOut` Object

```python
dac = analogio.AnalogOut(board.A0)
```

This configures pin A0 to output a true analog voltage.

### Writing an Analog Value

```python
dac.value = 32768
```

The value range is:

* `0` → 0 volts
* `65535` → 3.3 volts

Any value in between produces a proportional voltage.

## Writing PWM-Based Analog Output

Most analog output on the Circuit Playground Express uses PWM.

### Creating a `PWMOut` Object

```python
pwm = pwmio.PWMOut(board.D10, frequency=5000, duty_cycle=0)
```

* `frequency` controls how fast the pin switches on and off.
* `duty_cycle` controls how strong the output appears.

### Writing a PWM Value

```python
pwm.duty_cycle = 32768
```

The duty cycle range is:

* `0` → always off
* `65535` → always on

Values in between simulate analog levels.

## Breadboarding

When using analog output, wiring is similar to digital output but with added care.

Typical wiring includes:

* One wire from the analog output pin to the component
* One wire from the component to `GND`
* A current-limiting resistor when using LEDs

For PWM output, many components work without extra filtering. For true analog output (DAC), components like speakers or amplifiers are commonly used.

Never connect analog output pins directly to `3.3V` or `VOUT`.

## Example (PWM Analog Output)

```python
# Import libraries
import time
import board
import pwmio

# Set up PWM pin
led = pwmio.PWMOut(board.D10, frequency=5000, duty_cycle=0)

# Main loop
while True:
    # Fade LED up
    for value in range(0, 65536, 1024):
        led.duty_cycle = value
        time.sleep(0.01)

    # Fade LED down
    for value in range(65535, -1, -1024):
        led.duty_cycle = value
        time.sleep(0.01)
```

In this example, the LED gradually fades brighter and dimmer by changing the PWM duty cycle. This demonstrates how analog output allows smooth control instead of simple on/off behavior.

# Additional Documentation

* [Pin Details](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
* [Pins and Modules](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-pins-and-modules)
* [AnalogOut API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/analogio/)
* [PWMOut API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/pwmio/)
