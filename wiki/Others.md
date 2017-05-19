Describes some global functions that are not inside any class

Others
======

In this section are listed some global functions that can be acessed any
time during the execution of the program.

Functions
---------

### Connect

Connects two boxes.

~~~~ {.prettyprint}
connect(box_orig, outlet, box_dest, intlet)
~~~~

where:

> *box*orig\_ = the box where the connections starts;

> *outlet* = number of the outlet from *box*orig\_ where the connection
> starts;

> *box*dest\_ = the box where the connections ends;

> *inlet* = number of the inlet from *box*orig\_ where the connection
> ends;

### Disconnect

Disconnects two boxes.

~~~~ {.prettyprint}
disconnect(box_orig, outlet, box_dest, intlet)
~~~~

where:

> *box*orig\_ = the box where the connections starts;

> *outlet* = number of the outlet from *box*orig\_ where the connection
> starts;

> *box*dest\_ = the box where the connections ends;

> *inlet* = number of the inlet from *box*orig\_ where the connection
> ends;

### Search Box

Searchs the indice (ID) of a specific box in memory. If there's no box
with the given specification, the function returns -1.

~~~~ {.prettyprint}
search_box(box)
~~~~

where:

> *box* = box to be searched

### Search Connection

Searchs the indice (ID) of a specific connection in memory. If there's
no connection with the given specification, the function returns -1.

~~~~ {.prettyprint}
search_connection(box_orig, outlet, box_dest, intlet)
~~~~

where:

> *box*orig\_ = the box where the connections starts;

> *outlet* = number of the outlet from *box*orig\_ where the connection
> starts;

> *box*dest\_ = the box where the connections ends;

> *inlet* = number of the inlet from *box*orig\_ where the connection
> ends;
