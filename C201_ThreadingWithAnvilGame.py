from mcpi.minecraft import *
from mcpi.block import *
from time import sleep
from random import randint
import threading

mc = Minecraft.create()

mc.postToChat("Welcome to Anvil Drop!")
sleep(2)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

roomx = x
roomy = y
roomz = z

mc.setBlocks(x+10,y-1,z+10,x-10,y+15,z-10,GLASS)
mc.setBlocks(x+9,y,z+9,x-9,y+15,z-9,AIR)

mc.postToChat("Avoid the falling anvils!")
sleep(2)
mc.postToChat("Get ready...")
sleep(1)
for i in range(3,0,-1):
    mc.postToChat(i)
    sleep(1)

mc.postToChat("Go!")
dropSpeed = 3

#difficulty setter
def setDifficulty():
    counter = 1
    global dropSpeed
    mc.postToChat("Delay between anvils is: "+str(dropSpeed)+" seconds")
    mc.postToChat("Time Elapsed:")
    sleep(1)
    while(True):
        mc.postToChat(counter)
        if((counter%10)==0):
            mc.postToChat("It's getting faster!")
            dropSpeed *= 0.5
            mc.postToChat("Delay is now: "+str(dropSpeed)+" seconds")
        sleep(1)
        counter += 1

def clearGround():
    while(True):
        mc.setBlocks(roomx+9,roomy,roomz+9,roomx-9,roomy,roomz-9,AIR)
        sleep(0.1)

t1 = threading.Thread(target=setDifficulty)
t2 = threading.Thread(target=clearGround)
t1.start()
t2.start()

#Game Start
while(True):
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z

    numx = randint(-3,3)+x
    numz = randint(-3,3)+z
    while(not(numx<roomx+10 \
              and numx>roomx-10 \
              and numz<roomz+10 \
              and numz>roomz-10)):
        numx = randint(-3,3)+x
        numz = randint(-3,3)+z

    mc.setBlock(numx,roomy+15,numz,145)
    mc.setBlocks(roomx+9,roomy,roomz+9,roomx-9,roomy,roomz-9,AIR)
    sleep(dropSpeed)




    




