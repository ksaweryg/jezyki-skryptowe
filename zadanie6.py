import copy
di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
di_copied = copy.deepcopy(di)

di['four'][0] = 'cztery'

print(di)

print(di_copied)