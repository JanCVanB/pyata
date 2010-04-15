
from basic_classes.box import *
from basic_classes.object import *
from basic_classes.number import *
from basic_classes.message import *
from basic_classes.comment import *
from basic_classes.symbol import *
from basic_classes.connection import *
from communication import *

#file created just for debug tests



if __name__ == '__main__':
    pd = Communication(False)
    pd.init_pd()
    
    o1 = Number(10, 10)
    o2 = Number(100, 100)
    connect(o1, 0, o2, 0)
    sleep(2)
    
    disconnect(o1, 0, o2, 0)
    sleep(2)
    
    connect(Number(50, 50), 0, o2, 0)
    for c in memory_connections:
        print c
    sleep(2)
    
    
    connect(o2, 0, Number(50, 50), 0)
    for c in memory_connections:
        print c
    sleep(2)
    
    
    connect(o2, 0, o1, 0)
    for c in memory_connections:
        print c
    sleep(2)
    
    
    pd.send_pd("pd-new clear ; ")
    pd.send_pd("pd-new menusave ; ")
    pd.finish_pd()
 
    
def teste4():
    pd = Communication(False)
    pd.init_pd()
    
    o1 = Number(10, 10)
    o2 = Number(100, 100)
    c1 = Connection(o1, 0, o2, 0)
    
    for c in memory_connections:
        print c
    sleep(2)

    print "---"
    
    cmt = Comment(50, 50, "teste")
    c2 = Connection(cmt, 0, o2, 0)
    for c in memory_connections:
        print c
    sleep(2)    
    
    print "---"
    c2.delete()
    for c in memory_connections:
        print c
    sleep(2)
    
    print "---"    
    c1.delete()
    for c in memory_connections:
        print c
    sleep(2)
    
    pd.send_pd("pd-new clear ; ")
    pd.send_pd("pd-new menusave ; ")
    pd.finish_pd()
    
    
    
    
    
def teste3():
    pd = Communication(False)
    pd.init_pd()
    
    o1 = Number(10, 10)
    o2 = Number(100, 100)
    pd.send_pd("pd-new menusave ; ")
    sleep(0.01)
    
    t1 = pd.get_file()
    
    Connection(o1, 0, o2, 0)
    pd.send_pd("pd-new menusave ; ")
    sleep(0.01)
    
    t2 = pd.get_file()
    
    if (t1 == t2):
        print "iguais"
    else:
        print "nao iguais"
    
    pd.send_pd("pd-new clear ; ")
    pd.send_pd("pd-new menusave ; ")
    pd.finish_pd()
    
def test2():
    print "ei man"
    pd = Communication(False)
    pd.init_pd()
    
    obj1 = Number(10, 10)
    obj2 = Object(100, 100, "dac~")
    wire1 = Connection(obj1, 0, obj2, 0)
    #print wire1.box_orig
    sleep(2)
    
    #pd.send_pd("pd-new editmode 1 ; ")
    wire1.delete()
    obj1.set("440")
    sleep(2)
    
    #obj1.set("660")
    sleep(2)
    pd.send_pd("pd-new editmode 1 ; ")
    pd.send_pd("pd-new editmode 0 ; ")
    obj1.set("660")
    #obj1.decrement()
    #obj1.edit("osc~ 660")
    sleep(2)
    
    ###########
    # BUGOU AI EM CIMA! OLHAR COM CALMA DEPOIS!
    ##############
    
    #pd.send_pd("pd-new connect 1 0 0 0; ")
    wire1.create()
    #pd.send_pd("pd-new editmode 0 ; ")
    #print wire1.box_orig
    sleep(2)
    
    
    
    
    
    pd.finish_pd()
    
    
    
def test1():
    pd = Communication(False)
    pd.init_pd()
   
    obj1 = Object(10, 10, "osc~")
    obj2 = Object(100, 100, "dac~")
    c1 = Comment(150, 50, "upa!")
    m1 = Message(200, 20, "ground control")
    n1 = Number(100, 20)
    s1 = Symbol(20, 100)
    wire1 = Connection(obj1, 0, obj2, 0)
    #wire2 = Connection(n1, 0, obj2, 0)
    
    for c in memory_connections:
        print c
    
    sleep(2)
  
  
    
    pd.send_pd("pd-new editmode 1 ; ")
    obj1.move(50, 50)
    obj1.click()
    wire1.delete()
    m1.edit("to Major Tom!")
    sleep(2)
    
    for c in memory_connections:
        print c
    
    obj1.unselect()
    #obj1.edit("osc~ 440")
    wire1.create()
    c1.edit("agora vc esta vendo a edicao de objetos!")
    obj2.select()
    sleep(2)
    
    for c in memory_connections:
        print c

    pd.send_pd("pd-new editmode 0 ; ")  
    s1.set("vc esta vendo os numeros e symbols")
    n1.set(20)
    n1.decrement()
    n1.decrement()
    n1.increment()
    sleep(2)
    
    pd.send_pd("pd-new editmode 1 ; ")
    c1.edit("como apagar objetos")
    obj1.delete()
    obj2.delete()
    #n1.delete()
    #m1.delete()
    #s1.delete()
    sleep(2)
    
    c1.edit("um exemplo de comofaze-los existir de novo!")
    obj1.create()
    obj2.create()
    #n1.create()
    #m1.create()
    #s1.create()
    sleep(2)
    
    #for box in memory_box:
    #    print box
    
    
    
    
    pd.finish_pd()
   