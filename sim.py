import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as anim

from bots import Bot
from field import Field

fieldX = 2000
fieldY = 2000
frames = 1000

botnum = 500

treenum = 60
bspawn = 0.3
tradius = 100


field = Field(fieldX, fieldY, treenum, bspawn, tradius)

botlist = [Bot(field) for i in range(botnum)]

xs = [0] * frames
ys = [0] * frames
ths = [0] * frames

bxs = [0] * frames
bys = [0] * frames

for i in range(frames):
	print(i+1)

	field.update()

	bs = []
	for tree in field.trees:
		bs += tree.b
	bxs[i], bys[i] = zip(*bs)

	np.random.shuffle(botlist)

	for bot in botlist: bot.update(field)

	botlist = [bot for bot in botlist if bot.life]

	if len(botlist)==0: continue

	xs[i], ys[i], ths[i] = zip(*[(bot.x, bot.y, bot.theta) for bot in botlist])

fig, ax = plt.subplots()
ax.set_xlim(0,fieldX)
ax.set_ylim(0,fieldY)

treexs, treeys = zip(*[(tree.x, tree.y) for tree in field.trees])
treescat = ax.scatter(treexs, treeys,marker='o')

botscat = ax.quiver(xs[0],ys[0],np.cos(np.array(ths[0])), np.cos(np.array(ths[0])),
				 scale=75, headwidth=2, headlength=3)

banscat = ax.scatter(bxs[0], bys[0], marker='.')

def update(frame):
	botscat.set_offsets([i for i in zip(frame[0],frame[1])])
	botscat.set_UVC(np.cos(np.array(frame[2])), np.sin(np.array(frame[2])))

	banscat.set_offsets([i for i in zip(frame[3],frame[4])])
	return botscat,banscat,

animation = anim.FuncAnimation(fig, update, [i for i in zip(xs,ys,ths,bxs,bys)], interval=50, blit=True)
plt.show()



