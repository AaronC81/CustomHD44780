# CustomHD44780 Display Driver
CustomHD44780 is a very basic Python-based HD44780 16x2 display driver designed to be customized
to work with absolutely any single-board computer, including (but definitely not limited to) the 
Raspberry Pi and pcDuino.

## Example - Raspberry Pi
```python
import RPi.GPIO as GPIO

disp = HD44780Display(GPIO.output, GPIO.setup, ...) # enter your HD44780 pin numbers here
disp.begin()
disp.write("Hello, world!")
```

## How does it work?
CustomHD44780 handles interfacing with the display, but you need to provide two functions to tell
the library how to interact with your board's hardware:

   - `write_pin(pinNumber, signal)` - writes `signal` (either 1 or 0) to GPIO pin `pinNumber`.
   - `pin_mode(pinNumber, mode)` - configures GPIO pin `pinNumber` to act as an input (`mode == 0`) or output (`mode == 1`).

These are given in the constructor of `HD44780Display`. This flexibility allows the library to work
with **any** board, given you know how to interact with its GPIO pins.

## Why use this?
I needed to write a pcDuino HD44780 driver, but decided to make the library modular instead so that
it could be adapted to work with any other board.

If you'd like to use them, the two pcDuino GPIO functions are included in `pcDuinoFunctions.py`.