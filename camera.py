from pygame_sdl2 import Rect
from .constants import R_WIDTH, R_HEIGHT

class Camera:
    view = None
    x, y = None, None
    target = None
    
    def __init__(self):
        self.view = Rect(0, 0, R_WIDTH, R_HEIGHT)
        
    def apply(self, target):
        return target.rect.move(self.view.topleft)
    
    def getScenePosition(self, pos):
        return (pos[0] - self.x, pos[1] - self.y)
        
        
    def setTarget(self, gameobject):
        self.target = gameobject
        
    def update(self):
        try:
            self.x = -self.target.x + int(R_WIDTH / 2)
            self.y = -self.target.y + int(R_HEIGHT / 2)
        except:
            self.x, self.y = 0, 0
        self.view = Rect(self.x, self.y, R_WIDTH, R_HEIGHT)
        
    def draw(self, gameobjects, surface):
        for gameobject in gameobjects:
            surface.blit(gameobject.image, self.apply(gameobject))