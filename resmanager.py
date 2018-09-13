from os import path

class ResourceManager:
    sounds = None
    tracks = None
    images = None
    soundspath = None
    trackspath = None
    imagespath = None
    
    def __init__(self, soundspath, trackspath, imagespath):
        self.sounds = {}
        self.tracks = {}
        self.images = {}
        self.soundspath = soundspath
        self.trackspath = trackspath
        self.imagespath = imagespath
        
    def getSounds(self, names):
        return
        
    def getPlaylist(self, queue):
        return
        
    def getImage(self, name):
        return
        
    def registerSound(self, filename):
        return
        
    def registerTrack(self, filename):
        return
        
    def registerImage(self, filename):
        return
        