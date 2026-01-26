# Overview

The IR Transceiver built into the Circuit Playground Express allows for simple wireless communication between boards using infrared light. Infrared (IR) is a type of light that humans cannot see, but electronic sensors can detect. IR communication requires line of sight and typically works over a distance of about 10–20 meters. By sending timed pulses of IR light, one board can transmit information and another board can receive and interpret it.

# Important Information

The Circuit Playground Express has a built-in IR transmitter (TX) and IR receiver (RX). These components are located on either side of the reset button. 

![IR Transceiver](https://cdn-learn.adafruit.com/assets/assets/000/057/858/medium640/light_circuitpython_CPX_IR_TX_RX.jpg?1532480921)

The TX LED sends infrared light, and the RX sensor detects incoming infrared pulses and converts them into electrical signals the microcontroller can process.

## Installing and Importing Libraries

Before any IR communication can work, the correct libraries must be installed and imported. CircuitPython does not include IR support by default, so we rely on Adafruit’s `adafruit_irremote` library.

### Installing the Library

The `adafruit_irremote` library must be available on the board. 
1. Download the CircuitPython library bundle [(which can be found here)](https://circuitpython.org/libraries).
2. Unzip the bundle. 
3. In the folder, open the `lib` folder.
4. Find the file called `adafruit_irremote.mpy`.
5. Copy `adafruit_irremote.mpy` into the `lib` folder of the CIRCUITPY drive.

For PyCharm to provide autocompletion for the `adafruit_irremote` library, you will need to install the following package for PyCharm.
```
adafruit-circuitpython-irremote
```

### Importing Required Modules

Once the library is installed, the script must import several modules. Each module has a specific role in IR communication.

```python
import board
import pulseio
import adafruit_irremote
```

* The `board` module gives access to the physical pins on the Circuit Playground Express. 
* The `pulseio` module allows precise control and measurement of timed pulses, which is essential for IR signals. 
* The `adafruit_irremote` module handles encoding and decoding IR pulse patterns into usable data.

## IR Communication Principles

IR communication works by turning the transmitter on and off very quickly. These on-and-off patterns are called pulses. The length of each pulse and the gaps between them represent binary data.

### Pulses and Timing

Instead of sending a steady signal, IR uses short bursts of light. A long pulse might represent a binary `1`, while a short pulse might represent a binary `0`. The receiver does not see numbers directly, it only sees how long the light was on and how long it was off.

### Encoding and Decoding

Encoding is the process of turning numbers into pulse patterns that can be sent by the IR transmitter. Decoding is the opposite process, where the receiver measures incoming pulses and converts them back into numbers. The sender and receiver must agree on the same timing rules, called a protocol, or the data will not make sense.

## Transmitting

Transmitting IR signals involves creating a pulse output on the IR TX pin, defining how binary data should be encoded, and then sending a sequence of numbers.

### Creating a `PulseOut` Object
In order to transmit signals out of the IR TX, we need to set up a `PulseOut` object using the `pulseio` library. The `PulseOut` object identifies the `pin`, the `frequency` carrier signal, and the `duty_cycle` that will be used for transmission.

* `pin` is the pin the microcontroller is using for it's IR TX module. 
    * In the case of CircuitPlayground Express, it's a built in pin we can access with `board.IR_TX`.
* `frequency` of the carrier signal is the base signal that *carries* message signals. It ensures that other infrared light does not interfere with signals.
    * In the case of CircuitPlayground Express, we use `38kHz` or `38000` Hz.
    * You don't need to understand more than we that use `38000` for this value.
* `duty_cycle` represents the ratio for how long the infrared LED is `ON` compared to `OFF`.
    * You don't need to understand more than that we use `2**15` for this value.

This code is used to create a `PulseOut` object.
```python
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
```


### Creating an `encoder`
At this point, we could manually choose how long a pulse is, but the mat for figuring that out is a lot of work. Instead, we set up an encoder with specific rules for how we want to send data.

An encoder object defines how numbers are translated into pulses. The values represent durations in microseconds (1 *millionth* of a second). This doesn't control the pulses themselves, it only sets up the rules.

For each value below, the first number represents how long the light is ON, and the second number represents how long it is OFF (for example, `[ON, OFF]`).

* `header` is a unique pulse that signifies the start of a signal.
* `one` and `zero` represent the pulse lengths for a binary `1` and `0` respectively.
* `trail` is an optional value that signifies the end of the signal. 
    * In this example it is set to `0`, but it could have a different value like `[3000, 1500]` (or any other pair of numbers).

```python
encoder = adafruit_irremote.GenericTransmit(
    header=[9000, 4500],
    one=[560, 1700],
    zero=[560, 560],
    trail=0
)
```
*Note: Changing these values changes the signal pattern, and it's important to remember that both sender and receiver must match.*

### Sending Messages
Our encoder can now transmit data using `transmit()`!

Transmit requires a `PulseOut` object and a list of data to send.
* The `PulseOut` object is the one we set up earlier and named `pulseout`.
* The list is a list of `bytes`. Different lists represent different messages.

A `byte` can be represented by a value between 0-255. Each `byte` is broken into 8 `bits` and sent as pulses.

```python
encoder.transmit(pulseout, [255, 2, 255, 0])
```

Typically when sending data, it's better to send fewer bytes. The more bytes you send, the longer the signal takes and the more likely it will be corrupted. There isn't a hard rule about how many bytes you can send, but it is limited by the receiver's memory.

Here is a break down of how long a signal might take to send and how likely it is to succeed:

|# of bytes|Approximate Time|Likely to Succeed|
|-|-|-|
|1-4 bytes|~60 ms|Extremely likely to succeed|
|5-16 bytes|~240 ms|Very likely to succeed|
|17-32 bytes|~0.5 seconds|Unlikely to succeed|
|33-64 bytes|~1 second|Very unlikely to succeed|
|65+ bytes|1+ seconds|Extremely unlikely to succeed|

For reference, a typical TV remote sends 2 bytes of data.

## Receiving

Receiving IR signals requires listening for pulses on the IR RX pin and decoding them back into numbers.

### Creating a `PulseIn` Object

The receiver uses a `PulseIn` to record how long the signal is high or low. To create a `PulseIn` we need to define a `pin`, a `maxlen` and an `idle_state`.
* `pin` is the pin the microcontroller is using for it's IR RX module. 
    * In the case of CircuitPlayground Express, it's a built in pin we can access with `board.IR_RX`.
* `maxlen` is the maximum number of pulses that can be remembered by the `PulseIn` object. 
    * If it receives more than the maximum number of pulses, it will not be able to decode the message.
    * You don't need to understand more than we that use `120` for this value.
* `idle_state`is the `boolean` state the `PulseIn` object starts with. The first recorded pulse it receives will be the opposite of its idle state.
    * You don't need to understand more than we that use `True` for this value.

This code is used to create a `PulseIn` object.
```python
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
```

### Creating a `decoder` Object

A decoder object converts pulse timings into binary data. Unlike the encoder, there is no estra configuration to get it working.

```python
decoder = adafruit_irremote.GenericDecode()
```

The decoder reads pulses and attempts to match them to the expected protocol. If the timing does not match, an error is raised.

### Receiving Messages

Receiving messages has 2 steps:
1. Read the pulses.
2. Decode the pulses into a list of numbers.

This code needs to come first and reads the actual pulses from the `PulseIn` object.
```python
pulses = decoder.read_pulses(pulsein)
```

Once you have received the pulses, they can be decoded back into a list of `bytes`. However, there is a chance there is no message to be decoded, or the message may be incomplete. This section should always be placed in a `try` / `except` block
```python
try:
    message = decoder.decode_bits(pulses)
except adafruit_irremote.IRDecodeException:
    continue
```

The received list can be compared to known messages. If it matches a specific pattern, the program can respond with lights, sounds, or other actions.

## Transmitter and Receiver Example
### Transmitter
```python
# Import libraries
import board
import pulseio
import adafruit_irremote
from adafruit_circuitplayground import cp
import time

# Create PulseOut object
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)

# Create an encoder
encoder = adafruit_irremote.GenericTransmit(
    header=[9000, 4500],
    one=[560, 1700],
    zero=[560, 560],
    trail=0
)

# Define some messages
message_a = [255, 1, 255, 1]
message_b = [1, 255, 1, 255]
message_both = [127, 1, 127, 255]
message_neither = [1, 127, 255, 127]

# Main loop
while True:

    # Button logic
    if cp.button_a and not cp.button_b:
        encoder.transmit(pulseout, message_a) # Send message
    elif cp.button_b and not cp.button_a:
        encoder.transmit(pulseout, message_b) # Send message
    elif c.button_a and cp.button_b:
        encoder.transmit(pulseout, message_both) # Send message
    else:
        encoder.transmit(pulseout, message_neither) # Send message
    
    # Delay at end of loop so message doesn't get cut off
    time.sleep(0.2) 
```
### Receiver
```python
# Import libraries
import board
import pulseio
import adafruit_irremote

# Create PulseIn object
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)

# Create decoder object
decoder = adafruit_irremote.GenericDecode()

# Define some messages
message_a = [255, 1, 255, 1]
message_b = [1, 255, 1, 255]
message_both = [127, 1, 127, 255]
message_neither = [1, 127, 255, 127]

while True:
    # Read the pulses
    pulses = decoder.read_pulses(pulsein)

    # In case there would be an error we use a try / except block
    try:
        message = decoder.decode_bits(pulses)
    except adafruit_irremote.IRDecodeException:
        continue

    # Print logic
    if message == message_a:
        print("A button pressed!")
    elif message == message_b:
        print("B button pressed!")
    elif message == message_both:
        print("Both buttons pressed!")
    elif message == message_neither:
        print("Neither button pressed!")
```
## Transceiving

A single Circuit Playground Express can both send and receive IR signals within the same program. This is called transceiving.

### Using TX and RX Together

The TX and RX components are independent, so creating both a `PulseOut` and a `PulseIn` in the same script is allowed. The program can decide when to send and when to listen.

```python
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
```

### Switching Between Sending and Receiving

A common approach is to send signals based on input, such as a button press, and continuously check for incoming signals the rest of the time. As long as the program avoids transmitting and decoding at the exact same moment, a single board can successfully communicate in both directions.


## Transceiving

A single Circuit Playground Express can **both transmit and receive IR signals in the same script**. This is called **transceiving**. While the hardware supports this, it requires careful control over *when* the board is listening and *when* it is sending.

Unlike higher-level wireless systems, IR has no automatic coordination. If the board tries to transmit while it is also actively listening, pulses can be missed, corrupted, or misinterpreted.

### Using TX and RX Together

Because the IR transmitter (TX) and receiver (RX) are separate hardware components, it is valid to create both a `PulseOut` and a `PulseIn` in the same program.

```python
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()
encoder = adafruit_irremote.GenericTransmit(
    header=[9000, 4500],
    one=[560, 1700],
    zero=[560, 560],
    trail=0
)
```

At this point, the board is *capable* of sending and receiving, but it should **not do both at the same time**.

### Pausing the Receiver Before Transmitting

Before calling `encoder.transmit()`, the receiver should be paused.

```python
pulsein.pause()
encoder.transmit(pulseout, [255, 2, 255, 0])
```

Pausing tells the board to temporarily stop recording pulses. This keeps the pulse buffer clean and prevents self-interference.

### Resuming the Receiver After Transmitting

Once transmission is complete, the receiver should be resumed so it can listen again.

```python
pulsein.resume()
```

After resuming, the board can safely wait for incoming messages.

### Typical Transceiving Flow

A common and safe pattern for transceiving follows this sequence:

1. Listen for incoming messages
2. Decide whether to respond
3. Pause the receiver
4. Transmit a message
5. Resume the receiver

This ensures that sending and receiving never overlap.

### Example Transceiving Logic

```python
while True:
    # Listen for a message
    pulses = decoder.read_pulses(pulsein)
    try:
        message = decoder.decode_bits(pulses)
    except adafruit_irremote.IRDecodeException:
        continue

    # Decide to respond
    if message == [1, 2, 3, 4]:
        pulsein.pause()
        encoder.transmit(pulseout, [9, 9, 9, 9])
        pulsein.resume()
```

In this example:

* The board listens first
* Only transmits after a valid message is received
* Pauses and resumes the receiver to protect signal integrity

# Additional Documentation
* [PulseIO API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/pulseio/#)
* [Adafruit IR Remote API Reference](https://docs.circuitpython.org/projects/irremote/en/latest/api.html#)
