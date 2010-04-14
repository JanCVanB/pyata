
##########################################################
##########################################################
# description: abstract class that represents a message box
#
# autor: jeraman
# date: 14/04/2010
##########################################################
##########################################################


from box_classes.box import *

#number class itself
class Message (Box):
    #constructor
    def __init__(self, x, y,text, id):
        Box.__init__(self,x, y, id)
        self.text = text
    
    #edits this object
    def edit(self, text):
        command = self.unselect() #unselects
        
        temp = self.click() #selects this
        for cmd in temp:
            command.append(cmd)
        
        for i in text: #sends all key pressed
            command.append("key 1 " + str(ord(i)) + " 0 ; ") 
            command.append("key 0 " + str(ord(i)) + " 0 ; ") 
        
        temp = self.unselect() #unselects this
        for cmd in temp:
            command.append(cmd)
        
        self.text = text    
        return command
    
    #aux static function to debug this class
    @staticmethod
    def debug():
        box = Message(20, 20, "alo!", 0)
        print box.edit("ola")