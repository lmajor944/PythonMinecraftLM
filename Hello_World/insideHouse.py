from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# -54.1, 28.9, -26.2
buildX = -54.1
buildY = 28.9
buildZ = -26.2
width = 10
height = 5
length = 6

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length
mc.postToChat("You are in your house: " + str(inside))