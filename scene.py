from pygame_sdl2.sprite import Group
from pygame_sdl2.event import Event, post
from .camera import Camera
from .constants import REQUEST_SOUNDS, REQUEST_PLAYLIST

class Scene():
    gameobjects = None
    colliders = None
    camera = None
    sounds = None
    
    def __init__(self):
        self.gameobjects = Group()
        self.colliders = Group()
        self.camera = Camera()
        self.sounds = {}
        self.onStart()
        
    def mouseButtonDown(self, pos, button):
        self.onMouseButtonDown(pos, button)
        for gameobject in self.gameobjects:
            gameobject.onMouseButtonDown(pos, button)
            
    def mouseButtonUp(self, pos, button):
        self.onMouseButtonUp(pos, button)
        for gameobject in self.gameobjects:
            gameobject.onMouseButtonUp(pos, button)
        
    def mouseMotion(self, pos, rel, buttons):
        self.onMouseMotion(pos, rel, buttons)
        for gameobject in self.gameobjects:
            gameobject.onMouseMotion(pos, rel, buttons)
        
    def keyDown(self, key, mod):
        self.onKeyDown(key, mod)
        for gameobject in self.gameobjects:
            gameobject.onKeyDown(key, mod)
        
    def keyUp(self, key, mod):
        self.onKeyUp(key, mod)
        for gameobject in self.gameobjects:
            gameobject.onKeyUp(key, mod)
    
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
        
    def requestSounds(self, names):
        event = Event(REQUEST_SOUNDS, caller = self, list = names)
        post(event)
        
    def requestPlaylist(self, queue):
        event = Event(REQUEST_PLAYLIST, list = queue)
        post(event)
        
    def playSound(self, name):
        self.sounds[name].play()
            
    #USER METHODS
    def onStart(self):
        return
        
    def onUpdate(self):
        return
        
    def onExit(self):
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