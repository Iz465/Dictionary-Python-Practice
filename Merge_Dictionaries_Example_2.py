dict1 = {'a': 1, 'b': 2}

dict2 = {'b': 3, 'c': 4}


def merge_dictionaries(dict1, dict2):
  dict3 = dict1.copy()
  for key,value in dict2.items():
    if key in dict3:
       dict3[key] += value
    else:
        dict3[key] = value
  print(dict3)


merge_dictionaries(dict1,dict2)
