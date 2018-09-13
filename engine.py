import pygame_sdl2 as pg
from .scene import Scene
from .gameobject import GameObject
from .constants import *
from .mixer import Mixer
from .resmanager import ResourceManager

class Engine:
    running = False
    screen = None
    clock = None
    scene = None
    camera = None
    mixer = None
    framerate = None
    devmode = False
    
    def __init__(self, devmode = False, soundspath = "", trackspath = "", imagespath = ""):
        pg.import_as_pygame()
        pg.mixer.pre_init(S_DISFREQUENCY, S_SAMPLESIZE, S_CHANNELS, S_BUFFERSIZE)
        pg.init()
        pg.mixer.init()
        pg.font.init()
        self.devmode = devmode
        self.framerate = pg.font.Font(None, 32)
        pg.mixer.music.set_endevent(TRACK_ENDS)
        self.mixer = Mixer()
        self.resmanager = ResourceManager(soundspath, trackspath, imagespath)
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
            if event.type == MOUSEBUTTONUP:
                pos = self.camera.getScenePosition(event.pos)
                self.scene.mouseButtonUp(pos, event.button)
            if event.type == KEYDOWN:
                self.scene.keyDown(event.key, event.mod)
            if event.type == KEYUP:
                self.scene.keyUp(event.key, event.mod)
            if event.type == MOUSEMOTION:
                pos = self.camera.getScenePosition(event.pos)
                self.scene.mouseMotion(pos, event.rel, event.buttons)
            if event.type == TRACK_ENDS:
                self.mixer.next()
            if event.type == REQUEST_PLAYLIST:
                playlist = self.resmanager.getPlaylist(event.list)
                self.mixer.setPlaylist(playlist)
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
        if self.devmode:
            fpssurf = self.framerate.render(str(int(self.clock.get_fps())), True, COL_GREEN)
            self.screen.blit(fpssurf, (0, 0))
        pg.display.flip()
    