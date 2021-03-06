# coding: utf-8

from oslo_config import cfg

CONF = cfg.CONF


test_opts = [
    cfg.StrOpt('user',
               default='fabric',
               help='user for test'),
    cfg.StrOpt('password',
               default='fabric',
               help='password for test'),
    cfg.ListOpt('clusters',
                default=[
                    'centos7/',
                    'ubuntu14/',
                ],
                help='clusters for test'),
    cfg.DictOpt('fablib',
                default={},
                help='fablib for test'),
]

CONF.register_opts(test_opts, group='test')
