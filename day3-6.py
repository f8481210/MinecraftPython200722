# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:13:04 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
def buildPyramid(x,y,z,base=20):    
	   
	height = (base//2)+1    
	for i in range(height): #用來跑金字塔高度        
		x1 = x + i        
		y1 = y + i        
		z1 = z + i                

		x2 = x + base - i        
		#y2與y相同        
		z2 = z + base - i        
		mc.setBlocks(x1, y1, z1, x2, y, z2, 24)

x,y,z = mc.player.getTilePos()      
buildPyramid(x,y,z)
