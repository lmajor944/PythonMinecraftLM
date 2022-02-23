from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

blockType = 2
def randomBlockLocations(blockType, repeatS):
    count = 0
    while count <= 8:
        x = random.radint(-127, 127)
        z = random.radint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count += 1
