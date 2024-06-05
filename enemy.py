import pygame
from base import Object
from load_image import load_image
from phisics import AlivePhisics

class Enemy(Object):        
    def __init__(self, x, y):
       Object.__init__(Object, x, y)
       self.Phisics = AlivePhisics
        
       
class Turtle(pygame.sprite.Sprite,Enemy):
    def __init__(self, x, y):
        Enemy.__init__(Enemy, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("turtle.jpg", -1, .3)
        self.move = pygame.Vector2()
        # self.image.fill(pygame.Color("#000000"))
        self.rect.topleft = self.topleft
        self.move.x = -1
    def update(self, allObjects):
        self.Phisics.Gravity(self.Phisics, self, allObjects)
        self.collide(allObjects)
        newpos = self.rect.move((self.move.x*2, self.move.y*2))
        self.rect = newpos
    def collide(self, allObjects):
        for obj in allObjects:
            if "EnemyReverse" in type(obj).__name__ and self.rect.colliderect(obj.rect):
                if self.move.x > 0:
                    newpos = self.rect.move((8, self.move.y*2))
                    self.rect = newpos
                    self.move.x = -self.move.x
                else: 
                    newpos = self.rect.move((-8, self.move.y*2))
                    self.rect = newpos
                    self.move.x = -self.move.x
                    
class Mushroom(pygame.sprite.Sprite,Enemy):
    def __init__(self, x, y):
        Enemy.__init__(Enemy, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("mashroom.jpg", -1, .3)
        self.move = pygame.Vector2()
        # self.image.fill(pygame.Color("#000000"))
        self.rect.topleft = self.topleft
        self.move.x = -1
    def update(self, allObjects):
        self.Phisics.Gravity(self.Phisics, self, allObjects)
        self.collide(allObjects)
        newpos = self.rect.move((self.move.x*2, self.move.y*2))
        self.rect = newpos
    def collide(self, allObjects):
        for obj in allObjects:
            if "EnemyReverse" in type(obj).__name__ and self.rect.colliderect(obj.rect):
                if self.move.x > 0:
                    newpos = self.rect.move((8, self.move.y*2))
                    self.rect = newpos
                    self.move.x = -self.move.x
                else: 
                    newpos = self.rect.move((-8, self.move.y*2))
                    self.rect = newpos
                    self.move.x = -self.move.x
    