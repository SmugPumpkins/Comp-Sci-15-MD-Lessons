# Overview

The Circuit Playground Express can act as a **USB Human Interface Device (HID)** when connected to a computer. This means it can pretend to be a **keyboard**, a **mouse**, or both at the same time. Instead of just sending data to the computer, the board can *control* the computer by typing keys, moving the mouse, or clicking buttons. In this lesson, you will learn what HID is, how it works at a high level, how CircuitPython enables HID, and how to send keyboard and mouse actions safely and intentionally.

# Important Information

## What HID Is (Conceptually)

HID stands for **Human Interface Device**. It is a standard USB device type used for things like:

* Keyboards
* Mice
* Game controllers

When a device identifies itself as an HID, the computer automatically trusts it to send input events. No drivers are required. This is why keyboards and mice work immediately when plugged in.

When the Circuit Playground Express runs HID code, the computer treats it **as if it were a real keyboard or mouse**.

## Important Safety Note

Because HID code can send keystrokes and mouse movements:

* A program can take control of the computer
* Mistakes can cause rapid typing or mouse movement
* Bad logic can make the computer hard to use temporarily

For this reason, HID programs should:

* Be simple
* Include delays
* Only send input when explicitly triggered (such as by a button press)

If needed, unplugging the board immediately stops all HID behavior.

## Importing Libraries

HID functionality uses the `usb_hid` module along with specific device libraries.

```python
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode
```

The `usb_hid` module provides access to the USB HID interface. The `Keyboard` and `Mouse` classes represent HID devices. The `Keycode` class provides readable names for keyboard keys.

## Creating HID Devices

Before sending any input, HID device objects must be created.

### Creating a Keyboard

```python
keyboard = Keyboard(usb_hid.devices)
```

This creates a virtual keyboard connected to the computer.

### Creating a Mouse

```python
mouse = Mouse(usb_hid.devices)
```

This creates a virtual mouse connected to the computer.

Both devices can exist at the same time.

## Keyboard Input

### Sending a Key Press

Keyboard input is sent using **keycodes**, not characters.

```python
keyboard.press(Keycode.A)
keyboard.release(Keycode.A)
```

This presses and releases the `A` key. Releasing keys is required so they do not remain “held down”.

### Typing Text

To type text, keys are pressed and released automatically.

```python
keyboard.send(Keycode.H, Keycode.E, Keycode.L, Keycode.L, Keycode.O)
```

Each keycode represents a physical key on the keyboard.

### Modifier Keys

Modifier keys like Shift, Control, and Alt can be combined with other keys.

```python
keyboard.send(Keycode.CONTROL, Keycode.C)
```

This sends **Ctrl+C**, which is commonly used for copy.

## Mouse Input

### Moving the Mouse

Mouse movement is relative, not absolute.

```python
mouse.move(x=10, y=0)
```

This moves the mouse 10 units to the right.

### Mouse Buttons

Mouse buttons can be pressed and released.

```python
mouse.press(Mouse.LEFT_BUTTON)
mouse.release(Mouse.LEFT_BUTTON)
```

This performs a left-click.

### Scrolling

```python
mouse.move(wheel=1)
```

This scrolls the mouse wheel.

## Using Onboard Buttons as Triggers

HID actions should only happen in response to clear input. The Circuit Playground Express buttons are ideal for this.

```python
from adafruit_circuitplayground import cp
```

This allows button presses to trigger keyboard or mouse actions safely.

## Example: Keyboard Input

```python
# Import libraries
import time
import usb_hid
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Create keyboard
keyboard = Keyboard(usb_hid.devices)

while True:
    if cp.button_a:
        keyboard.send(Keycode.H, Keycode.I)
        time.sleep(0.5)
```

In this example, pressing button A types “HI” on the connected computer.

## Example: Keyboard and Mouse Together

```python
# Import libraries
import time
import usb_hid
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode

# Create HID devices
keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)

while True:
    if cp.button_a:
        keyboard.send(Keycode.SPACE)
        time.sleep(0.5)

    if cp.button_b:
        mouse.move(x=20)
        time.sleep(0.5)
```

In this example:

* Button A presses the space bar
* Button B moves the mouse to the right

## Best Practices for HID Programs

HID programs should always:

* Use delays to prevent rapid repeated input
* Require a physical trigger like a button
* Avoid infinite loops that send input continuously
* Be tested carefully

HID is powerful, but that power should be used intentionally and responsibly.

# Additional Documentation

* [Keyboard](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-hid-keyboard)
* [Keyboard and Mouse](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-hid-keyboard-and-mouse)
* [Keyboard API Reference](https://docs.circuitpython.org/projects/hid/en/latest/api.html#keyboard)
* [Mouse API Reference](https://docs.circuitpython.org/projects/hid/en/latest/api.html#mouse)
* [Keycode API Reference](https://docs.circuitpython.org/projects/hid/en/latest/api.html#keycode)
* [usb_hid API Reference](https://docs.circuitpython.org/en/latest/shared-bindings/usb_hid/)
