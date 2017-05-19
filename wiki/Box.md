Describes the Box class and its methods

Box
===

this is one of the most important class in Pyata. though you cannot
create a object of this class, it is super class of all others boxes
classes: [Object](Object.md), [Number](Number.md),
[Message](Message.md), [Symbol](Symbol.md) and [Comment](Comment.md).
so, as you may expect, all methods described in this document can be
used in any of the classes above.

Methods
-------

### Move

moves the object in the patch to a new x, y.

~~~~ {.prettyprint}
move(new_x, new_y)
~~~~

where:

> *new*x\_ = new x position of the box;

> *new*y\_ = new y position of the box;

### Verify Inlets

verify how many inlets owns the box.

~~~~ {.prettyprint}
verify_inlets()
~~~~

### Verify Outlets

verify how many outlets owns the box.

~~~~ {.prettyprint}
verify_outlets()
~~~~

### Select

selects the box

~~~~ {.prettyprint}
select()
~~~~

### Unselect

unselects the box

~~~~ {.prettyprint}
unselect()
~~~~

### Shift Select

selects the box. if more than one box is selected, after calling this
method, all of them will still be selected.

~~~~ {.prettyprint}
shift_select()
~~~~

### Shift Unselect

unselects the box. if more than one box is selected, after calling this
method, all of them (but the one you called shift\_unselect) will still
be selected.

~~~~ {.prettyprint}
shift_unselect()
~~~~

### Delete

deletes the Box from the patch.

~~~~ {.prettyprint}
delete()
~~~~


