from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
highestBlockY = mc.getHeight(x, z)
highEnough = y >= highestBlockY
mc.postToChat(highestBlockY)

mc.postToChat("The Player is above the ground: " + str(highEnough))

