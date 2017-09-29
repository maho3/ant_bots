import numpy as np
import random 
import math

import matplotlib.pyplot as plt
import matplotlib.animation as anim

class Bot:
    
    stomach=0.5
    radius = 50
    speed = 10
    
    theta = random.random()*2*math.pi
    
    def __init__(self, fieldX, fieldY):
        self.x = random.random()*fieldX
        self.y = random.random()*fieldY
        self.BoundX = fieldX
        self.BoundY = fieldY


    def repeatBounds(self):
        if self.x < 0:
            self.x += self.BoundX
        elif self.x > self.BoundX:
            self.x -= self.BoundX

        if self.y < 0:
            self.y += self.BoundY
        elif self.y > self.BoundY:
            self.y -= self.BoundY  

    def update(self):
        v = 2*random.random()-1
        
        self.theta += v*math.pi
        
        self.x += self.speed * math.cos(self.theta)
        self.y += self.speed * math.sin(self.theta)

        self.repeatBounds()
	
        
        return self.x, self.y, self.theta
    

fieldX = 1000
fieldY = 1000
frames = 1000
botnum = 50

botlist = [Bot(1000,1000) for i in range(botnum)]

xs = [0]*frames
ys = [0]*frames
ths = [0]*frames

for i in range(frames):
    xs[i], ys[i], ths[i] = zip(*[botlist[i].update() for i in range(len(botlist))])

fig, ax = plt.subplots()
ax.set_xlim(0,fieldX)
ax.set_ylim(0,fieldY)

scat = ax.quiver(xs[0],ys[0],[0]*len(xs[0]), [1]*len(ys[0]))

def update(frame):
	scat.set_offsets([i for i in zip(frame[0],frame[1])])
	return scat,

animation = anim.FuncAnimation(fig, update, [i for i in zip(xs,ys)], interval=50, blit=True)
plt.show()



