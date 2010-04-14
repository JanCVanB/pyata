
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
    def __init__(self, x, y, label, id=-1):
        Box.__init__(self,x, y, id)
        self.label = label
        command = Box.canvas + "obj " + str(self.x) + " " + str(self.y) + " " + self.label + "; "
        Box.snd.send_pd(command)
        
    
    #edits this object
    def edit(self, label):
        self.unselect() #unselects
        self.click() #selects this    
        
        command = ""
        for i in label: #sends all key pressed
            command += Box.canvas + "key 1 " + str(ord(i)) + " 0 ; "
            command += Box.canvas + "key 0 " + str(ord(i)) + " 0 ; " 
        
        Box.snd.send_pd(command)
        self.unselect() #unselects this
        self.label = label
        
    
    #aux static function to debug this class
    @staticmethod
    def debug():
        o = Object(10, 10, 0, "dac~")
        print o.edit("osc~")
        print o.edit("")
    