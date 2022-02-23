from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):
    mc.setBlocks(x+3, y, z+3, x+1, y+6, z+1, 17)
    mc.setBlocks(x, y+6, z, x+5, y+12, z + 8, 18)
    

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
