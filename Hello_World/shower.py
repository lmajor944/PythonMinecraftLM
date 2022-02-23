from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = -51
shwrY = 17
shwrZ = 6

width = 5
height = 5
length = 5

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x + width and shwrY <= y + height and shwrZ <= z + length:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ, shwrX + width, shwrY + height, shwrZ + length, 0)
    
    

