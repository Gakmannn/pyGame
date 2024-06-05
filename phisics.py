class Phisics:
    def __init__(self):
        pass

class SurfacePhisics(Phisics):
    def __init__(self):
        pass

class EntrancePhisics(Phisics):
    def __init__(self):
        pass
    
class AlivePhisics(Phisics):
    def __init__(self):
        pass
            
    def Gravity(self, object, allObjects):
        onGrond = False
        for obj in allObjects:
            if "Ground" in type(obj).__name__ and object.rect.colliderect(obj.rect):
                onGrond = True
            if not onGrond:
                object.move.y = 1
            else:
                object.move.y = 0