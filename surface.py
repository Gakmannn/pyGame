from base import Object
from phisics import EntrancePhisics 
from load_image import load_image
import pygame

class Surface(Object):
    def __init__(self,x,y):
       Object.__init__(Object, x, y)
    #    self.Phisics = SurfacePhisics

class SkySurface(Object):
    def __init__(self,x,y):
       Object.__init__(Object, x, y)
    #    self.Phisics = SurfacePhisics

class Entrance(Surface):
    def __init__(self,x,y):
       Surface.__init__(x, y)
       self.Phisics = EntrancePhisics

class EnemyReverse(pygame.sprite.Sprite, Surface):
    def __init__(self, x, y):
       Surface.__init__(Surface, x, y)
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((72, 72))
       self.image.fill(pygame.Color("#000000"))
       self.rect = pygame.Rect(0, 0, 72, 72)
       self.rect.topleft = self.topleft
       
class Briak(pygame.sprite.Sprite, SkySurface):
    def __init__(self, x, y):
        Surface.__init__(Surface, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("briak.png", None, .15)
        self.rect.topleft = self.topleft
                
    def update(self):
        pass

class Question(pygame.sprite.Sprite, SkySurface):
    def __init__(self, x, y):
        Surface.__init__(Surface, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("question.png", None, .15)
        self.rect.topleft = self.topleft
                
    def update(self):
        pass

class Ground(pygame.sprite.Sprite, Surface):
    def __init__(self, x, y):
        Surface.__init__(Surface, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("ground.jpg", None, .3)
        self.rect.topleft = self.topleft
                
    

class GroundPipe(pygame.sprite.Sprite, Surface):
    def __init__(self, x, y):
        Surface.__init__(Surface, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("groundpipe.jpg", None, .3)
        self.rect.topleft = self.topleft
                
    

class PipeEntrance(pygame.sprite.Sprite, Entrance):
    def __init__(self, x, y):
        Surface.__init__(Surface, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("pipe.png", -1, .3)
        self.rect.topleft = self.topleft
                
    