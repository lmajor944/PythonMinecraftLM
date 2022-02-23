from mcpi.minecraft import Minecraft
mc = Minecraft.create()
height = 5
def setPillar(x, y, z, height):
    stairBlock = 156
    block = 155
    
    mc.setBlocks(x - 1, y + height, z - 1, x +1, y + height, z + 1, block, 1)
    mc.setBlocks(x - 1, y + height - 1, z, stairBlock, 12)
    mc.setBlocks(x + 1, y + height - 1, z, stairBlock, 13)
    mc.setBlocks(x, y + height - 1, z + 1, stairBlock, 15)
    mc.setBlocks(x, y + height - 1, z - 1, stairBlock, 14)
    
    mc.setBlocks(x - 1, y, z - 1,  x + 1, y, z +1, block, 1)
    mc.setBlocks(x - 1, y + 1, z, stairBlock, 0)
    mc.setBlocks(x + 1, y + 1, z, stairBlock, 1)
    mc.setBlocks(x, y + 1, z + 1, stairBlock, 3)
    mc.setBlocks(x, y + 1, z - 1, stairBlock, 2)
    
    mc.setBlocks(x,y, z, x, y + height, z, block, 2)
pos = mc.player.getTilePos()
x, y, z = pos.x + 2, pos.y, pos.z
for i in range(0,21):
    setPillar(x, y, z, height)
    