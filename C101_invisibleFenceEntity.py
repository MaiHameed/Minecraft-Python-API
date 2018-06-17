from mcpi.minecraft import *
from mcpi.entity import *
from mcpi.block import *
from time import sleep

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x+3,y-1,z+3,x-3,y-1,z+9,DIAMOND_BLOCK)
pig = mc.spawnEntity(PIG,x,y,z)
sheep = mc.spawnEntity(SHEEP,x,y,z)

while(True):
    pigpos = mc.entity.getTilePos(pig)
    sheeppos = mc.entity.getTilePos(sheep)
    if((pigpos.x>=x+3) or\
       (pigpos.x<=x-3) or\
       (pigpos.z>=z+9) or\
       (pigpos.z<=z+3)):
        mc.entity.setTilePos(pig,x,y,z+6)
        mc.postToChat("Get back here pig!")
    if((sheeppos.x>=x+3) or\
       (sheeppos.x<=x-3) or\
       (sheeppos.z>=z+9) or\
       (sheeppos.z<=z+3)):
        mc.entity.setTilePos(sheep,x,y,z+6)
        mc.postToChat("Get back here sheep!")
    sleep(0.01)
        
