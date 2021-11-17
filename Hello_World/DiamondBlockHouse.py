import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
p = mc.player.getTilePos()
mc.setBlocks(p.x + 1, p.y, p.z + 1, p.x + 10, p.y + 5, p.z + 10, block.DIAMONDBLOCK)
mc.setBlocks(p.x + 2, p.y + 4, p.z + 2, p.x + 9