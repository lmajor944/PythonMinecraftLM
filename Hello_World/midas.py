from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
water = 9
count = 1
while count == 1:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if blockBelow != 9 or blockBelow != 0: 
        mc.setBlock(pos.x, pos.y, pos.z, 41)
        