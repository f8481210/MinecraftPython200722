# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:21:36 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,\
            hit.pos.z
        block = mc.getBlock(x,y,z)
        mc.postToChat("你打到:"+str(block))
       #題目: 我要打到石頭的時候才變成黃金！
        #if block == 1:
        mc.setBlock(x,y,z,41)
        