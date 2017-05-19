# pyata

> a Library that allows you to use Pure Data inside Python!

Authored by Jerônimo Barbosa ([@jeraman](https://github.com/jeraman))

Recovered by Jan Van Bruggen ([@JanCVanB](https://github.com/JanCVanB))
from https://code.google.com/archive/p/pyata

[Demo on Youtube:](https://www.youtube.com/watch?v=Xpwb48qjxds)

[![Pyata Demo (using Pure Data inside Python)](https://img.youtube.com/vi/Xpwb48qjxds/0.jpg)](https://www.youtube.com/watch?v=Xpwb48qjxds)


## Description

Pyata (Pyatã, from Tupi or yet, Py.thon + Pure D.ata) is a simple cross-plataform open-source Python module that allows people to use [Pure Data](http://puredata.info/) (aka, Pd) just like an API. In other words, it is an abstraction to Pd, that can be used for doing a lot of things that Pd can do, but without manipulate the Pd interface in a direct way.

It was developed using a technique known as "[dynamic patching](https://jeraman.info/2009/03/22/how-to-use-pure-data-as-a-api/)", which is based on dynamic creation of Pd objects realized through sockets, achieved through [FUDI protocol](http://wiki.puredata.info/en/FUDI). This means, for example, that we can create a [osc~ 440] object sending to Pd a specific message through sockets.

So what basically the library does is to receive the commands given by users, transforming them into the equivalent message. These messages are sent to Pd, that processes them like they were a patch running inside Pd (a virtual patch), generating results. After that, these results are reloaded again into the Python program, that allows it to be always updated according the “virtual patch”.

Before starting, please, read [the tutorial](https://github.com/JanCVanB/pyata/blob/master/wiki/Getting_Started.md)!


## Functionalities

This version includes:
- Boxes creation, edition and remotion (object, number, comments, symbols and messages)
- Get from Pd the state of any box (number of inlet/outlets, the ID of each box on Patch, values of numbers and symbols)
- Connection management (connect and disconnect boxes)
- Basic operations (copy, paste, duplicate, cut, save)


## Recovery steps

All credit to Dominik Dorn ([@domdorn](https://github.com/domdorn)) and [his Google Code recovery instructions](https://dominikdorn.com/2016/05/how-to-recover-a-google-code-svn-project-and-migrate-to-github/) (thanks! :)

```sh
# Download the svn dump'ed repo
$ wget https://storage.googleapis.com/google-code-archive-source/v2/code.google.com/<PROJECTNAME>/repo.svndump.gz

# Unzip
$ gunzip repo.svndump.gz

# Create the repo
$ svnadmin create /tmp/testgc

# Restore it
$ svnadmin load /tmp/testgc/ < repo.svndump

# Launch a local svn daemon
$ svnserve --foreground -d

# In another terminal, clone your repo now using git svn
# (optionally create a authors file for correctly mapping to git usernames)
$ git svn --stdlayout -A authors.txt clone svn://localhost/tmp/testgc/

# Go into the cloned repo
$ cd testgc/

# Add the upstream github repo
$ git remote add origin https://github.com/<USERNAME>/<PROJECTNAME>.git

# Push it
$ git push --set-upstream origin master
```

I did not need any of the following steps to recover pyata.

```sh
# Till now, we only have the trunk / master branch.
# Get atlassians svn-migration-scripts.jar from https://bitbucket.org/atlassian/svn-migration-scripts/downloads
$ wget https://bitbucket.org/atlassian/svn-migration-scripts/downloads/svn-migration-scripts.jar

# Run the scripts and expect the suggested actions
$ java -Dfile.encoding=utf-8 -jar svn-migration-scripts.jar clean-git

# If you like what you see (usually you do..), perform the actions
$ java -Dfile.encoding=utf-8 -jar svn-migration-scripts.jar clean-git --force

# After this i had a branch structure like this:
$ git branch -a
* master
  remotes/origin/0.2_nate
  remotes/origin/0.4_gblaszczyk
  remotes/origin/jsf-1.2-spring-2
  remotes/origin/jsf-1.2-spring-3
  remotes/origin/jsf-2.0-spring-2
  remotes/origin/jsf-2.0-spring-3
  remotes/origin/master
  remotes/origin/site
  remotes/origin/site@17
  remotes/origin/tags/0.1
  remotes/origin/tags/0.3_jsf-1.2-spring-2
  remotes/origin/tags/0.3_jsf-1.2-spring-3
  remotes/origin/tags/0.3_jsf-2.0_spring-2
  remotes/origin/tags/0.3_jsf-2.0_spring-3
  remotes/origin/tags/0.5
  remotes/origin/trunk

# Checkout each branch (except tags and trunk) and push it
$ for i in `git branch -r | grep -v 'tags\|trunk' `; do git checkout ${i/origin\// }; git push;  done

# Push the branches
$ git push --all origin

# Checkout each tag and create a tag with the same name
$ for i in `git branch -r | grep 'tags'`; do git checkout $i; git tag ${i/origin\/tags\// }; done

# Push the tags
$ git push --tags origin
```
