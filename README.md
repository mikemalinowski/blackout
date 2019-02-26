# Blackout

## Installation
You can either download or clone this repo, or alternatively you can
install this module using pip:

```commandline
pip install blackout
```
## Overview
Blackout is a small micro-module which makes it easier to completely
forget packages. This is particularly useful when working with packages
made up of multiple sub-modules.

And example might be:

    /site-packages/foo/__init__.py
    /site-packages/foo/bar.py

If bar.py has a function called foo() within it, and we change that
function then it is not enough to reload foo, we must specifically
reload foo as well as foo.bar. 

When working with packages with any modules this can be time consuming
and problematic - particularly when developing within a host which is
persistent.

Blackout helps, because we can unload the package in its entirety in 
a single line using:

    ```blackout.drop('foo')```

This will remove any hold to foo as well as any submodules of foo. In this 
case we can simply call ```import foo``` again, knowing that everything
within that package is being loaded fresh.

## Compatability

This has been tested under Python 2.7.13 and Python 3.6.6 under both Windows and Ubuntu.
