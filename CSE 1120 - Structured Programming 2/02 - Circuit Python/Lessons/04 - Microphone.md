# Overview

The Circuit Playground Express includes a built-in microphone that can be used to measure how loud the surrounding environment is. Unlike simple digital sensors, microphones produce continuous audio data that must be sampled and processed before it becomes useful. In this lesson, we focus on **measuring volume**, not recording or playing sound.

# Important Information

Working with sound on the Circuit Playground Express involves three main steps: recording raw audio samples from the microphone, storing those samples efficiently, and converting them into a single value that represents volume.

It is located by the little ear icon.

![Microphone](https://cdn-learn.adafruit.com/assets/assets/000/057/738/medium640/makecode_circuit_playground_mic.jpg?1532013732)

## Importing Libraries

Several libraries are required to work with audio input and basic math.

```python
import array
import math
import time
import audiobusio
import board
```

The `array` module is used to store numeric data efficiently in memory. 
The `math` module provides mathematical operations that are not built into Python by default. 
The `time` module is used to slow the program down so values can be read clearly. 
The `audiobusio` module allows access to digital audio hardware such as microphones. 
The `board` module provides access to the physical pins on the Circuit Playground Express.

## Creating a `PDMIn` Object

The microphone on the Circuit Playground Express is a **PDM microphone**, which outputs a digital audio signal. To use it, we must create a `PDMIn` object that tells CircuitPython how to communicate with the microphone.

```python
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)
```

* The first two arguments specify which pins are used for the microphone’s clock and data signals. 
    * These are built into the board, so we use `board.MICROPHONE_CLOCK` and `board.MICROPHONE_DATA`.
* `sample_rate` defines how many audio samples are captured per second. 
    * A value of `16000` means the microphone is sampled 16,000 times each second. 
    * Higher sample rates give more detail but require more processing.
* `bit_depth` defines how precise each sample is. 
    * A value of `16` means each sample is stored as a 16-bit number. 
    * Higher bit depth allows for more precise measurements of sound intensity.

## Storing Samples

Audio data is captured as many individual samples. To keep memory usage predictable and efficient, we store these samples in a fixed-size array instead of a regular Python list.

```python
samples = array.array('H', [0] * 160)
```

This creates space for exactly 160 unsigned 16-bit values. 
* The `'H'` type indicates that each value is an unsigned short integer. Using a fixed-size array ensures that memory usage stays constant and avoids creating new objects every time audio is recorded.
* The number `160` controls how many samples are collected at once. More samples provide smoother results but take longer to process.

## Recording Samples

Once the microphone and storage array are ready, audio data can be recorded.

```python
mic.record(samples, len(samples))
```

This line tells the microphone to fill the `samples` array with audio data. The microphone captures sound for a short moment and writes the raw sample values directly into the array. Each value represents how strong the sound signal was at a specific instant in time.

The `len(samples)` argument ensures that the microphone records exactly as many samples as the array can hold.

## Detecting Volume

Raw audio samples are not useful on their own because they constantly fluctuate above and below a center value. To measure volume, we need a way to summarize how much the signal changes overall.

```python
def sound_level(samples):
    mean = sum(samples) / len(samples)
    total = 0
    for sample in samples:
        total += (sample - mean) ** 2
    return math.sqrt(total / len(samples))
```
The above math is complex and honestly, I don't understand it. It's explained [here](https://en.wikipedia.org/wiki/Root_mean_square).

However, we get a magnitude that increases as the sound gets louder. While the math behind this is advanced, the important idea is that this function turns raw audio data into a usable volume level.

## Example

The following example shows how all of these pieces fit together to continuously measure sound volume.

```python
# Import libraries
import array
import math
import time
import audiobusio
import board

# Sound level helper function
def sound_level(samples):
    mean = sum(samples) / len(samples)
    total = 0
    for sample in samples:
        total += (sample - mean) ** 2
    return math.sqrt(total / len(samples))

# Create PDMIn (microphone)
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# Create array to store samples
samples = array.array('H', [0] * 160)

# Main loop
while True:
    # Record samples from mic
    mic.record(samples, len(samples))
    # Get sound level
    magnitude = sound_level(samples)
    print(magnitude)
    # Delay to allow for processing without cutting anything off
    time.sleep(0.1)
```

In this program, the microphone repeatedly records small chunks of sound. Each chunk is converted into a single volume value and printed to the console. As sounds get louder or quieter, the printed number changes, allowing the microphone to be used as a basic volume sensor.

# Additional Documentation

* [Adafruit Tutorial](https://learn.adafruit.com/make-it-sense/circuitpython-3)
* [AudiobusIO API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/audiobusio/)
