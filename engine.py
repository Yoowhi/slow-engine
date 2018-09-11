import pygame_sdl2 as pg
from .scene import Scene
from .constants import *
from .mixer import Mixer

class Engine:
    running = False
    screen = None
    clock = None
    scene = None
    camera = None
    mixer = None
    
    def __init__(self):
        pg.import_as_pygame()
        pg.mixer.pre_init(S_DISFREQUENCY, S_SAMPLESIZE, S_CHANNELS, S_BUFFERSIZE)
        pg.init()
        pg.mixer.init()
        pg.mixer.music.set_endevent(SONG_ENDS)
        self.mixer = Mixer()
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
            if event.type == MOUSEBUTTONDOWN:
                pos = self.camera.getScenePosition(event.pos)
                self.scene.mouseButtonDown(pos, event.button)
            elif event.type == MOUSEBUTTONUP:
                pos = self.camera.getScenePosition(event.pos)
                self.scene.mouseButtonUp(pos, event.button)
            elif event.type == KEYDOWN:
                self.scene.keyDown(event.key, event.mod)
            elif event.type == KEYUP:
                self.scene.keyUp(event.key, event.mod)
            if event.type == MOUSEMOTION:
                pos = self.camera.getScenePosition(event.pos)
                self.scene.mouseMotion(pos, event.rel, event.buttons)
            if event.type == SONG_ENDS:
                self.mixer.next()
            
    def openScene(self, scene):
        self.pause()
        if isinstance(self.scene, Scene):
            self.scene.exit()
        self.scene = scene
        self.camera = scene.camera
        
    def render(self):
        self.screen.fill(COL_DARKGRAY)
        self.camera.draw(self.scene.gameobjects, self.screen)
        pg.display.flip()
        
    