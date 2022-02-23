from mcpi.minecraft import Minecraft
mc = Minecraft.create()
colorString = input("Enter a block color: ")
def getWoolState(color):
    if color == "pink":
        blockState = 6
    elif color == "red":
        blockState = 14
    elif color == "yellow":
        blockState = 4
    elif color == "lime":
        blockState = 5
    return blockState

state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)