
##########################################################
##########################################################
# description: example that moves objects and set values fro numbers dynamically
#
# autor: jeraman
# date: 26/04/2010
##########################################################
##########################################################



#imports Pyata library
from Pd import *
import math


#planet class for rotate boxes
class Planet():
    def __init__(self, radius, c_x, c_y, box):
        self.radius = radius
        self.c_x = c_x
        self.c_y = c_y
        self.box = box
    
    def move(self, angle):
        angle = math.radians(angle)
        x = self.radius * math.cos(angle)
        y = self.radius * math.sin(angle)
        x+=self.c_x
        y+=self.c_y
        x = int(x)
        y = int(y)
        self.box.move(x, y)




#mains method
if __name__ == '__main__':
    
    #creates an instance of Pd
    pd = Pd()
    
    #initializes Pyata
    pd.init()
    
    #creates some numbers
    n1=Number(100, 300)
    n2=Number(500, 300)
    n3=Number(300, 100)
    n4=Number(300, 500)
    
    #creates an object dac~ in 10, 10 on the patch
    dac = Object(10, 10, "dac~")
    #creates a planet to rotate boxes
    p1 = Planet(100, 300, 300, dac)
    
    #creates an oscillator
    osc = Object(dac.x+50, dac.y, "osc~")
    #creates another planet for the osc
    p2 = Planet(50,dac.x, dac.y, osc)
    
    #conencts osc to dac
    connect(osc, 0, dac, 0)
    
    #creates a number t control the synth
    centro=Number(300, 300)
    centro.set(440)
    
    #connects all numbers to osc
    connect(centro, 0, osc, 0)
    connect(osc, 0, n1, 0)
    connect(osc, 0, n2, 0)
    connect(osc, 0, n3, 0)
    connect(osc, 0, n4, 0)
    
    #init numbers used during the rotation
    i = 0
    j = 0
    
    #the main loop to rotate
    for time in range(150):
        i = (i+1)%361
        p1.move(i)
        p2.c_x = dac.x
        p2.c_y = dac.y
        j = (j+5)%361
        p2.move(j)
        centro.set(440+j)
        sleep(0.05)
        
        
    #finishes Pyata
    pd.quit()
    
   