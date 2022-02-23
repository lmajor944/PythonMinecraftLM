from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y + 1
z = pos.z

blockType = mc.getBlock(x, y, z)
mc.postToChat(blockType != 0)
blockType2 = mc.getBlock(x, y + 1, z)
mc.postToChat(blockType2 != 0)
mc.postToChat(str(blockType) + str(blockType2))