from Xlib import X, display, XK
from Xlib.ext import xtest

queue = []

class Latch:
  def __init__(self):
    self.n = 0
  def __enter__(self):
    self.n += 1
  def decrement(self):
    print('decrementing latch')
    self.n -= 1
  def __exit__(self, *args):
    queue.append(self.decrement)
  def __bool__(self):
    return self.n > 0

simulating = Latch()


display = display.Display()
root = display.screen().root
def char_to_keycode(char: str):
    return display.keysym_to_keycode(ord(char))

def keysym_to_keycode(keysym):
    return display.keysym_to_keycode(keysym)

handlers = {}
def grab(char, handler):
    root.grab_key(char_to_keycode(char), X.Mod1Mask, True, X.GrabModeAsync, X.GrabModeAsync)
    handlers[char_to_keycode(char)] = handler

def loop():
    while True:
        if not display.pending_events():
            while queue:
                queue.pop(0)()
        handle(display.next_event())

def handle(event):
    if simulating: return
    print('received', event)
    if event.type == X.KeyPress:
        handler = handlers.get(event.detail)
        if handler: handler.simulate()

def press(keycode):
    print('press', keycode)
    xtest.fake_input(root, X.KeyPress, keycode)
    xtest.fake_input(root, X.KeyRelease, keycode)

class AltReleased:
    def __init__(self):
        self.keycode = keysym_to_keycode(XK.XK_Alt_L)
    def __enter__(self):
        print('releasing alt')
        xtest.fake_input(root, X.KeyRelease, self.keycode)
    def __exit__(self, *args):
        #print('re-pressing alt')
        #xtest.fake_input(root, X.KeyPress, self.keycode)
        pass
    
alt_released = AltReleased()