
from box_classes.box import *
from box_classes.object import *
from box_classes.number import *
from box_classes.message import *
from box_classes.comment import *
from box_classes.symbol import *
from communication import *

#file created just for debug tests



if __name__ == '__main__':
    print "ei man"
    pd = Communication(False)
    pd.init_pd()
   
    obj1 = Object(10, 10, "dac~")
    obj2 = Object(100, 100, "dac~")
    c1 = Comment(150, 50, "upa!")
    m1 = Message(200, 20, "ground control")
    n1 = Number(100, 20)
    s1 = Symbol(20, 100)
    sleep(2)
    
    pd.send_pd("pd-new editmode 1 ; ")
    obj1.move(50, 50)
    obj1.click()
    m1.edit("to Major Tom!")
    sleep(2)
    
    obj1.unselect()
    obj1.edit("osc~")
    c1.edit("agora vc esta vendo a edicao de objetos!")
    obj2.select()
    sleep(2)

    pd.send_pd("pd-new editmode 0 ; ")  
    s1.set("vc esta vendo os numeros e symbols")
    n1.set(20)
    n1.decrement()
    n1.decrement()
    n1.increment()
    sleep(2)
    
    
    
    
    
    pd.finish_pd()
   