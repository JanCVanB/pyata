Installing Pyata

i'm still working in a better way to install the library (a distutil
installer). untill this, you will not really install pyata, but just use
its source in your program. this is how you can get it.

before we start...
==================

you should have already Pure Data installed on your machine. check how
to install it on:

-   [mac osx](http://en.flossmanuals.net/PureData/InstallingOSX)
-   [windows](http://en.flossmanuals.net/PureData/InstallingWindows)
-   [linux
    (ubuntu)](http://en.flossmanuals.net/PureData/InstallingUbuntu)

-   you should be able to run it via command line. you can see how to
    achieve it [here](http://en.flossmanuals.net/PureData/StartingPD).

using!
======

it's very easy to use Pyata. this tutorial will show how to get started
with it, step by step...

1 - download...
---------------

to download Pyata, you need to check out it from svn.

**OSX/Linux**

1.  open a terminal.
2.  make or change into the directory where you want the Pyata
    sourcecode.
3.  run the following command to download Pyata from the svn repository:

> `svn checkout http://pyata.googlecode.com/svn/trunk/ pyata-read-only`

**Windows**

you will need an svn client, like
[Tortoise](http://tortoisesvn.tigris.org/).

2 - configure...
----------------

after that, you have to configure Pyata. for that you must:

1.  among the downloaded files, you'll find "config.properties" file.
    open it.
2.  in the beggining of it, you will find an important variable:
    PD\_DIR, that stores where your original pd application is (that one
    you are able to run using a terminal). update its value (you must
    put the entire path!!!) and run the "example.py" file. if you have
    no errors, everything should be fine and configured!

3 - ... and run!
----------------

now, everything should be fine and you can try Pyata without problems!
keep on, reading the [tutorial](Getting_Started.md)!
