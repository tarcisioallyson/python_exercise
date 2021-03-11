def iterables():
  """ iterable -> list, dict, tuple, set, string
      iterate -> one by one check each item in the collection"""
  user = {
    'name': 'Golem',
    'age': 5000,
    'can_swim': False
  }

  for item in user.items():
    print(item)
  
  for item in user.values():
    print(item)

  for item in user.keys():
    print(item)

  #unpacking
  for key, value in user.items():
    print(key, value)
