
##########################################################
##########################################################
# description: abstract class that represents a generic Symbol box
#
# autor: jeraman
# date: 13/04/2010
##########################################################
##########################################################

from box    import *
from socket import *



#number class itself
class Symbol (Box):
    #constructor
    def __init__(self, x, y, id):
        Box.__init__(self,x, y, id)
        self.text = "symbol"
        rcv = ""
    
    @staticmethod
    def init_socket(r):
        Symbol.rcv = r
        
    #get the value from pd
    def get_value(self):
        temp = Number.rcv.recv(32)
        self.text = temp[:(len(temp)-2)]
        return self.value
        
    
    #edits this object
    def set(self, text): 
        command = self.click() #clicks
        for i in text: #sends all key pressed
            command.append("key 1 " + str(ord(i)) + " 0 ; ") 
            command.append("key 0 " + str(ord(i)) + " 0 ; ")   
        command.append("key 1 10 0 ;") # press enter
        command.append("key 0 10 0 ;")
        #self.value = self.get_value()
        return command
    
    
    #aux static function to debug this class
    @staticmethod
    def debug():
        o = Symbol(10, 10, 0)
        print o.set("mesa")