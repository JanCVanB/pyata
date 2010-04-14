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
from box_classes.number import *




#variable that stores the port number
RCV_PORT = 3001 
#variable that stores the port number
SND_PORT = 3000 
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
class Communication(): 
    
    #constructor
    def __init__(self, nogui): 
        self.snd_port = int(SND_PORT) 
        self.rcv_port = int(RCV_PORT)
        self.snd_socket = socket(AF_INET, SOCK_STREAM)
        self.rcv_socket = socket(AF_INET, SOCK_STREAM)
        self.host = HOST 
        self.thread=RemotePd(nogui)
        self.canvas = "pd-new"
        self.rcv = ""
            
    #connecting to pd
    def init_pd(self): 
        print "initializing server.pd..."
        self.thread.start()
        sleep(5)
        
        try: 
            self.snd_socket.connect((self.host, self.snd_port))
            self.rcv_socket.bind((self.host, self.rcv_port))
            self.rcv_socket.listen(1) 
            self.rcv, addr = self.rcv_socket.accept()
            self.init_pyata()
            print "connecting with pd"
            return True
        except error, err: 
            print "Error connecting to %s:%d: %s" % (self.host, self.snd_port, err) 
            return False
    
    #init some socket variables
    def init_pyata(self):
        Number.init_socket(self.rcv)
    
    
    #sending a command to pd
    def send_pd(self, commands):
        try:
            message = ""
            
            if isinstance(commands, (str, unicode)):
                message = self.canvas + " " + commands + " "
            else:
                for cmd in commands:
                    message += self.canvas + " " + cmd + " "
        
            self.snd_socket.send(message)
            return True
        except error, err: 
            print "Error sending message %s : %s" % (message, err) 
            return False


    #closing connection
    def finish_pd(self): 
        temp = "killall pd"
        p = Popen(temp, shell=True)
        
        self.snd_socket.close() 
        self.rcv_socket.close()
        print "closing connection with pd" 

        
    #setting the canvas to where the messages are going
    def set_canvas(self, canvas):
        self.canvas=canvas
        
    #aux static function to debug this class
    @staticmethod
    def debug():
        c = Communication(False)
        c.init_pd()
        sleep(5)
        c.finish_pd()
        
        

        