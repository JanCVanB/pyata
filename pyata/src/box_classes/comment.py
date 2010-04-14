
##########################################################
##########################################################
# description: abstract class that represents a comment box
#
# autor: jeraman
# date: 14/04/2010
##########################################################
##########################################################


from box_classes.box import *

#number class itself
class Comment (Box):
    #constructor
    def __init__(self, x, y,text, id=-1):
        Box.__init__(self,x, y, id)
        self.text = text
        command = Box.canvas + "text " + str(self.x) + " " + str(self.y) + " " + self.text + "; "
        Box.snd.send_pd(command)
    
    #edits this object
    def edit(self, text):
        self.unselect() #unselects
        self.click() #selects this
        
        command = ""
        for i in text: #sends all key pressed
            command += Box.canvas + "key 1 " + str(ord(i)) + " 0 ; " 
            command += Box.canvas + "key 0 " + str(ord(i)) + " 0 ; "        
        Box.snd.send_pd(command)
        self.unselect() #unselects this
        self.text = text    
        
        
    #aux static function to debug this class
    @staticmethod
    def debug():
        box = Comment(20, 20, "alo!", 0)
        print box.edit("ola")