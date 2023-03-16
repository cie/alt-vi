import re
from autokey.interface import XRecordInterface
from autokey.model.key import Key

class ConfigManager:
    def __init__(self):
        self.hotKeys =[]
        self.hotKeyFolders =[]
        self.globalHotkeys =[]
        self.workAroundApps = re.compile('bzzzzz')

class App:
    def __init__(self):
        self.configManager = ConfigManager()

class Mediator:
    def set_modifier_state(self, modifier, state):
        pass
        
#grab('j', Movement(XK.XK_Down))
#loop()
time.sleep(3)

interface = XRecordInterface(Mediator(), App())
interface.initialise()