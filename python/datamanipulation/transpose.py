import copy
import json
import numbers
from typing import List


def list_nested_keys(data: dict, parent_key='', sep='__') -> list:
    keys = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            keys.extend(list_nested_keys(v, new_key, sep=sep))
        # Filtering out "middle layer" keys that don't have values
        # Thing to note: isinstance(False, numbers.Number) --> True
        elif v or isinstance(v, numbers.Number) or isinstance(v, list):
            keys.append(new_key)
    return keys


def flatten(data: dict, res: dict={}, parent_key='', sep='__'):
    res = copy.deepcopy(res)
    for k, v in data.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            res = flatten(v, res, parent_key=new_key)
        else:
            res[new_key] = v
    return res


def transpose(data: List[dict], parent_sep='__', transpose_key='transposed') -> dict:
    """Only supports nested dictionaries. If a value is a list of dictionaries, it will not be flattened."""
    # Get keys:
    keys = set().union(*[list_nested_keys(d, sep=parent_sep) for d in data])
    print(keys)
    # Initializing dicitonary
    res = {}
    for k in keys:
        res[k] = []
    for d in data:
        a = flatten(d, sep=parent_sep)
        # Fill missing keys with None
        for k in keys:
            if k not in a.keys():
                a[k] = None
        for k in res.keys():
            res[k].append(a[k])
    res[transpose_key] = True
    return res


def expand(data: dict, sep='__', transpose_key='transposed') -> List[dict]:
    """Expands a flattened dictionary of lists into a list of nested dictionaries."""
    # Assert that all the lists in the values are of the same length.
    del data[transpose_key]
    if data == {}:
        return []
    value_lengths = [len(x) for x in list(data.values())]
    assert max(value_lengths) == min(value_lengths)
    return [nullout_empty(nest_dict(dict(zip(data, x)), sep=sep)) for x in zip(*data.values())]


def nest_dict(flat_dict, sep='__'):
    nested_dict = {}
    for key, value in flat_dict.items():
        keys = key.split(sep)
        current_dict = nested_dict
        for i, k in enumerate(keys):
            if i == len(keys) - 1:
                current_dict[k] = value
            else:
                if k not in current_dict:
                    current_dict[k] = {}
                current_dict = current_dict[k]
    return nested_dict


def nullout_empty(dictionary: dict):
    """Removes nested dictionaries that only contain null values."""
    res = copy.deepcopy(dictionary)
    for k, v in dictionary.items():
        if isinstance(v, dict):
            res[k] = nullout_empty(v)
    if all(x is None for x in res.values()):
        return None
    return res


if __name__ == '__main__':
    a = [{'x': 1, 'y': 2, 'z': 3, 'i': {'a': 'a', 'b': [{'foo': 42, 'bar': 'universe'}, {'foo': 11, 'bar': 'hello'}], 'c': {'yo': 0.0, 'co': 99}}},
         {'x': 4, 'y': None, 'z': None, 'i': {'a': 'a', 'b': [{'foo': 51, 'bar': None}], 'c': None}},
         {'x': 0, 'y': 57, 'z': None, 'i': {'a': 'samwise', 'b': [], 'c': None}},
         {'x': 5, 'y': 6, 'z': None, 'i': {'a': 'e', 'b': [{'foo': None, 'bar': 'frodo'}, {'foo': 0.0, 'bar': 'world'}, {'foo': 94, 'bar': 'another'}], 'c': {'yo': 85, 'co': 9}}},
         {'x': 7, 'y': 8, 'z': 9, 'i': None}]
    r = {
        'transposed': True,
        'x': [1,4,0,5,7],
        'y': [2,None,57,6,8],
        'z': [3,None,None,None,9],
        'i__a': ['a','a','samwise','e',None],
        'i__b': [[{'foo':42,'bar':'universe'},{'foo':11,'bar':'hello'}],[{'foo':51,'bar':None}],[],[{'foo': None, 'bar': 'frodo'}, {'foo': 0.0, 'bar': 'world'}, {'foo': 94, 'bar': 'another'}], None],
        'i__c__yo': [0.0,None,None,85,None],
        'i__c__co': [99,None,None,9,None]
    }
    battery_status_failing = json.loads('[{"datetime": "2023-03-16T10:39:02.485273", "battery_id": 1, "voltage": 0.0, "state_of_health": 0, "state_of_charge": -99, "alarms": [false, false, false, false, false, false, false, false, false, false, false, false, false, false], "robot_id": "thorvald-056"}]')
    rec = expand(transpose(battery_status_failing))
    assert battery_status_failing == rec
    b = transpose(a)
    assert b == r
    c = expand(r)
    assert c == a
    d = {'x': 7, 'y': 0, 'z': 9, 'i': {'a': None, 'b': None, 'c': {'yo': None, 'co': None}}, 'a': {'foo': 0.0}}
    e = {'x': 7, 'y': 0, 'z': 9, 'i': None, 'a': {'foo': 0.0}}
    assert e == nullout_empty(d)

    f = {'transposed': True}
    g = []
    h = expand(f)
    assert h == g

    i = [{'x': 0, 'y': False}, {'x': 0, 'y': False}]
    j = {'x':[0,0],'y':[False,False],'transposed':True}
    assert transpose(i) == j
    assert expand(j) == i

    k = [{'a': [], 'b': 1},{'a':[], 'b': 2}]
    l = {'a': [[],[]], 'b':[1,2], 'transposed':True}
    m = expand(transpose(k))
    assert m == k
    
    print("OK!")

    for i in range(0, 100):
        with open('/home/bard/tmp_no_optimization.json', 'a+') as f:
            f.write(json.dumps(a))
        with open('/home/bard/tmp_optimized.json', 'a+') as f:
            f.write(json.dumps(b))
