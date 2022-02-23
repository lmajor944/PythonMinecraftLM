from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -29
y = 25
z = -22

gift = mc.getBlock(x, y, z)
if gift == 57:
    mc.setBlock(-28, 25, -22, 0)
    mc.setBlock(-28, 26, -22, 0)
else:
    mc.postToChat("Place an offering on the pedestal.")