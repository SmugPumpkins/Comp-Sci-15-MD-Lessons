# Board Setup
Download the UF2 from [https://circuitpython.org/board/circuitplayground_express/] 

Plug in the board

Hit reset button 2x

Now the board shows up as a drive

Paste the UF2 file into the circuit playground drive

# PyCharm Setup

This guide is based off of [this video by Professor G](https://www.youtube.com/watch?v=Qx0twoHyH-8). It also uses the TA guide for windows from [http://bit.ly/windows-pycharm-circuitpython]

## Important Installs
Install setup tools
```
pip install setuptools
```

Install circup
```
pip install circup
```

Verify circup is installed
```
circup --version
```

Update board?
```
circup install -a
```

Download and install msys2 [https://www.msys2.org/]. This is necessary for installing Tio which allows the terminal in pycharm to display output from the circuit. DO NOT CHANGE THE INSTALL DESTINATION

Launch msys2 and paste into the msys2 terminal:
```
pacman -S tio
```
You will be asked if you want to proceed, type `y` and press `Enter`

Verify Tio installation by pasting this into the terminal:
```
tio --version
```

Update system environment variables
System Properties > Advanced > Environment Variables... > User Variables (not system variables) > PATH > Edit... > New

Paste the following into the entry box (if you installed msys2 into the default location):
```
C:\msys64\usr\bin
```
If you did NOR install msys2 in the default directory, you will instead need to Browse and find it (instead of clicking "New")

Click "`OK`" on the environment variables AND the system properties page to save the changes

To verify everything works, paste this into a regular command prompt window. It should give you a version of Tio.

```
tio --version
```
## Project Configuration
In PyCharm:

File > Settings

Settings to Change:

Turn off auto save:
* Appearance and Behavior > System Settings > Autosave
    * Turn off "Save files if the IDE is idle for _ Seconds"
    * Turn off "Save files when switching to a different application or a built-in terminal"

Turn ON unsaved indicator:
* Editor > General > Editor Tabs > Appearance
    * Turn on "Mark modified"

Change the Project Root:
* Project Structure > + Add Content Root
    * Select the board (it needs to be plugged into the computer and have the right buttons pressed)

Add circuitpython-stubs:
* Project Structure > Python Interpreter > Install
    * Search for "circuitpython-stubs" and install it.

Additional circuit python libraries (these are specific for Ciruit Playground):
* Also install:
    * adafruit_circuitplayground
    * adafruit_hid
    * adafruit_lis3dh
    * adafruit_thermistor
    * neopixel

