def check_duplicate():
  some_list = ['a','b','c','b','d','m','n','n']

  duplicate = []
  for item in some_list:
    if some_list.count(item) >= 2:
      if item not in duplicate:
        duplicate.append(item)
      else:
        pass
  print(duplicate)