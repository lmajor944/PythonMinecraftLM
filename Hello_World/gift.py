from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -36
y = 17
z = -19
gift = mc.getBlock(x, y, z)

if gift == 57:
    print("Thanks for the Diamond")
elif gift == 6:
    print("I guess tree saplings are as good as diamonds...")
    
else:
    mc.postToChat("Bring a gift to " + str(x) + "," + str(y) + "," + str(z))
