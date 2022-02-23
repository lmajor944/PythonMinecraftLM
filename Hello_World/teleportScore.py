from mcpi.minecraft import Minecraft
mc = Minecraft.create()

points = int(input("Enter your points: "))
if points > 2:
    mc.player.setPos(-52, 17, 6)
elif points <= 2:
    mc.player.setPos(-19, 3, 24)
elif points > 4:
    mc.player.setPos(6, 7, 28)
elif points > 6:
    mc.player.setPos(49, 6, -1)
else:
    mc.postToChat("I don't know what to do with that information")
