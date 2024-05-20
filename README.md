A Python library for controlling the adafruit [64x64 RGB LED Matrix](https://www.adafruit.com/product/3649). 
>Can be used on smaller/bigger LED matrices, edit the parser values in the `MatrixBase` class.
## `base.py`:
Entry point for the matrix; [hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library is used for drawing into the matrix. `MatrixBase` is a helper class that handles all the matrix options and drawing. It should be 
