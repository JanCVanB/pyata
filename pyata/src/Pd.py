

##########################################################
##########################################################
# description: main class that emulates Pd
#
# autor: jeraman
# date: 16/04/2010
##########################################################
##########################################################


from basic_classes.box import *
from basic_classes.object import *
from basic_classes.number import *
from basic_classes.message import *
from basic_classes.comment import *
from basic_classes.symbol import *
from basic_classes.connection import *
from communication import *


class Pd():
    #construtor
    def __init__(self):
        self.c = Communication(False)
    
    #inicializando a api
    def init(self):
        self.c.init_pd()
        self.clear()
        
    #finalizando a api
    def quit(self):
        self.clear()
        self.save()
        self.c.finish_pd()
        
    #salvando o arquivo
    def save(self):
        self.c.save_state(Box.canvas)
        
    #cleans the patch
    def clear(self):
        self.c.send_pd(Box.canvas + "clear ; ")
    
    #modifies the editmode. receives a boolean.
    def editmode(self, on_off):
        command = Box.canvas + "editmode 1 ; "
        if on_off==False:
            command += Box.canvas + "editmode 0 ; "
        self.c.send_pd(command)
    
    #modifies the dsp. receives a boolean
    def dsp(self, on_off):
        if on_off==False:
            self.c.send_pd("; pd dsp 0 ; ")
        else:
            self.c.send_pd("; pd dsp 1 ; ")
   
   #returns the memory available in Pd     
    def get_box_list(self):
        return memory_box
    
    #return the connections available in Pd
    def get_connection_list(self):
        return memory_connections
    