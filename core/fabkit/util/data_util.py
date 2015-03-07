# coding: utf-8

from types import DictType, ListType, StringType, IntType
from fabkit import databag, env


def decode_cluster_map():
    for cluster_name, data in env.cluster_map.items():
        env.cluster_map[cluster_name] = decode_data(data)


def decode_data(data, origin_data=None):
    if not origin_data:
        origin_data = data

    if type(data) is DictType:
        for key, value in data.items():
            data[key] = decode_data(value, origin_data)

    if type(data) is ListType:
        data = [decode_data(value, origin_data) for value in data]

    if type(data) is StringType:
        splited_value = data.split('${')
        if len(splited_value) > 1:
            result = ''
            for value in splited_value:
                splited_key = value.split('}', 1)
                if len(splited_key) > 1:
                    key = splited_key[0]
                    if key.find('#') == 0:
                        tmp_keys = key[1:].split('.')
                        tmp_data = origin_data
                        for tmp_key in tmp_keys:
                            if tmp_key.isdigit():
                                tmp_key = int(tmp_key)
                            tmp_data = tmp_data[tmp_key]

                        tmp_data = decode_data(tmp_data, origin_data)
                        if type(tmp_data) is StringType:
                            result += tmp_data + splited_key[1]
                        elif type(tmp_data) is IntType:
                            result += str(tmp_data) + splited_key[1]
                        else:
                            return tmp_data

                    else:
                        result += databag.get(key) + splited_key[1]
                else:
                    result += value

            return result

    return data