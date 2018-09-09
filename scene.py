from .gameobject import GameObject
from pygame_sdl2.sprite import Group

class Scene():
    gameobjects = None
    colliders = None
    
    def __init__(self):
        self.gameobjects = Group()
        self.colliders = Group()
        self.onStart()
    
    def update(self):
        for gameobject in self.gameobjects:
            gameobject.update()
            
    def exit(self):
        self.onExit()
            
    def addGameObject(self, gameobject):
        self.gameobjects.add(gameobject)
        if gameobject.iscollider:
            self.colliders.add(gameobject)
            
    #USER METHODS
    def onStart(self):
        return
        
    def onUpdate(self):
        return
        
    def onExit(self):
        return