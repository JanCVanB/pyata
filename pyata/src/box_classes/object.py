
##########################################################
##########################################################
# description: abstract class that represents a generic Object box
#
# autor: jeraman
# date: 13/04/2010
##########################################################
##########################################################

from box import *




#box class itself
class Object (Box):
    #constructor
    def __init__(self, x, y, label, id):
        Box.__init__(self,x, y, id)
        self.label = label
        
    
    #edits this object
    def edit(self, label):
        command = self.unselect() #unselects
        
        temp = self.click() #selects this
        for cmd in temp:
            command.append(cmd)
        
        for i in label: #sends all key pressed
            command.append("key 1 " + str(ord(i)) + " 0 ; ") 
            command.append("key 0 " + str(ord(i)) + " 0 ; ") 
        
        temp = self.unselect() #unselects this
        for cmd in temp:
            command.append(cmd)
            
        return command
    
    #aux static function to debug this class
    @staticmethod
    def debug():
        o = Object(10, 10, 0, "dac~")
        print o.edit("osc~")
        print o.edit("")
    