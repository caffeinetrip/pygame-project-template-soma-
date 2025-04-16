import sys
import engine.pygpen as pp

class quit(pp.GameScript):
    def on_update(self):
        if self.e['Input'].pressed('quit'):
            sys.exit()