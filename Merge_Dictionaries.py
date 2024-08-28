
def merge_dictionaries(dict1, dict2):
  dict3 = {}
  dict3.update(dict1)
  for name,value in dict2.items():
    if name not in dict3:
      dict3[name] = value
  return dict3



dictionary1 = {
  '1': 'lol',
  '2': 'heh',
  '3': 'waa'
}

dictionary2 = {
  '4': 'ugg',
  '5': 'dugg',
  '6': 'mug'
}

dictionary3 = merge_dictionaries(dictionary1, dictionary2)

print(dictionary3)