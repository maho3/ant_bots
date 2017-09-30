import numpy as np


class Tree:

    def __init__(self, rate, radius, fieldX, fieldY):
        self.x = np.random.rand()*fieldX
        self.y = np.random.rand()*fieldY
        self.rate = rate
        self.radius = radius
        self.b = [(self.x, self.y)]

    def update(self):
        if (np.random.rand() <= self.rate):
            t = np.random.rand() * 2 * np.pi
            r = np.random.rand() * self.radius

            banX = self.x + r*np.cos(t)
            banY = self.y + r*np.sin(t)

            self.b.append((banX,banY))


class Field:

    def __init__(self, X, Y, numTrees, rate, radius):
        self.X = X
        self.Y = Y
        self.numTrees = numTrees

        self.trees = [Tree(rate, radius, X, Y) for i in range(numTrees)]


    def update(self):

        for i in self.trees:  i.update()


