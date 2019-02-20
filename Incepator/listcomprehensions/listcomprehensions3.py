#creating a list from a dictionary
dct = {'one': 1, 'two': 2, 'three':3}
lst = [[k,v] for k, v in dct.items()]
print(lst)