#!/usr/bin/env python3

from Xlib import XK
from keyboardio import keysym_to_keycode, grab, loop, press, simulating, alt_released
import time

class Movement():
    def __init__(self, key):
        self.keycode = keysym_to_keycode(key)
    def simulate(self):
        with simulating:
            with alt_released:
                press(self.keycode)
        
#grab('j', Movement(XK.XK_Down))
#loop()
time.sleep(3)
press(116)
