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

    

#connects two generic boxes
def connect (b1, outlet, b2, inlet):
    Connection(b1, outlet, b2, inlet)


#disconnect a connection
def disconnect(b1, outlet, b2, inlet):
    #procura a conexao
    i = search_connections(b1, 0, b2, 0)
    #se realmente existir
    if i>-1:
        memory_connections[i].delete()


#searchs a generic connection
#def search_connections (c):
#    i=0   
#    #seraching for a specific box in memory
#    for connections in memory_connections:
#        if c==connections:
#            return i
#        i+=1
    
    #return -1 if not
#    if i==len(memory_connections):
#        return -1


#searchs a generic connection
def search_connections (b1, o, b2, i):
    i=0   
    #seraching for a specific box in memory
    for c in memory_connections:
        if (b1==c.box_orig) & (o==c.outlet) & (b2==c.box_dest) & (i==c.inlet):
            return i
        i+=1
    
    #return -1 if not
    if i==len(memory_connections):
        return -1


    

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
            command = Connection.canvas + "menusave ; "
            Connection.snd.send_pd(command)
            sleep(0.01)#alterar o tempo de espera aqui
            t1 = self.snd.get_file()

            #try to build the connection
            command = Connection.canvas + "connect " + str(b1) + " " + str(self.outlet) + " " + str(b2) + " " + str(self.inlet) + " ; "
            Connection.snd.send_pd(command)
            
            #get the state after insertin the connection
            command = Connection.canvas + "menusave ; "
            Connection.snd.send_pd(command)
            sleep(0.01)#alterar o tempo de espera aqui
            t2 = self.snd.get_file()
            
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
            command = Connection.canvas + "menusave ; "
            Connection.snd.send_pd(command)
            sleep(0.01) #alterar o tempo de espera aqui
            t1 = self.snd.get_file()
            
            #try to remove the connection
            command = Connection.canvas + "disconnect " + str(b1) + " " + str(self.outlet) + " " + str(b2) + " " + str(self.inlet) + " ; "
            Connection.snd.send_pd(command)
            
            #get the state after removing the connection
            command = Connection.canvas + "menusave ; "
            Connection.snd.send_pd(command)
            sleep(0.01) #alterar o tempo de espera aqui
            t2 = self.snd.get_file()
            
            #verifies if changed
            if t1 != t2:
                i=search_connections(self.box_orig, self.outlet, self.box_dest, self.inlet)
                memory_connections.pop(i)
                print "funfou"
            else:
                print "nao funfou"
            
            
        
    #method that sets the canvas
    @staticmethod
    def set_canvas(nc):
        Connection.canvas = nc
        
    #method that sets the sender
    @staticmethod
    def set_sender(s):
        Connection.snd = s
        
        