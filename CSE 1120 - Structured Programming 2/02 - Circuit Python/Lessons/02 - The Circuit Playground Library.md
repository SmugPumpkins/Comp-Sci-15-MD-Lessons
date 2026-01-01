# Overview
The Circuit Playground Express is packed full of built in sensors and outputs. It has lights, a speaker, buttons, a switch, an accelerometer, and even a few things you might not expect like a light sensor or a thermometer. This guide will outline some of the ways we can access these built in modules using the `circuitplayground` library.

# Important Information

This lesson is going to cover *a lot* of content. Because you have been using python for a while now, hopefully most of these concepts are familiar, and the focus is just on new ways of implenting things you've already learned.

The official documentation for this library can be found here, at the [Adadruit CircuitPlayground Library API Reference](https://docs.circuitpython.org/projects/circuitplayground/en/latest/api.html#adafruit_circuitplayground.circuit_playground_base.CircuitPlaygroundBase.pixels).

## Setting Up

### Importing the Library
Before we can use the `circuitplayground` library, we need to import it. Because the name of the library is so long, we will shorten the namespace to `cp` when we import it.
```python
from adafruit_circuitplayground import cp
```
`cp` will be the prefix we use to access all of the parts of this library.

### Using a While Loop
Typically, a python program runs once and then completes. When working with inputs and outputs like on the CircuitPlayground Express, we need our code to be continuously checking for input or continuously providing output. To do this, our script will have 2 main parts.

At the top of our code we will put everything that needs to run once. Importing libraries, initializing variables, and any other set up code will run at the beginning.

At the bottom of our code, we will use a `while` loop to continuously check for inputs and provide outputs.
```python
# Set Up code
from adafruit_circuitplayground import cp
...
while True:
    # Input and output code from the CircuitPlayground Express will go here
```

## Inputs (Sensors)
The following section covers all of the input devices (sensors) that this library can use. 

There are additional sensors on the CircuitPlayground Express, like a microphone and an infrared tranciever, but this library does not contain modules for them.
### Buttons
The CircuitPlayground Express has 3 buttons on it.
#### Reset Button
The first button is the reset button. This button cannot be programmed and is only used for resetting the device or preparing it to be Bootloaded with firmware.

![Reset Buttton](https://cdn-learn.adafruit.com/assets/assets/000/076/510/medium640/educators_circuitpy_reset_button.jpg?1559761014)

The other 2 buttons *are* programmable.
#### Button A
Button A is labeled with an `A` and is on the left side of the CircuitPlayground Express.

![Button A](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/button_a.jpg)

Button A can be read with the following code:

```python
cp.button_a
```

Button A will be in one of two states. When it is pressed, `cp.button_a` is `True`. When the button is not pressed, `cp.button_a` will be `False`.

#### Button B
Button B is labeled with an `B` and is on the right side of the CircuitPlayground Express.

![Button B](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/button_b.jpg)

Button B can be read with the following code:

```python
cp.button_b
```

Button B will be in one of two states. When it is pressed, `cp.button_b` is `True`. When the button is not pressed, `cp.button_b` will be `False`.

#### Button Example
Using these values in your code might look something like this:
```python
from adafruit_circuitplayground import cp

while True:
    if cp.button_a:
        print("Button A is Pressed!")
    if cp.button_b:
        print("Button B is Pressed!")
```

### Switch
Like the buttons, the switch will be in one of two states. The switch is located in the center of the CircuitPlayground Express, between the music note and the ear.

![Switch](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/slide_switch.jpg)

The switch position can be accessed with the following code:
```python
cp.switch
```

The switch will be `True` when it is in the left position (next to the music note), and will be `False` when it is in the right position (next to the ear).

#### Switch Example
Using the switch in your code might look something like this:
```python
from adafruit_circuitplayground import cp

while True:
    if cp.switch:
        print("The switch is to the left!")
    else:
        print("The switch is to the right!")
```
### Touch
The CircuitPlayground Express has seven capacitive touch pads located around the edge of the device.

![Capacitive Touch Pads](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/capacitive_touch_pads.jpg)

Capacitive touch sensors can detect the electrical properties of your body. They are similar to buttons, but instead of detecting an open or closed circuit, they detect the electrical signals of your body.

Each capacitive touch sensor on the board has it's own value associated with it. The values correspond to the labels next to the touch pad. The values are as follows:
```python
cp.touch_A1
```
```python
cp.touch_A2
```
```python
cp.touch_A3
```
```python
cp.touch_A4
```
```python
cp.touch_A5
```
```python
cp.touch_A6
```
```python
# Note that this one is NOT A7
cp.touch_TX
```

Each capacitive touch sensor is separate from the others. When a sensor is touched, the value reads as `True`, and when it is not being touched it reads as `False`.

#### Capacitve Touch Example
Using the capacitive touch sensors in your code might look something like this:
```python
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touching A1")
    if cp.touch_A2:
        print("Touching A2")
    if cp.touch_A3:
        print("Touching A3")
    if cp.touch_A4:
        print("Touching A4")
    if cp.touch_A5:
        print("Touching A5")
    if cp.touch_A6:
        print("Touching A6")
    if cp.touch_TX:
        print("Touching TX")
```
### Light Sensor
The light sensor (also called a *photoresistor*) is  located in the top left corner of the CircuitPlayground Express and has an eye next to it.

![Light Sensor](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/light_sensor.jpg)

The light sensor is different from the other sensors we've looked at. With buttons, switches, and capacitive touch, the values were either `True` or `False`. They are either pressed or not pressed, switched on or switched off.

With the light sensor, it detects *how bright the light is*. So instead of getting a `True` or `False` value, the light sensor provides a number based on how brigt the light is. 

A lower number means less light, and a higher number means more light.

The following code will access the light sensor's value:
```python
cp.light
```

#### Light Example
In this example, the light value will print once every half second.
```python
from adafruit_circuitplayground import cp
import time

while True:
    print("Light:", cp.light)
    time.sleep(0.5)
```

### Accelerometer
An accelerometer is able to detect the rotation of the CircuitPlayground Express. It can detect rotations on the X, Y, and Z axis, which are indicated on the icon near the center of the CircuitPlayground Express.

![Accelerometer](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/accelerometer.jpg)

The accelerometer also acts differently from the light sensor, or the buttons and switches. Instead of providing a single value, it provides *three!*

The values that it provides are an X, Y, and Z rotation of the CircuitPlayground Express.
#### The Acceleration Object
Technically speaking, it provides one value in the form of an acceleraation object. This code is used to access the acceleration object:
```python
cp.acceleration
```
If we printed the acceleration, we would get an output like this:
Code:
```python
print(cp.acceleration)
```
Output:
```
acceleration(x=3.2942, y=-5.28605, z=8.1589)
```
The numbers will be different depending on the actual rotation of the CircuitPlayground Express.

On its own, the acceleration object isn't very useful. To do anything meaningful, we need to access the actual X, Y, and Z rotation values.
#### Accessing Rotation Values
There are 2 ways we can access the rotation values. 

The first way is called `dot notation`. We can access them by writing `.x`, `.y`, or `.z` on our acceleration object.
```python
from adafruit_circuitplayground import cp

while True:
    # In this example they get stored as variables, but you could also just access them directly without storing them as a variable
    x_rotation = cp.acceleration.x
    y_rotation = cp.acceleration.y
    z_rotation = cp.acceleration.z
```

The second way is by accessing their index. X is the first value, and is at index `0`, Y is at index `1`, and Z is at index `2`.
```python
from adafruit_circuitplayground import cp

while True:
    # In this example they get stored as variables, but you could also just access them directly without storing them as a variable
    x_rotation = cp.acceleration[0]
    y_rotation = cp.acceleration[1]
    z_rotation = cp.acceleration[2]
```
Generally I prefer dot notation because it is clearer what kind of value is being accessed. For me, `.x` clearly represents some kind of x value. `[0]` on the other hand is just the first index of something, and could be anything.

#### Acceleration Example
Your code might look something like this:
```python
from adafruit_circuitplayground import cp
import time

while True:
    x_rotation = cp.acceleration.x
    y_rotation = cp.acceleration.y
    z_rotation = cp.acceleration.y

    print(f"X rotation: {x_rotation}, Y rotation: {y_rotation}, Z rotation: {z_rotation}")
```
### Tap Detection
Tap detection is not actually built in to the CircuitPlayground Express and is instead a special feature added by this library! It uses the accelerometer to detect jumps in movement. If the jump is big enough for a short period of time, then it registers a tap!

![Accelerometer](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/accelerometer.jpg)

Tap detection has 2 parts. 

#### Configure Taps

First, you need to specify the number of taps that you would like to count. In this example, we will specify 1 tap, but you can do more if you would like. The number of taps can be initialized outside of your `while` loop:
```python
cp.detect_taps = 1
```
#### Detect Taps

Second, you need to check if the CircuitPlayground Express has been tapped. Like buttons, this value is either `True` or `False`. If you have tapped the devide the right number of times, the value will be `True`, otherwise it will be `False`.
```python
cp.tapped
```
*If you do not configure the taps beforehand, this value will not do anything.*
#### Tap Detection Example
Your code for tap detection might look something like this:
```python
from adafruit_circuitplayground import cp

cp.detect_taps = 1
while True:
  if cp.tapped:
    print("Single tap detected!")
```


### Shake Detection
Shake detetion uses the accelerometer to detect when the CircuitPlayground Express has been shaken.

![Accelerometer](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/accelerometer.jpg)

The shake detection provides a `True` or `False` value. If the CircuitPlayground Express is being shaken, the value is `True`, otherwise the value is `False`.

This code will allow you to access the value for shaking:
```python
cp.shake()
```

Note that the shake detection has brakets `()` at the end of it. That's because this is a method (function from the library) that returns a value rather than a variable.
#### Changing the Shake Threshold
Inside the brackets you can specify how high you want the shake threshold to be. The default value if you do not change the shake threshold is `30`.

If you want it to be *more* sensitive, you can make it a *lower* value. The minimum value is `10` which represents not being shaken at all. *If you put a value lower than `10`, the CircuitPlayground Express will continuously be detecting a shake even if it's not moving.*
```python
cp.shake(shake_threshold=15)
```

If you want it to be *less* sensitive, you can make the shake threshold a *higher* value. Remember that the default value is `30`. If you want it to need a hard shake, the number will need to be higher than `30`.
```python
cp.shake(shake_threshold=40)
```

#### Shake Example
Your shake code might look something like this:
```python
from adafruit_circuitplayground import cp

while True:
    if cp.shake(shake_threshold=25):
        print("Shake detected!")
```

### Temperature
The temperature sensor detects the temperature in degrees Celsius. It is located in the top right corner of the CircuitPlayground Express.

![Temperature Sensor](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/thermistor.jpg)

The output for the temperature sensor is a number representing the temperature in degrees Celsius. To access this value you can use the following code:
```python
cp.temperature
```

#### Temperature Example
Your temperature sensor code might look something like this:
```python
from adafruit_circuitplayground import cp
import time

while True:
    print(f"It is {cp.temperature}°C right now!")
    time.sleep(1)
```
## Outputs
This section covers some of the built in output devices on the CircuitPlayground Express. Outputs are often changed depending on the inputs received through the sensors. Everything that gets output is controlled through code.
### Built In LED
The simplest output on the CircuitPlayground Express is the built in red LED. It is located on the right side of the micro USB port.

![Built in LED](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/red_led.jpg)

The built in LED can be in one of two states, it can either be on or off. This is controlled with a boolean value. To turn it on, it must be set to `True`. To turn it off, it must be set to `False`.

The value can be assigned just like any other variable:
```python
# Turn on the LED
cp.red_led = True
```
```python
# Turn off the LED
cp.red_led = False
```
#### Ensuring the LED is Seen
One thing to be aware of is that if there is no time delay between turning it on and off, it will appear as though the state hasn't changed. 

Often you will want to create some kind of delay between it turning on or off.
```python
# On for 0.5 seconds
cp.red_led = True
time.sleep(0.5)

# Off for 0.5 seconds
cp.red_led = False
time.sleep(0.5)
```

You can also link its state to one of the input devices.
```python
# When the switch is on, the LED is on
# When the switch is off, the LED is off
cp.red_led = cp.switch
```
#### LED Example
Your code for the LED might look something like this:
```python
from adafruit_circuitplayground import cp
import time

while True:
    cp.red_led = True
    time.sleep(0.5)
    cp.red_led = False
    time.sleep(0.5)
```
### Speaker
There is a speaker built into the CircuitPlayground that can play tones or sound files. It is located in the bottom left corner and is indicated with a music note icon.
![Speaker](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/speaker.jpg)

#### Notes to Frequencies

<details>
<summary>List of Notes to Frequencies</summary>

```
B0  31
C1  33
CS1 35
D1  37
DS1 39
E1  41
F1  44
FS1 46
G1  49
GS1 52
A1  55
AS1 58
B1  62
C2  65
CS2 69
D2  73
DS2 78
E2  82
F2  87
FS2 93
G2  98
GS2 104
A2  110
AS2 117
B2  123
C3  131
CS3 139
D3  147
DS3 156
E3  165
F3  175
FS3 185
G3  196
GS3 208
A3  220
AS3 233
B3  247
C4  262
CS4 277
D4  294
DS4 311
E4  330
F4  349
FS4 370
G4  392
GS4 415
A4  440
AS4 466
B4  494
C5  523
CS5 554
D5  587
DS5 622
E5  659
F5  698
FS5 740
G5  784
GS5 831
A5  880
AS5 932
B5  988
C6  1047
CS6 1109
D6  1175
DS6 1245
E6  1319
F6  1397
FS6 1480
G6  1568
GS6 1661
A6  1760
AS6 1865
B6  1976
C7  2093
CS7 2217
D7  2349
DS7 2489
E7  2637
F7  2794
FS7 2960
G7  3136
GS7 3322
A7  3520
AS7 3729
B7  3951
C8  4186
CS8 4435
D8  4699
DS8 4978
```
</details>

#### Playing Tones with `play_tone()`
A tone is basically a note. However, instead of specifying a musical note value, we need to specify a value for the passive buzzer frequency. 

A low frequency corresponds to a low note, and a high frequency corresponds to a high note. The minimum value is `0`, and the highest value is around `5000`.


`play_tone()` is a method that has multiple parameters, but the third one is optional.
> **cp.play_tone** *(**frequency** : int, **duration** : float, **waveform** : int = 0)*
> * `frequency` is **required** and sets the pitch of the tone.
> * `duration` is **required** and sets how long the tone should play in seconds.
> * `waveform` is **optional** and tells the passive buzzer in the speaker how to play the notes.
>   * The value defaults to `0` which uses a sine wave to produce the sound.
>   * The value can also be set to `1` which uses a square wave to produce the sound. *The square wave is much louder than the sine wave.*

When playing a tone, the rest of the program pauses until the tone is finished.

#### `play_tone()` Example
The folowing examples will all produce the exact same outcome. I have this broken up into 3 different versions of the same example to hopefully help clarify the parameters of using `play_tone()`

Your code might look something like this for `play_tone()`:

```python
from adafruit_circuitplayground import cp

frequency = 500
duration_in_seconds = 1.5
waveform = 0
cp.play_tone(frequency, duration_in_seconds, waveform)
```

```python
from adafruit_circuitplayground import cp

frequency = 500
duration_in_seconds = 1.5
cp.play_tone(frequency, duration_in_seconds)
```

```python
from adafruit_circuitplayground import cp

cp.play_tone(500, 1.5)
```
#### Playing Tones with `start_tone()` and `stop_tone()`

Instead of playing a tone for a specific duration, you can tell the program to start a tone and then later stop it. Once a tone is started, it will continue until it has been stopped. *Other tones will not be able to play until it is stopped.*

The advantage that `start_tone()` and `stop_tone()` have over `play_tone()` is that the rest of the program does not pause while the tone is being played. With some creative problem solving, this allows you to create tones simultaneously with the rest of your program running.

`start_tone()` has 2 parameters, but the second one is optional..
> **cp.start_tone** *(**frequency** : int, **waveform** : int = 0)*
> * `frequency` is **required** and sets the pitch of the tone.
> * `waveform` is **optional** and tells the passive buzzer in the speaker how to play the notes.
>   * The value defaults to `0` which uses a sine wave to produce the sound.
>   * The value can also be set to `1` which uses a square wave to produce the sound. *The square wave is much louder than the sine wave.*

#### `start_tone()` and `stop_tone()` Example
The folowing examples will all produce the exact same outcome. I have this broken up into 3 different versions of the same example to hopefully help clarify the parameters of using `start_tone()`. 

*Note: These examples do still pause the program because they use* `time.sleep()`*. If you want your program to not pause, you will need to build your own creative solution for when tones should stop or start.*

Your code might look something like this for `start_tone()`:
```python
from adafruit_circuitplayground import cp
import time

frequency = 500
waveform = 0
cp.start_tone(frequency, waveform)
time.sleep(1)
cp.stop_tone()
```

```python
from adafruit_circuitplayground import cp
import time

frequency = 500
cp.start_tone(frequency)
time.sleep(1)
cp.stop_tone()
```

```python
from adafruit_circuitplayground import cp
import time

cp.start_tone(500)
time.sleep(1)
cp.stop_tone()
```

#### Playing Files with `play_file()`
The CircuitPlayground Express also has the ability to play sound files that are saved as a `.wav` file on the device itself. This is done with the `play_file()` method.

The CircuitPlayground Express has very limited storage space, and many free online sound effects download as `.mp3` files. You may need to use an online `.mp3` to `.wav` converter. You also may need to use an online `.wav` compressor.

It is also important to note, your code will be much easier to manage if you rename your sound files appropriately. There should be no spaces (use underscores `_` instead), letters should be all lowercase, and names should be short and descriptive. 

Once a `.wav` file is saved to the CircuitPlayground Express, it can be accessed with the following code:
```python
cp.play_file("your_file_name.wav")
```

Just like the `play_tone()` method, using `play_file()` will pause the rest of your code until the file is done playing.

#### `play_file()` Example
Your code for playing a sound file might look something like this:
```python
from adafruit_circuitplayground import cp

cp.play_file("your_file_name.wav")
```
### Neopixels
Neopixels are a group of lights built into the CircuitPlayground Express, and are my favourite output. Each `pixel` has an index number starting from the left of the micro USB port and continuing counter-clockwise ranging from 0-9. These index numbers are noted in the photo below. 

![Neopixels](https://docs.circuitpython.org/projects/circuitplayground/en/latest/_images/neopixel_numbering.jpg)

The Neopixels are accessed with the following code:
```python
cp.pixels
```
On it's own this code doesn't do much, so there are 3 methods we will focus on with Neopixels.
* Changing the brightness with `.brightness`
* Setting the color of *all* the Neopixels with `.fill()`
* Setting the color of *individual* Neopixels


#### Neopixel Brightness

Neopixel brightness can range from `0` to `1`. It is important to realize that Neopixels are *very* bright. 

When testing, I usually lower the brightness to `0.025` so I don't go blind. Once everything is working, I may change the brightness to something brighter, like `0.1`. The example in the official documentation sets it to `0.3`, but that's still too bright for me.

The code for changing brightness is:
```python
cp.pixels.brightness = 0.025
```
This changes the brightness for *all* Neopixels.

#### Change All Neopixels with `fill()`
The color of the Neopixel is controlled with RGB values (red, green, and blue). To change the color, you need to set all three values to a number between `0` and `255` like this:

```python
# Pure RED
# RED = 255, GREEN = 0, BLUE = 0
cp.pixels.fill((255, 0, 0))
```

Notice that the `fill()` method has 2 pairs of brackets. The outer bracket is the brackets for parameters on the `fill()` method, in this case a color. The inner brackets enclose a special data type called a `tuple` that you will learn more about next year. Both pairs of brackets are necessary for the code to work properly.

An easier solution to setting the color is saving colors as variables (or constants) and passing those values as arguments for the `fill()` method:

```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

cp.pixels.fill(GREEN)
```

To turn all the pixels off, change the fill to `(0, 0, 0)`.
```python
PIXELS_OFF = (0, 0, 0)

cp.pixels.fill(PIXELS_OFF)
```

If you aren't sure what RGB values you need to set to get a specific color, you can use an online color picker.

If you are interested, you can also look into the documentation about using hex values instead found [here](https://docs.circuitpython.org/projects/circuitplayground/en/latest/api.html#adafruit_circuitplayground.circuit_playground_base.CircuitPlaygroundBase.pixels).

#### `fill()` Example
Your code for filling all of the pixels might look something like this:
```python
from adafruit_circuitplayground import cp

ORANGE = (252, 165, 3)

cp.pixels.fill(ORANGE)
```
#### Change Individual Neopixels
Changing individual Neopixels is similar to filling them all. The difference here is that instead of using a `fill()` method, we select a pixel from its index. The image above labels each pixel with its index.

Just like with `fill()`, we use RGB values to specify the color. This code will change the pixel at index `0`:
```python
# Pure RED
# RED = 255, GREEN = 0, BLUE = 0
cp.pixels[0] = (255, 0, 0)
```

The number to specify the index can also be a variable. Using a variable would allow you to change which pixel is what color with some creative problem solving:
```python
favorite_color = (252, 3, 215)
current_pixel = 7

cp.pixels[current_pixel] = favorite_color
```
Just like with `fill()`, we can turn an individual pixel off by changing its color to `(0, 0, 0)`.
```python
PIXEL_OFF = (0, 0, 0)

cp.pixels[0] = PIXEL_OFF
```
#### Individual Neopixel Example
Your code for changing the colors of individual pixels might look something like this:
```python
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.025

RED = (255, 0, 0)
ORANGE_RED = (252, 111, 3)
ORANGE = (252, 165, 3)
YELLOW = (252, 211, 3)
GREEN_YELLOW = (194, 252, 3)
GREEN = (0, 255, 0)
GREEN_BLUE = (3, 252, 127)
LIGHT_BLUE = (3, 194, 252)
BLUE = (0, 0, 255)
PURPLE = (186, 3, 252)



while True:
    cp.pixels[0] = RED
    cp.pixels[1] = ORANGE_RED
    cp.pixels[2] = ORANGE
    cp.pixels[3] = YELLOW
    cp.pixels[4] = GREEN_YELLOW
    cp.pixels[5] = GREEN
    cp.pixels[6] = GREEN_BLUE
    cp.pixels[7] = LIGHT_BLUE
    cp.pixels[8] = BLUE
    cp.pixels[9] = PURPLE
```

