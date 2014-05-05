# coding: utf-8

# library for test

import os
from fabric.api import env
import commands
import util, conf
import json

def get_searched_nodes_obj(host_pattern):
    hosts = []
    for host in util.get_expanded_hosts(host_pattern):
        hosts.append({
                "name": host,
                "chef_environment": "_default",
                "json_class": "Chef::Node",
                "automatic": {},
                "normal": {},
                "chef_type": "node",
                "default": {},
                "override": {},
                "run_list": [ "" ]
            })

    return { "results": len(hosts), "rows": hosts }


def get_searched_nodes(host_pattern):
    return json.dumps(get_searched_nodes_obj(host_pattern))
