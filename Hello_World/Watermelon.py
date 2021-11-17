import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
p = mc.player.getTilePos()
mc.setBlock(p.x, p.y, p.z, block.MELON)
