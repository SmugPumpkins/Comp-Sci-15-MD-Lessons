While I finish building out this course content, as I think you guys will beat me to it, I will provide the resources here that I am learning from that we might just have to use together.
* [IR Overview](https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python/overview)
* [IR from CPX to CPX](https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python/ir-from-cpx-to-cpx)
* [Using IR as Input](https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python/using-ir-as-an-input)

# Overview
The IR Transciever built into the CircuitPlayground Express allows for wireless communication between multiple CircuitPlayground Express devices. IR is short for Infrared, a wavelength of light that is invisible to the naked eye. IR communication must have line of sight and only has a range of around 10-20 meters.
# Important Information
The IR Transmitter is labeled as TX and the IR Receiver is labeled as RX. They are located on either side of the reset button.

![IR Transceiver](https://cdn-learn.adafruit.com/assets/assets/000/057/858/medium640/light_circuitpython_CPX_IR_TX_RX.jpg?1532480921)
## Important Libraries
The following libraries need to be installed on PyCharm.
```
adafruit-circuitpython-irremote
```

You also need to download and unzip the bundle from here to find the irremote library. https://circuitpython.org/libraries 

Once unzipped, open up the lib folder from the zip file, and copy the file called `adafruit_irremote.mpy` to the lib folder on the CIRCUITPY drive 
## Transmitting

## Receiving