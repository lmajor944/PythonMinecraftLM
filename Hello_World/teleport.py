from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#set x, y, and z variables to represent coordinates
x = 10.7
y = 110.0
z = 12.6 

#change player position
mc.player.setTilePos(x, y, z)