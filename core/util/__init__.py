# coding: utf-8

from base import genconfig, sync_fablib, upload, client  # noqa

genconfig.__doc__ = """
Generate config.
"""

sync_fablib.__doc__ = """
Sync fablib.
"""

upload.__doc__ = """
Upload fabric-repo to swift.
"""

client.__doc__ = """
Download fabric-repo from swift, and run $ fab setup:local.
"""
