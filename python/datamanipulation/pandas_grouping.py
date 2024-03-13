"""
Showing how to group pandas dataframes in different ways
"""

import numpy as np
import pandas as pd


letter_list = ['a', 'b']
data = pd.DataFrame([
  [1, ['a', 'c']],
  [2, ['b', 'd']],
  [3, ['a', 'c']],
  [4, ['a', 'c']],
  [5, ['b', 'd']],
  [6, ['b', 'c']],
  [7, ['a', 'd']],
  [8, ['b', 'c']],
  [9, ['b', 'c']]
], columns=['num', 'letters'])
ranges = pd.DataFrame([
  [2, 3, 'na'], 
  [4, 7, 'nb'], 
  [8, 10, 'nc']
], columns=['start', 'end', 'name'])

def intersection(lst, letter_list):
    return list(set(lst) & set(letter_list))[0]

data['letter'] = data['letters'].apply(lambda x: intersection(x, letter_list))

range_dict = {range(row['start'], row['end']+1): row['name'] for idx, row in ranges.iterrows()}
data['group'] = data['num'].apply(lambda x: next((v for k, v in range_dict.items() if x in k), np.nan))

data.index.rename('idx', inplace=True)
data.reset_index(inplace=True)
data.set_index(['group', 'idx'], inplace=True)

data.groupby('letter').apply(lambda x: x)
