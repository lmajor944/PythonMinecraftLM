from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -4
y = 8
z = -6
blockType = 103
up = 1
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)
