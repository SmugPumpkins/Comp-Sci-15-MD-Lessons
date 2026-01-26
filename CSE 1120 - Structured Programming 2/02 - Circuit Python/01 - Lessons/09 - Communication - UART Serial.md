# Overview

UART communication allows the Circuit Playground Express to **send and receive text data** with another device using two wires. UART stands for *Universal Asynchronous Receiver/Transmitter*. It is one of the simplest and most common ways for microcontrollers to communicate with computers, sensors, and other boards. In this lesson, you will learn what UART is, how it works at a high level, which pins are used, how to wire a UART connection, and how to send and receive data using CircuitPython.

# Important Information

## What UART Is (Conceptually)

UART is a **serial communication protocol**, meaning data is sent **one bit at a time**, in order, rather than all at once.

UART communication has three important characteristics:

* It is **asynchronous** (no shared clock wire)
* It uses **separate send and receive wires**
* Both devices must agree on the **speed** of communication

UART is commonly used for:

* Debug output
* Communication between boards
* Talking to GPS modules, Bluetooth modules, and serial devices

## Pin Details

![Pinout Diagram](https://cdn-learn.adafruit.com/assets/assets/000/139/941/large1024/makecode_circuit_playground_Adafruit_Circuit_Playground_Express_Pinout_2.png?1758740487)

UART uses **two specific pins** on the Circuit Playground Express.

### UART Pins

* **A6 / D0** – UART RX (Receive)
* **A7 / D1** – UART TX (Transmit)

RX receives data *into* the board.
TX sends data *out* of the board.

These pins are fixed for hardware UART on the Circuit Playground Express.

## How UART Wiring Works

UART requires at least **three connections**:

1. **TX → RX**
   The transmitting pin of one device must connect to the receiving pin of the other.
2. **RX → TX**
   Communication goes both ways.
3. **GND → GND**
   Both devices must share a common ground.

This is called a **crossed connection**:

* TX connects to RX
* RX connects to TX

UART does **not** use `3.3V` as a data line. Power may be supplied separately if needed, but data always travels on TX and RX.

## Importing Libraries

UART communication in CircuitPython uses the `busio` library.

```python
import time
import board
import busio
```

The `board` library provides access to the UART pins. The `busio` library provides the `UART` class used to send and receive serial data. The `time` library is useful for pacing communication.

## Creating a `UART` Object

To use UART, a `UART` object must be created.

```python
uart = busio.UART(
    board.TX,
    board.RX,
    baudrate=9600
)
```

The first argument is the transmit pin. The second argument is the receive pin. The `baudrate` defines the communication speed in bits per second.

A baud rate of `9600` is very common and is a good default. Both devices **must use the same baud rate**, or the data will be unreadable.

## Sending Data Over UART

UART sends **bytes**, not numbers or strings directly. Text must be converted to bytes before sending.

```python
uart.write(b"Hello\n")
```

The `b` before the string indicates that this is a **bytes object**. The newline character (`\n`) is often included so the receiving side knows when a message ends.

Anything sent with `write()` goes out through the TX pin.

## Receiving Data Over UART

To receive data, the program checks if any bytes are available and then reads them.

```python
data = uart.read()
```

If no data is available, `read()` returns `None`. If data is available, it returns a bytes object.

To safely handle this, code usually checks before using the data.

```python
data = uart.read()
if data:
    print(data)
```

The received bytes can be converted into text if needed.

```python
text = data.decode("utf-8")
```

## Breadboarding

When wiring UART:

* Connect **TX on one device to RX on the other**
* Connect **RX on one device to TX on the other**
* Always connect **GND to GND**

UART signals on the Circuit Playground Express use **3.3V logic**. Connecting to devices that use higher voltages can damage the board.

Wires should be kept short and secure. Loose connections can cause corrupted or missing data.

## Example (UART Echo)

```python
# Import libraries
import time
import board
import busio

# Create UART object
uart = busio.UART(board.TX, board.RX, baudrate=9600)

# Main loop
while True:
    # Read incoming data
    data = uart.read()
    if data:
        print(data)
        # Send the same data back
        uart.write(data)

    time.sleep(0.1)
```

In this example, the Circuit Playground Express listens for incoming UART data. When data is received, it prints it and sends the same data back. This is called an **echo** and is commonly used to test whether UART communication is working correctly.

## What UART Is Good For (At This Level)

At an introductory level, UART is best used for:

* Sending simple text messages
* Debugging communication between boards
* Triggering actions based on received commands

UART is **not** used for high-speed data, networking, or complex protocols. Its strength is simplicity and reliability.

# Additional Documentation

* [Pin Details](https://learn.adafruit.com/adafruit-circuit-playground-express/pinouts)
* [Pins and Modules](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-pins-and-modules)
* [UART Guide](https://learn.adafruit.com/circuitpython-essentials/circuitpython-uart-serial)
* [BusIO API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/busio/)
