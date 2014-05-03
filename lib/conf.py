# coding: utf-8

import os
import ConfigParser
from fabric.api import env
import commands
import util
import json

inifile = ConfigParser.SafeConfigParser()
inifile_dir = os.path.join(os.path.dirname(__file__), '../../')
inifile_path = os.path.join(inifile_dir, 'fabfile.ini')
inifile.read(inifile_path)

def complement_path(path):
    if path == '':
        return None
    if path.find('/') == 0:
        return path
    else:
        return os.path.join(inifile_dir, path)

# common
chef_repo_path = complement_path(inifile.get('common', 'chef_repo_path'))
tmp_cookbooks_paths = inifile.get('common', 'cookbooks_paths')
tmp_cookbooks_paths = tmp_cookbooks_paths.replace(' ', '').split(',')
cookbooks_paths = []
for path in tmp_cookbooks_paths:
    cookbooks_paths.append(complement_path(path))

node_path      = complement_path(inifile.get('common', 'node_path'))
role_path      = complement_path(inifile.get('common', 'role_path'))
http_proxy     = inifile.get('common', 'http_proxy')
https_proxy    = inifile.get('common', 'https_proxy')

# chefric
chefric_path       = complement_path(inifile.get('chefric', 'chefric_path'))
log_dir_path       = os.path.join(chefric_path, inifile.get('chefric', 'chefric_log'))
chef_rpm           = inifile.get('chefric', 'chef_rpm')
if chef_rpm != '':
    chef_rpm_path      = os.path.join(chefric_path, chef_rpm)
else:
    chef_rpm_path = None

tmp_chef_rpm       = inifile.get('chefric', 'tmp_chef_rpm')


if not os.path.exists(log_dir_path):
    os.mkdir(log_dir_path)

env.is_proxy = False
def is_proxy(option=None):
    if option and option.find('p') != -1:
        if http_proxy and https_proxy:
            env.is_proxy = True
            return True
        else:
            raise Exception('http_proxy is bad')
    else:
        env.is_proxy = False
        return False

env.is_server = False
def is_server(option=None):
    if option and option.find('s') != -1:
        env.is_server = True
        return True
    else:
        env.is_server = False
        return False

def get_initial_json(host):
    return {
        'name': host,
        'run_list': []
    }

# chef-solo用のjson文字列を作成し、返します
# chef-serverのjsonをマージすると、chef-soloで利用できなくなるため必要
def get_jsonstr_for_chefsolo(host=None):
    host_json = util.load_json(host)
    json_obj = {
        'run_list': host_json['run_list'],
    }
    return json.dumps(json_obj)


