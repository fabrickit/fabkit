# coding: utf-8

from base import databag  # noqa

databag.__doc__ = """
access databag

## Args
    option (str): action option
        set: set databag

## Examples
```
$ fab databag:set,test/database.password,dbpass
```
"""
