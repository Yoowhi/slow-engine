import pygame_sdl2 as pg
from scene import Scene
from constants import *

class SlowEngine:
    running = False
    screen = None
    clock = None
    scene = None
    camera = None
    
    def __init__(self):
        pg.import_as_pygame()
        pg.init()
        self.screen = pg.display.set_mode((R_WIDTH, R_HEIGHT))
        self.clock = pg.time.Clock()
        
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(int(1000/R_FPS))
            self.tick()
            
    def pause(self):
        self.running = False
            
    def tick(self):
        self.handleEvents()
        self.scene.update()
        self.render()
        
    def handleEvents(self):
        for event in pg.event.get():
            None
            
    def openScene(self, scene):
        self.pause()
        #camera pause here
        if isinstance(self.scene, Scene):
            self.scene.exit()
        self.scene = scene
        
    def render(self):
        self.screen.fill(COL_DARKGRAY)
        self.scene.gameobjects.draw(self.screen)
        pg.display.flip()
        
    