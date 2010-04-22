
from Pd import *


import math

radius = 100
c_x = 0
c_y = 0

#numero entre 0 e 1
def circle (x):
    x = (x*radius*2)+(c_x-radius)
    math
    print x
    term = math.sqrt(math.pow(radius, 2) - math.pow( (x - c_x) , 2) )
    return term + c_y 

#file created just for debug tests



if __name__ == '__main__':
    pd = Pd()
    pd.c.load_config()
    
   