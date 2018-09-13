import os
from pygame_sdl2 import Surface
from pygame_sdl2.mixer import Sound

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
        self.registerResources()
        
    def getSounds(self, names):
        #return self.sounds.fromkeys(names)
        sounds = {}
        for key, sound in self.sounds.items():
            sounds[key] = sound
        return sounds
        
    def getPlaylist(self, queue):
        result = []
        for name in queue:
            result.append(self.tracks[name])
        return result
        
    def getImage(self, name):
        return self.images[name]
        
    def registerResources(self):
        soundfilenames = self.collectFilenames(self.soundspath, [".ogg", ".mp3"])
        trackfilenames = self.collectFilenames(self.trackspath, [".ogg", ".mp3"])
        imagefilenames = self.collectFilenames(self.imagespath, [".png", ".jpg"])
        for filename in soundfilenames:
            self.registerSound(filename)
        for filename in trackfilenames:
            self.registerTrack(filename)
        for filename in imagefilenames:
            self.registerImage(filename)
        
    def collectFilenames(self, directory, extensions):
        filenames = []
        for filename in os.listdir(directory):
            if filename.endswith(tuple(extensions)):
                filenames.append(filename)
        return filenames
        
    def registerSound(self, filename):
        path = os.path.join(self.soundspath, filename)
        self.sounds[filename] = Sound(path)
        
    def registerTrack(self, filename):
        path = os.path.join(self.trackspath, filename)
        self.tracks[filename] = path
        
    def registerImage(self, filename):
        path = os.path.join(self.imagespath, filename)
        #self.images[filename] = 