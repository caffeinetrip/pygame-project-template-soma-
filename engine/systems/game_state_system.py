import time
from .. import pygpen as pp

GAME_SCENES = ['game']

class GameStateSystem(pp.ElementSingleton):
    def __init__(self, custom_id=None):
        super().__init__(custom_id)
        self.scene = 'game'
        self.player_deaths = 0
        self.scene_transition_timer = 0
        self.transition_duration = 2.0
        self.game_over_start_time = 0
        self.scene_transitioning = False
        self.next_scene = None

    def start_scene_transition(self, next_scene):
        self.scene_transitioning = True
        self.scene_transition_timer = time.time()
        self.next_scene = next_scene
        self.e['Window'].e_start_transition()

    def update(self, current_time):
        if self.scene_transitioning and current_time - self.scene_transition_timer >= self.transition_duration:
            self.scene = self.next_scene
            self.scene_transitioning = False
            self.e['Window'].e_start_transition()
    
    def is_in_gameplay(self):
        return self.scene in GAME_SCENES