from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -2
y = 13
z = -8
blockType = 103
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + 1, z, blockType)