
##########################################################
##########################################################
# description: abstract class that manages all Pd object available
#
# autor: jeraman
# date: 14/04/2010
##########################################################
##########################################################

from box_classes.box import *
from box_classes.number import *
from box_classes.message import *
from box_classes.comment import *
from box_classes.symbol import *



class Box_Collection:
    #constructor
    def __init__(self):
        self.list=[]
    
    #creates a object box
    def create_object (self, x, y, label):
        self.list.append( Object(x, y, label) )