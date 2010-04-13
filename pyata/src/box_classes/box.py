
##########################################################
##########################################################
# description: abstract class that represents any Pd box
#
# autor: jeraman
# date: 13/04/2010
##########################################################
##########################################################


#aux function to debug this class
def debug(self):
    box = Box(20, 20, 0)
    print box.move(10, 10)
    print box.select()
    print box.unselect()
    print box.shift_select()
    print box.shift_unselect()

class Box:
    #constructor of the class
    def __init__(self, x, y, id):
        self.x=x
        self.y=y
        self.id=id
        self.inlet= self.get_number_inlets()
        self.outlet=self.get_number_outlets()
    
    #clicks inside this obj
    def click(self):
        command  = "mouse " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        command += "mouseup " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        return command
        
    # method that moves this box   
    def move (self, new_x, new_y):
        command  = "mouse " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        command += "motion " + str(new_x) + " " + str(new_y) + " 0 ; "
        command += "mouseup " + str(new_x) + " " + str(new_y) + " 1 0 ; "
        self.x=new_x
        self.y=new_y
        return command
    
    #method that selects this box
    def select (self):
        command  = "mouse " + str(self.x-1) + " " + str(self.y-1) + " 1 0 ; "
        command += "motion " + str(self.x+1) + " " + str(self.y+1) + " 0 ; "
        command += "mouseup " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        return command
    
    #method that unselects this box
    def unselect(self):
        command  = "mouse " + str(self.x-1) + " " + str(self.y-1) + " 1 0 ; "
        command += "mouseup " + str(self.x-1) + " " + str(self.y-1) + " 1 0 ; "
        return command
    
    #method that selects this box with key shift pressed
    def shift_select (self):
        command = "key 1 0 0 ; "
        command  = "mouse " + str(self.x-1) + " " + str(self.y-1) + " 1 0 ; "
        command += "motion " + str(self.x+1) + " " + str(self.y+1) + " 0 ; "
        command += "mouseup " + str(self.x+1) + " " + str(self.y+1) + " 1 0 ; "
        command += "key 0 0 0 ;"
        return command
    
    #method that unselects this box with key shift pressed
    def shift_unselect(self):
        command = "key 1 0 0 ; "
        command += "mouse " + str(self.x-1) + " " + str(self.y-1) + " 1 0 ; "
        command += "mouseup " + str(self.x-1) + " " + str(self.y-1) + " 1 0 ; "
        command += "key 0 0 0 ;"
        return command
    
    
    # @TODO gets the number of inlet of the object
    def get_number_inlets (self):
        return 0
    
    # @TODO gets the number of inlet of the object
    def get_number_outlets (self):
        return 0
        
    


