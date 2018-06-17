from mcpi.minecraft import *
from mcpi.entity import *
from mcpi.block import *
from time import sleep

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlock(x+3,y-1,z+3,DIAMOND_BLOCK)
mc.setBlock(x+3,y-1,z+9,IRON_BLOCK)
mc.setBlock(x-3,y-1,z+3,GOLD_BLOCK)
mc.setBlock(x-3,y-1,z+9,REDSTONE_BLOCK)

eid = mc.spawnEntity(SHEEP,x+3,y,z+3,"{NoAI:1}")
while(True):
    mc.entity.setTilePos(eid,x+3,y,z+9)
    sleep(1)
    mc.entity.setTilePos(eid,x-3,y,z+9)
    sleep(1)
    mc.entity.setTilePos(eid,x-3,y,z+15)
    sleep(1)
    mc.entity.setTilePos(eid,x+3,y,z+15)
    sleep(1)
