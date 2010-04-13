##########################################################
##########################################################
# description: class that handles pd communication
#
# important: based on Frank Barknecht script at:
# http://markmail.org/message/ohuwrz77hwo3bcwp#query:python%20pdsend+page:1+mid:ybdc6esbu7q53otu+state:results 
#
# autor: jeraman
# date: 06/04/2009
##########################################################
##########################################################

#import sys
from threading  import *
from socket     import *
from time       import *  
from subprocess import *





#variable that stores the port number
PORT = 3000 
#variable that stores the host
HOST = "localhost"
#replace this to where pd file is (COMPLETY DIRECTORY)
PD_DIR = ""
#replace this to where server.pd is (COMPLETY DIRECTORY)
SERVER_DIR = "/home/jeraman/workspace/pyata/src"






# a thread class that we're gonna use for calling the server.pd patch
class RemotePd ( Thread ):
    def __init__(self, nogui):
       Thread.__init__(self)
       self.nogui = nogui
        
    def run ( self ):
       if self.nogui:
           temp = "cd %s && pd -nogui %s/server.pd" %(PD_DIR, SERVER_DIR)
       else:
           temp = "cd %s && pd %s/server.pd" %(PD_DIR, SERVER_DIR)
       self.p = Popen(temp, shell=True)




#communication class
class Communication(socket): 
    
    #constructor
    def __init__(self, nogui): 
        self._port = int(PORT) 
        self._host = HOST 
        self.thread=RemotePd(nogui)
        socket.__init__(self)
        self.canvas = "pd-new"
            
    #connecting to pd
    def init_pd(self): 
        print "initializing server.pd..."
        self.thread.start()
        sleep(5)
        
        try: 
            self.connect((self._host, self._port)) 
            print "connecting with pd"
            return True
        except error, err: 
            print "Error connecting to %s:%d: %s" % (self._host, self._port, err) 
            return False
    
    #sending a command to pd
    def send_pd(self, command):
        try:
            command = canvas + " "+command+ ";" 
            self.send(command)
            return True
        except error, err: 
            print "Error sending message %s : %s" % (command, err) 
            return False


    #closing connection
    def finish_pd(self): 
        temp = "killall pd"
        p = Popen(temp, shell=True)
        
        self.close() 
        print "closing connection with pd" 

        
    #setting the canvas to where the messages are going
    def set_canvas(self, canvas):
        self.canvas=canvas
        
        
if __name__ == '__main__':
    c = Communication(False)
    c.init_pd()
    sleep(5)
    c.finish_pd()
        