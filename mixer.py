from pygame_sdl2.mixer import music
from .constants import S_VOLUME, S_MUSICVOLUME

class Mixer:
    playlist = None
    current = -1
    
    def __init__(self):
        self.playlist = []
        self.setVolume(S_MUSICVOLUME)
        
    def next(self):
        music.stop()
        if len(self.playlist) > 0:
            if (self.current < len(self.playlist) - 1) and (self.current >= 0):
                self.current += 1
            else:
                self.current = 0
            self.play(file = self.playlist[self.current])
        else:
            self.current = -1
            self.stop()
        
    def play(self, file):
        music.load(file)
        music.play()
        
    def setVolume(self, volume):
        music.set_volume(1 * S_VOLUME * volume)
    
    def stop(self):
        music.stop()
        
    def setPlaylist(self, playlist):
        self.playlist = playlist
        self.current = -1