from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

def randomBlockLocations(blockType, repeats):
    count = 0

    x = random.randint(-127, 127)
    z = random.randint(-127, 127)
    y = mc.getHeight(x, z)
    mc.setBlock(x, y, z)
    mc.setBlock(x, y, z, blockType)
    count += 1
    
