
from box_classes.object import *
from communication import *

#file created just for debug tests

if __name__ == '__main__':
    pd = Communication(False)
    pd.init_pd()
    
    command = "editmode 1;"
    pd.send_pd(command);
    
    obj1 = Object(10, 10, "dac~", 0)
    command = "obj " + str(obj1.x) + " " + str(obj1.x) + " " + obj1.label + ";"
    print command
    pd.send_pd(command)
    sleep(2)
    
    #obj2 = Object(20, 20, "dac~", 0)
    #command = "obj " + str(obj2.x) + " " + str(obj2.x) + " " + obj2.label + ";"
    #print command
    #pd.send_pd(command)
    #sleep(2)
    
    command = obj1.move(100, 100)
    print command
    pd.send_pd(command)
    sleep(2)
    
    command = obj1.unselect()
    print command
    pd.send_pd(command)
    sleep(2)

    #command = obj2.select()
    #print command
    #pd.send_pd(command)
    #sleep(2)
    
    command = obj1.edit("osc~")
    print command
    pd.send_pd(command)
    sleep(5)
    
    
    
    
    pd.finish_pd()