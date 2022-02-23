from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z, 8)

score = 0

while blockAbove == 8 or blockAbove == 9:
    time.sleep(1)
    pos = mc.player.getPos()
    blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z, 8)
    score = score + 1
    mc.postToChat("Current Score: " + str(score))
    mc.postToChat("Final Score: " + str(score))
if score > 6:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)