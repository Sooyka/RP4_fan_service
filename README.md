# Rapsberry Pi 4 fan controller

Original fan for RP4 can be controlled with PWM, however, there was no controller for it outside of Raspbian.

# Usage

This controller reads cpu temperature and scale fan speed linearly with it, with minimum at 50 celsius and max at 70 celsius.
On default settings it gives pwm at pin 12 on RP4, which GPIO 18 and pwm0.

## Config

There is planned config to be added
