from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 10
y = 11
z = 12
melon = 103
block = mc.getBlock(x, y, z)

NoMelon = block != 103

mc.postToChat("You need to get more food: " + str(NoMelon))