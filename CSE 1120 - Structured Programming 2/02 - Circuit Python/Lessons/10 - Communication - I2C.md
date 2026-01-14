# Overview

I2C communication allows the Circuit Playground Express to **talk to multiple devices using only two shared wires**. I2C stands for *Inter-Integrated Circuit*. It is commonly used to communicate with sensors, displays, and other microcontrollers. In this lesson, you will learn what I2C is, how it works at a high level, which pins are used on the Circuit Playground Express, how I2C devices are wired, and how to communicate with them using CircuitPython.

# Important Information

## What I2C Is (Conceptually)

I2C is a **shared-bus communication protocol**. Instead of having a separate set of wires for every device, many devices can all connect to the same two data lines.

I2C has three key ideas:

* Devices share the same bus
* Each device has a unique **address**
* One device controls the conversation at a time

The Circuit Playground Express always acts as the **controller** (sometimes called the master). Sensors and other peripherals act as **devices** (sometimes called slaves).

## Pin Details

![Pinout Diagram](https://cdn-learn.adafruit.com/assets/assets/000/139/941/large1024/makecode_circuit_playground_Adafruit_Circuit_Playground_Express_Pinout_2.png?1758740487)

I2C communication uses two specific pins that are shared by all I2C devices.

### I2C Pins

* **A4 / D3** – I2C SCL (Clock)
* **A5 / D2** – I2C SDA (Data)

The clock line controls *when* bits are sent.
The data line carries the actual data.

These pins are fixed for I2C on the Circuit Playground Express.

## How I2C Wiring Works

I2C always uses the same basic connections:

1. **SCL → SCL**
   All devices share the same clock line.
2. **SDA → SDA**
   All devices share the same data line.
3. **GND → GND**
   All devices must share a common ground.
4. **Power (3.3V)**
   Most I2C devices need power from the board.

Unlike UART:

* Devices are **not crossed**
* All SDA pins connect together
* All SCL pins connect together

Multiple devices can be connected at the same time as long as each one has a unique I2C address.

## Importing Libraries

I2C communication in CircuitPython uses the `busio` library.

```python
import time
import board
import busio
```

The `board` library provides access to the I2C pins. The `busio` library provides the `I2C` class used to control the bus. The `time` library is often used to slow down communication for readability.

## Creating an `I2C` Object

Before using I2C, an `I2C` object must be created.

```python
i2c = busio.I2C(board.SCL, board.SDA)
```

This tells CircuitPython to use the built-in I2C clock and data pins. Only **one** I2C object should exist in a program.

## Locking the I2C Bus

I2C is a shared resource. Before using it, the program must make sure the bus is available.

```python
while not i2c.try_lock():
    pass
```

This waits until the Circuit Playground Express has exclusive access to the bus. When finished, the bus should be unlocked.

```python
i2c.unlock()
```

## Scanning for I2C Devices

Each I2C device has a numeric address. Before communicating, it is common to scan the bus to see what devices are connected.

```python
devices = i2c.scan()
print(devices)
```

This returns a list of addresses for all connected I2C devices. Addresses are usually shown in decimal but are often written in hexadecimal in documentation.

## Communicating With I2C Devices

I2C communication happens in short messages. The controller writes data to a device or reads data from it using the device’s address.

### Writing Data

```python
i2c.writeto(0x40, bytes([0x01, 0x02]))
```

This sends two bytes of data to the device with address `0x40`.

### Reading Data

```python
result = bytearray(2)
i2c.readfrom_into(0x40, result)
```

This reads two bytes of data from the device and stores them in `result`.

Most of the time, you will not write this low-level code yourself. Sensor libraries handle these details internally.

## Breadboarding

When wiring I2C devices:

* All **SDA pins connect together**
* All **SCL pins connect together**
* All devices share **GND**
* Devices are powered from **3.3V**

Many I2C breakout boards already include pull-up resistors on SDA and SCL. This means you usually do not need to add extra resistors.

Because I2C is a shared bus:

* Loose wires can affect all devices
* Long wires can cause communication errors
* Secure connections are important

## Example (I2C Scan)

```python
# Import libraries
import time
import board
import busio

# Create I2C object
i2c = busio.I2C(board.SCL, board.SDA)

# Wait for I2C bus
while not i2c.try_lock():
    pass

# Scan for devices
devices = i2c.scan()
print("I2C devices found:", devices)

# Unlock bus
i2c.unlock()

while True:
    time.sleep(1)
```

In this example, the Circuit Playground Express scans the I2C bus and prints the addresses of any connected devices. This is often the first step when working with a new I2C sensor.

## What I2C Is Good For (At This Level)

At an introductory level, I2C is best used for:

* Connecting sensors (temperature, motion, light, etc.)
* Using displays or LED drivers
* Communicating with breakout boards

I2C is powerful because it allows many devices to share the same two wires, making it ideal for expandable projects.

# Additional Documentation

* [Pin Details](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
* [Pins and Modules](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-pins-and-modules)
* [I2C Guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-i2c)
* [BusIO API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/busio/)
