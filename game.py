import pygame, time
import engine.pygpen as pp

from engine.systems.game_state_system import GameStateSystem
from engine.game_analytics import GameAnalytics, send_to_firebase

FPS = 60
WINDOW_SIZE = (1020, 660)
DISPLAY_SIZE = (340, 220)
START_TIME = time.time()

class Game(pp.PygpenGame):
    def load(self):
        pp.init(
            WINDOW_SIZE, fps_cap=FPS, caption='Echo of Fallens', opengl=True,
            input_path='data/dbs/key_configs/config.json',
            font_path='data/fonts',
            frag_path='shaders/shader.frag',
        )
        
        self.bg_surf = pygame.Surface(DISPLAY_SIZE, pygame.SRCALPHA)
        self.display = pygame.Surface(DISPLAY_SIZE, pygame.SRCALPHA)
        self.ui_surf = pygame.Surface(DISPLAY_SIZE, pygame.SRCALPHA)
        
        self.e['Renderer'].set_groups(['default', 'ui', 'background'])
        
        self.camera = pp.Camera(DISPLAY_SIZE, slowness=0.3, pos=(5, 0))
        
        self._init_state()
        self.reset()
    
    def _init_state(self):
        self.last_update_time = time.time()
    
    def _load_systems(self):
        self.gamestate_system = GameStateSystem()
    
    def reset(self):
        self._load_systems()
        
        self.e['Window'].start_transition()
        
        self.e['ScriptLoader'].load_scripts()
        self.e['ScriptLoader'].update()
    
    def update(self):
        current_time = time.time()
        self.last_update_time = current_time
        
        self.bg_surf.fill((0, 0, 0, 0))
        self.display.fill((0, 0, 0, 0))
        self.ui_surf.fill((0, 0, 0, 0))
        
        self.gamestate_system.update(current_time)
        
        if self.gamestate_system.is_in_gameplay():
            self._update_gameplay()
        
        self.e['ScriptLoader'].update()
        
        self.e['Renderer'].cycle({'default': self.display, 'ui': self.ui_surf, 'background': self.bg_surf})
        self.e['Window'].cycle({ 'surface': self.display, 'bg_surf': self.bg_surf, 'ui_surf': self.ui_surf})
    
    def _update_gameplay(self):       
        self.camera.update()
        
        self.e['EntityGroups'].update()
        self.e['EntityGroups'].renderz(offset=self.camera)

if __name__ == "__main__":
    try:
        Game().run()
    # game analytics
    finally:
        analytics = GameAnalytics.update(START_TIME)
        send_to_firebase(analytics)