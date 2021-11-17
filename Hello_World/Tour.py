from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time


#set x, y, and z variables to represent coordinates
x = 12.5
y = 110.0
z = 12.5

#change player position
mc.player.setTilePos(x, y, z)

time.sleep(10)

x = 15
y = 10
z = 14

mc.player.setTilePos(x, y, z)