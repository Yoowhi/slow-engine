import pygame_sdl2 as pg
from scene import Scene
from constants import *

class Game:
    running = True
    screen = None
    clock = None
    scene = None
    camera = None
    
    def __init__(self):
        pg.import_as_pygame()
        pg.init()
        self.screen = pg.display.set_mode((R_WIDTH, R_HEIGHT))
        self.clock = pg.time.Clock()
        #USER SCENE INIT
        
        self.run()
        
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
        self.drawObjects()
        
    def handleEvents(self):
        for event in pg.event.get():
            None
            
    def changeScene(self, newscene):
        self.pause()
        #camera pause here
        self.scene.exit()
        self.scene = newscene
        self.run()
        
    def drawObjects(self):
        self.screen.fill(COL_DARKGRAY)
        self.scene.gameobjects.draw(self.screen)
        pg.display.flip()
        
    