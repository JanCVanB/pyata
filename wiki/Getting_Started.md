if you want to start using Pyata, read this simple guide.

Considerations
==============

Some stuff to have in mind before starting:

1.  This library works **always** with pd in edit mode. So, if you don't
    want crash your program, don't change it.
2.  Untill this version, it's **not recommended** to create two boxes
    too near (in x-y position) one from other. This is very important if
    you don't want to bug your program. This happens due to the manner
    Pyata was built, based on the position of the boxes on the patch
    that runs on Pd. So make sure to create boxes keeping a good
    distance between them.
3.  The library is still in beta phase. So if you find a bug, please,
    let me know.

Still before starting...
========================

Before using, you have to install Pyata. You can find how to do it
[here](How_To_Install.md).

Quick tutorial!
===============

http://web12.twitpic.com/img/90356545-bc6087f87a17b1f7b427111b798ce3cf.4bd1d12a-full.png

This tutorial is quite simple. It will create an oscilator ("osc\~") and
a digital-analogic converter ("dac\~"), connecting them. The image above
shows the final result. You can find further informations of classes,
methods and what you can do with them reading the [Pd](Pd.md),
[Box](Box.md), [Object](Object.md), [Number](Number.md),
[Message](Message.md), [Symbol](Symbol.md), [Comment](Comment.md) and
[Others](Others.md), API specification.

~~~~ {.prettyprint}
#imports Pyata library
from Pd import *


#mains method
if __name__ == '__main__':
    
    #creates an instance of Pd
    pd = Pd()
    
    #initializes Pyata
    pd.init()
    
    #creates an object dac~ in 10, 10 on the patch
    dac = Object(10, 10, "dac~")
    
    #moves the dac to 300, 300
    dac.move(200, 200)
    
    #creates an object osc~ in 200, 100 on the patch
    osc = Object(200, 150, "osc~")
    
    #connects the outlet 0 from osc to the inlet 0 from dac
    connect(osc, 0, dac, 0)
    
    #edits the osc object from "osc~" to "osc~ 220"
    osc.edit("osc~ 220")
    
    sleep(2)
    
    #creates an number in 200, 10 on the patch
    n1 = Number(osc.x, osc.y-50)
    
    #connects the outlet 0 from osc to the inlet 0 from dac
    connect(n1, 0, osc, 0)
    
    #sets the value from the number to 440
    n1.set(440)
    
    sleep(2)
    
    #increments n1 120 times
    for i in range(0, 220):
        n1.increment()
    sleep(2)
    
    #prints n1 value
    print n1.get_value()
    
    #prints all objects available in memory
    print pd.get_box_list()
    
    #prints all connections available in memory
    print pd.get_connection_list()
    
    sleep(2)
    
    
    #finishes Pyata
    pd.quit()
~~~~


