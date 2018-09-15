from pygame_sdl2 import Surface, Rect
from pygame_sdl2.sprite import Sprite
from pygame_sdl2.font import Font
from .constants import FONT_DEFAULTSIZE, COL_WHITE

class GUIElement(Sprite):
    x, y = None, None
    width, height = None, None
    image = None
    rect = None
    
    def __init__(self, place, size, image = None):
        Sprite.__init__(self)
        self.x, self.y = place
        self.width, self.height = size
        if isinstance(image, Surface):
            self.image = image
        else:
            self.image = Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = place
        
    def get_place(self):
        return (self.x, self.y)
        
    def get_size(self):
        return (self.width, self.height)
        
class Label(GUIElement):
    text = None
    font = None
    fontsize = None
    color = None
    
    def __init__(self, place, text = "", fontname = None, fontsize = FONT_DEFAULTSIZE, color = COL_WHITE):
        self.text = text
        self.fontsize = fontsize
        self.color = color
        self.font = Font(fontname, fontsize)
        image = self.font.render(text, True, color)
        size = self.font.size(text)
        super(Label, self).__init__(place, size, image)
        
    def changeText(self, newtext):
        self.text = newtext
        self.image = self.font.render(newtext, True, self.color)
        self.rect = self.image.get_rect()
    
        
    