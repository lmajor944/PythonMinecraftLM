import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
p = mc.player.getTilePos()
mc.setBlock(p.x, p.y, p.z, block.DIRT)
mc.setBlocks(p.x + 1, p.y, p.z + 1, p.x + 10, p.y + 5, p.z + 10,block.GLASS)