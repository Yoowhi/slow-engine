from pygame_sdl2.sprite import Sprite, Rect
from  pygame_sdl2 import Surface
from .constants import TILE_WIDTH, TILE_HEIGHT, COL_GREEN

class GameObject(Sprite):
    x, y = None, None
    iscollider = False
    image = None
    rect = None
    
    def __init__(self, image = None, place = (None, None), iscollider = False):
        Sprite.__init__(self)
        if image != None:
            self.image = image
            #CONVERT THE IMAGE!!!!---------------
        else:
            self.image = Surface((TILE_WIDTH, TILE_HEIGHT))
            self.image.fill(COL_GREEN)
        self.rect = self.image.get_rect()
        self.x, self.y = place
        self.rect.topleft = self.x, self.y
        self.iscollider = iscollider
        self.onStart()
        
    def update(self):
        self.onUpdate()
        self.rect.x = self.x
        self.rect.y = self.y
        
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