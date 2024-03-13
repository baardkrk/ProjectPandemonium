"""
Exploring dictionaries and the filter function
"""

import json

d = {
    'r2': [[32, 32, 'noe']],
    'r1': [[32, 32, 'noe'], [42, 42, 'annet']],
    'r3': [[32, 32, 'noe'], [42, 42, 'annet'], [52, 52, 'igjen']]
}


print(json.dumps(d, indent=4))
print('===============')

d = dict(filter(lambda x: len(x[1]) <= 2, d.items()))
print(json.dumps(d, indent=4))
