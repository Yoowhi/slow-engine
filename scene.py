from .gameobject import GameObject
from  .camera import  Camera
from pygame_sdl2.sprite import Group

class Scene():
    gameobjects = None
    colliders = None
    camera = None
    
    def __init__(self):
        self.gameobjects = Group()
        self.colliders = Group()
        self.camera = Camera()
        self.onStart()
    
    def update(self):
        for gameobject in self.gameobjects:
            gameobject.update()
        self.camera.update()
        
    def draw(self, surface):
        for gameobject in self.gameobjects:
            surface.blit(gameobject.image, self.camera.apply(gameobject))
            
    def exit(self):
        self.onExit()
        
    #METHODS FOR USER CALLS
    def addGameObject(self, gameobject):
        self.gameobjects.add(gameobject)
        if gameobject.iscollider:
            self.colliders.add(gameobject)
            
    def bindCamera(self, gameobject):
        self.camera.setTarget(gameobject)
            
    #USER METHODS
    def onStart(self):
        return
        
    def onUpdate(self):
        return
        
    def onExit(self):
        return