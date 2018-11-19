#meh.py
from mcpi import minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("BIG MEME")
x, y, z = mc.player.getPos()
#floor
mc.setBlocks(x, y-1, z, x+4, y-1, z, 1)
mc.setBlocks(x, y-1, z, x, y-1, z+10, 1)
