from pygame_sdl2.sprite import Sprite, Rect
from  pygame_sdl2 import Surface
from  pygame_sdl2.event import Event, post
from .constants import TILE_WIDTH, TILE_HEIGHT, COL_GREEN, REQUEST_SOUNDS

class GameObject(Sprite):
    x, y = None, None
    iscollider = False
    image = None
    rect = None
    sounds = None
    
    def __init__(self, image = None, place = (None, None), iscollider = False):
        self.sounds = {}
        Sprite.__init__(self)
        if image != None:
            self.image = image
            #CONVERT THE IMAGE!!!!---------------
        else:
            self.image = Surface((TILE_WIDTH, TILE_HEIGHT))
            self.image.fill(COL_GREEN)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.x, self.y = place
        self.rect.topleft = self.x, self.y
        self.iscollider = iscollider
        self.onStart()
        
    def update(self):
        self.onUpdate()
        self.rect.x = self.x
        self.rect.y = self.y
        
    #METHODS FOR USER CALLS
    def requestSounds(self, names):
        event = Event(REQUEST_SOUNDS, caller = self, list = names)
        post(event)
        
    #USER METHODS
    def onStart(self):
        return
        
    def onUpdate(self):
        return
        
    def onMouseButtonDown(self, pos, button):
        return
        
    def onMouseButtonUp(self, pos, button):
        return
        
    def onMouseMotion(self, pos, rel, buttons):
        return
        
    def onKeyDown(self, key, mod):
        return
        
    def onKeyUp(self, key, mod):
        return