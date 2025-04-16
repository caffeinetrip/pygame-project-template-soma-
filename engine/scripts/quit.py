import sys
import engine.pygpen as pp

class Quit(pp.GameScript):
    def __init__(self):
        super().__init__()
    
    def on_update(self):
        if self.e['Input'].pressed('quit'):
            sys.exit()