from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def Water():
    """Returns the value of the Water block"""
    return 8

def Wool():
    """Returns the value of the Wool block"""
    return 35

def Lava():
    """Returns the value of the Lava block"""
    return 10

def TNT():
    """Returns the value of the TNT block"""
    return 46

def Flower():
    """Returns the value of the Flower block"""
    return 37

def Diamond():
    """Returns the value of the Diamond block"""
    return 57

block = Flower()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, block)