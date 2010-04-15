##########################################################
##########################################################
# description: abstract class that represents any Connection between boxes
#
# autor: jeraman
# date: 15/04/2010
##########################################################
##########################################################

from box import *
from time       import *  


memory_connections = []


    


def search_connections (c):
    i=0   
    #seraching for a specific box in memory
    for connections in memory_connections:
        if c==connections:
            return i
        i+=1
    
    #return -1 if not
    if i==len(memory_connections):
        return -1
    else:
        return i



class Connection:
    canvas = "pd-new "
    snd = ""

    #constructor
    def __init__(self, box_orig, outlet, box_dest, inlet):
        self.box_orig = box_orig
        self.outlet = outlet
        self.box_dest = box_dest
        self.inlet = inlet
        self.create()
        
        
    #creates a connection in Pd    
    def create(self):
        b1 = search_box(self.box_orig)
        b2 = search_box(self.box_dest)

        if (b1 > -1) & (b2 > -1):
            #get the state before inserting the connection
            self.snd.send_pd("pd-new menusave ; ")
            sleep(0.1)
            t1 = self.snd.get_file()

            #try to build the connection
            command = Connection.canvas + "connect " + str(b1) + " " + str(self.outlet) + " " + str(b2) + " " + str(self.inlet) + " ; "
            Connection.snd.send_pd(command)
            
            #get the state after insertin the connection
            self.snd.send_pd("pd-new menusave ; ")
            sleep(0.1)
            t2 = self.snd.get_file()
            
            print t1
            print
            print "------"
            print
            print t2
            
            #verifies if changed
            if t1 != t2:
                memory_connections.append(self)
                print "funfou"
            else:
                print "nao funfou"

    
    #creates a connection in Pd    
    def delete(self):
        b1 = search_box(self.box_orig)
        b2 = search_box(self.box_dest)
        if (b1 > -1) & (b2 > -1):
            #get the state before removing the connection
            self.snd.send_pd("pd-new menusave ; ")
            sleep(0.1)
            t1 = self.snd.get_file()
            
            #try to remove the connection
            command = Connection.canvas + "disconnect " + str(b1) + " " + str(self.outlet) + " " + str(b2) + " " + str(self.inlet) + " ; "
            Connection.snd.send_pd(command)
            
            #get the state after removing the connection
            self.snd.send_pd("pd-new menusave ; ")
            sleep(0.1)
            t2 = self.snd.get_file()
            
            print t1
            print
            print "------"
            print
            print t2
            
            #verifies if changed
            if t1 != t2:
                i=search_connections(self)
                #print i
                memory_box.pop(i)
                print "funfou!"
            else:
                print "nao funfou!"
            
            
        
    #method that sets the canvas
    @staticmethod
    def set_canvas(nc):
        Connection.canvas = nc
        
    #method that sets the sender
    @staticmethod
    def set_sender(s):
        Connection.snd = s
        
        