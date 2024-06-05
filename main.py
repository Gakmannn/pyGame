import sys
import pygame
from base import Object
from load_image import load_image
from surface import Briak, Question, Ground, GroundPipe, PipeEntrance, EnemyReverse
from enemy import Mushroom, Turtle
from pygame.locals import QUIT
import pygame.examples.moveit as aliens
from math import pi
WIN_WIDTH = 900 
WIN_HEIGHT = 500
PLW = 72
PLH = 72
 
# aliens.main()

LevelMap = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0],
	[0,3,8,0,9,6,0,9,0,0,0,0,0,0,0,0,0],
	[0,0,2,5,9,1,1,7,0,9,0,0,0,0,0,0,8],
	[1,1,1,4,0,1,1,1,1,0,1,0,1,1,1,1,1],
]

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
	
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
    
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы

    return pygame.Rect(l, t, w, h)  
    
class AI:
    def __init__(self):
        pass
  
class Object:
    def __init__(self,x,y):
        self.topleft = (x, y)

class PowerMushroom(Object):
    pass
    
class Mario(pygame.sprite.Sprite, Object):
    def __init__(self, x, y):
        Object.__init__(Object, x, y)
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("mario.jpg", -1, .3)
        self.offset = (-20, -20)
        self.rect.topleft = self.topleft
        self.move = pygame.Vector2()
        self.jump = False
                
    def StartMove(self, buttonCode):
        if buttonCode == 119:
            pass
        elif buttonCode == 100:
            # D
            self.move.x = 1
            # self.rect.move_ip(self.offset)
        elif buttonCode == 97:
            # A
            self.move.x = -1
            
        elif buttonCode == 115:
            pass
        elif buttonCode == 32:
            # Space
            self.jump = True
            pass
        
    def StopMove(self, buttonCode):
        if buttonCode == 119:
            pass
        elif buttonCode == 100:
            # D
            self.move.x = 0
            # self.rect.move_ip(self.offset)
        elif buttonCode == 97:
            # A
            self.move.x = 0
            
        elif buttonCode == 115:
            pass
        elif buttonCode == 32:
            # Space
            self.jump = False
            pass

    def update(self, allObjects):
        self.Collide(allObjects)
        newpos = self.rect.move((self.move.x*2, self.move.y*2))
        self.rect = newpos

    def Collide(self, allObjects):
        onGrond = False
        for obj in allObjects:
            if "Ground" in type(obj).__name__ and self.rect.colliderect(obj.rect):
                onGrond = True

        if onGrond:
            if not self.jump:
                self.move.y = 0
            else:
                self.move.y = -60
        else:
            self.move.y = 1
            
        
class LevelConstructor:
    def __init__(self, LevelMap):
        self.LevelMap = LevelMap
    @staticmethod
    def init():
        # 72 x 72
        for yIndex, objLine in enumerate(LevelMap):
            for xIndex, obj in enumerate(objLine):
                if obj == 1:
                    o = Ground(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                # if obj == 2:
                #     allObjects.append(Mario(xIndex*70, yIndex*70))
                if obj == 3:
                    o = Briak(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                    o = Briak(xIndex*PLW+PLW/2, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                if obj == 4:
                    o = GroundPipe(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                if obj == 5:
                    o = PipeEntrance(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                if obj == 6:
                    o = Mushroom(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    monsters.add(o)
                    platforms.append(o)
                if obj == 7:
                    o= Turtle(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    monsters.add(o)
                    platforms.append(o)
                if obj == 8:
                    o = Question(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                    o = Briak(xIndex*PLW+PLW/2, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                if obj == 8:
                    o = Question(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                    o = Briak(xIndex*PLW+PLW/2, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                if obj == 9:
                    o = EnemyReverse(xIndex*PLW, yIndex*PLW)
                    entities.add(o)
                    platforms.append(o)
                    
pygame.init()
clock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# Create The Backgound
background = pygame.Surface(DISPLAYSURF.get_size())
background = background.convert()
bg = pygame.image.load("data/nebo.jpg")
background.fill((170, 238, 187))
pygame.display.set_caption('Hello World!')
mario = Mario(1*PLW, 4*PLW)
# allsprites = pygame.sprite.RenderPlain(allObjects)
entities = pygame.sprite.Group() # Все объекты
monsters = pygame.sprite.Group() # Все передвигающиеся объекты
platforms = [] # то, во что мы будем врезаться или опираться
LevelConstructor.init()
entities.add(mario)

total_level_width  = len(LevelMap[0])*PLW # Высчитываем фактическую ширину уровня
total_level_height = len(LevelMap)*PLH   # высоту
   
camera = Camera(camera_configure, total_level_width, total_level_height) 

while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # print(event.key)
            mario.StartMove(event.key)
        elif event.type == pygame.KEYUP:
            mario.StopMove(event.key)
    pygame.display.update()
    # allsprites.update()
    
    monsters.update(platforms)
    mario.update(platforms)
    
    # DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(bg, (0, 0))
    # allsprites.draw(DISPLAYSURF)
    camera.update(mario)
    for e in entities:
        DISPLAYSURF.blit(e.image, camera.apply(e))
    
    pygame.display.flip()
