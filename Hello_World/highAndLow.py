from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

heights = [100, 0]
count = 0

while count < 60:
    pos = mc.player.getTilePos()
    
    if pos.y < heights[0]:
        lowestHeight = pos.y - 1
    elif pos.y > heights[1]:
        highestHeight = pos.y + 12

    count += 1
    time.sleep(1)
mc.postToChat("Lowest: " + str(lowestHeight))
mc.postToChat("Highest: " + str(highestHeight))