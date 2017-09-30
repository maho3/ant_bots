
import numpy as np


class Bot:
    
    stomach=1.0
    radius = 10
    speed = 5
    life = True
    
    theta = np.random.rand()*2*np.pi
    
    def __init__(self, field):
        self.x = np.random.rand()*field.X
        self.y = np.random.rand()*field.Y
        self.BoundX = field.X
        self.BoundY = field.Y


    def repeatBounds(self):
        if self.x < 0:
            self.x += self.BoundX
        elif self.x > self.BoundX:
            self.x -= self.BoundX

        if self.y < 0:
            self.y += self.BoundY
        elif self.y > self.BoundY:
            self.y -= self.BoundY


    def control(self):
        v = 1 * np.random.rand() - 0.5

        self.theta += v * np.pi

    def update(self, field):
        self.stomach -= 0.01

        if self.stomach <= 0:
            self.life=False
            return

        for tree in field.trees:
            if ((tree.radius + self.radius)**2 > ((self.x - tree.x)**2 + (self.y - tree.y)**2)):

                i = 0

                while i < len(tree.b):
                    if (self.radius**2 > ((self.x - tree.b[i][0])**2 + (self.y - tree.b[i][1])**2)):
                        self.stomach += 0.5
                        del tree.b[i]
                        i-=1
                    i+=1

        self.control()

        self.x += self.speed * np.cos(self.theta)
        self.y += self.speed * np.sin(self.theta)

        self.repeatBounds()


