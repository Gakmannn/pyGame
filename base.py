class Point:

    def __init__(self):
        self.x = 0
        self.y = 0


class Object:

    def __init__(self, x, y):
        self.topleft = (x, y)
        self.move = Point()

    def update(self):
        pass

    def Collide(self):
        pass
