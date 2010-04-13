
##########################################################
##########################################################
# description: abstract class that represents a generic Object box
#
# autor: jeraman
# date: 13/04/2010
##########################################################
##########################################################

from box import *


class Object (Box):
    #constructor
    def __init__(self, x, y, label, id):
        Box.__init__(self,x, y, id)
        self.label = label
    
    #edits this object
    def edit(self, label):
        command = self.unselect() #unselects
        command += self.click() #clicks inside
        for i in label: #sends all key pressed
            command += "key 1 " + str(ord(i)) + " 0 ; " 
            command += "key 0 " + str(ord(i)) + " 0 ; " 
        command += self.unselect() #unselects
        return command
            
if __name__ == '__main__':
    o = Object(10, 10, 0, "dac~")
    print o.edit("osc~")
    print o.edit("")
    