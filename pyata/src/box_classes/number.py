
##########################################################
##########################################################
# description: abstract class that represents a generic Number box
#
# autor: jeraman
# date: 13/04/2010
##########################################################
##########################################################

from box import *




#number class itself
class Number (Box):
    #constructor
    def __init__(self, x, y, id):
        Box.__init__(self,x, y, id)
        self.value = 0
        
    
    #edits this object
    def set(self, value): 
        command = self.click() #clicks
        str_value = str(value) # transforms the value to str
        for i in str_value: #sends all key pressed
            command.append("key 1 " + str(ord(i)) + " 0 ; ") 
            command.append("key 0 " + str(ord(i)) + " 0 ; ")   
        command.append("key 1 10 0 ;") # press enter
        command.append("key 0 10 0 ;")
        self.value = value # @TODO   
        return command
    
    #increments the lowest amount from the value of a number
    def increment(self):
        command = []
        command.append("mouse " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ;")
        command.append("motion " + str(self.x+1) + " " + str(self.y) + " 0 ;")
        command.append("mouseup " + str(self.x+1) + " " + str(self.y) + " 1 0 ;")
        self.value = 0 # @TODO
        return command
    
    #decrements the lowest amount from the value of a numbe
    def decrement(self):
        command = []
        command.append("mouse " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ;")
        command.append("motion " + str(self.x+1) + " " + str(self.y+2) + " 0 ;")
        command.append("mouseup " + str(self.x+1) + " " + str(self.y+2) + " 1 0 ;")
        self.value = 0 # @TODO
        return command
    
    
    
    #aux static function to debug this class
    @staticmethod
    def debug():
        o = Number(10, 10, 0)
        print o.set(20)
        print o.increment()
        print o.decrement()    