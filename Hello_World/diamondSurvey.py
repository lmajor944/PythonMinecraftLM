from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y - 1, pos.z
    
for i in range(1, 51):

    blockBelow = mc.getBlock(x, y - i, z)
    if blockBelow == 56:
        mc.postToChat("block is " + str(i) + " blocks below you!")
        time.sleep(8)
    else:
        mc.postToChat("no diamond block")
    