from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

pos = mc.player.getTilePos()

x,y,z = pos.x, pos.y, pos.z

while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(0.3, 0.3)
    y = mc.getHeight(x, z)
    
    mc.player.setPos(x, y, z)
    time.sleep(0.1)
