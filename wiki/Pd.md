Describes the Pd class and its methods

Pd
==

an important class in Pyata. if you want to use this library, is this
class you must import at first. you also must have a instance of this
class inside your program. it will be responsible to communicate with
the Pd process and has all the methods related to basic Pd
functionalities (copy, paste, save, and others).

Methods
-------

### Init

initializes the library stuff and the Pd itself. must be called before
doing any kind of thing with Pyata.

~~~~ {.prettyprint}
init()
~~~~

### Quit

finishes the library stuff and the Pd itself. must be called when your
program is about to end.

~~~~ {.prettyprint}
quit()
~~~~

### Save

saves the modifications in the patch.

~~~~ {.prettyprint}
save()
~~~~

### Clear

clears the patch.

~~~~ {.prettyprint}
clear()
~~~~

### Get Box List

returns the boxes available in Pd.

~~~~ {.prettyprint}
get_box_list()
~~~~

### Get Connection List

returns the connections available in Pd.

~~~~ {.prettyprint}
get_connection_list()
~~~~

### Copy

copies the selected boxes (if you want to select/unselect a box, just
check select()/unselect() method, from Box class).

~~~~ {.prettyprint}
copy()
~~~~

### Paste

pastes boxes available in transfer board.

~~~~ {.prettyprint}
paste(new_x, new_y)
~~~~

where:

> *new*x\_ = the x position where you want to paste the objects;

> *new*y\_ = the y position where you want to paste the objects;

### Duplicate

duplicates the selected boxes (if you want to select/unselect a box,
just check select()/unselect() method, from Box class).

~~~~ {.prettyprint}
duplicate(new_x, new_y)
~~~~

where:

> *new*x\_ = the x position where you want to duplicate the objects;

> *new*y\_ = the y position where you want to duplicate the objects;

### Selectall

selects all the objects available in Pd.

~~~~ {.prettyprint}
selectall()
~~~~


