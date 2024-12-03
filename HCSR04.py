"""
A lightweight MicroPython implementation for interfacing with an HC-SR04 Ultrasonic Sensor
Author: Sombit Pramanik - https://github.com/SombitPramanik/
Version: 1.0
Get updates to this code file here: https://github.com/SombitPramanik/UL_Sensor_HC_SR04

License: MIT License
Copyright 2024 Sombit Pramanik
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# HC-SR04 is the Name/Model of the Ultrasonic Sensor
from machine import Pin, time_pulse_us
import utime


class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.trigger.low()

    def measure_distance(self):
        # Send a 10-microsecond pulse to trigger pin
        self.trigger.high()
        utime.sleep_us(10)
        self.trigger.low()

        # Measure the time for the echo pulse
        try:
            pulse_time = time_pulse_us(self.echo, 1, 30000)  # Timeout: 30ms
        except OSError:
            return None  # Return None if no echo is received within timeout

        # Calculate distance in centimeters
        distance = (pulse_time / 2) / 29.1
        return distance
