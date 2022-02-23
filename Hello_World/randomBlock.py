from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
ids = [10, 8, 2, 4, 5]
cool = random.choice(ids)
mc.setBlock(x, y, z, cool)

