from mcpi.minecraft import Minecraft
mc = Minecraft.create()

position = mc.player.getTilePos()
x = 22
y = 0
z = 16
y = y + 10
mc.player.setTilePos(x, y, z)