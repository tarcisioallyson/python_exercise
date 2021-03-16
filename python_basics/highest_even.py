def highest_even(li):
  '''Return highest even number'''
  even = []
  for items in li:
    if items % 2 == 0:
      even.append(items)
  return max(even)

#numbers = [22,32,55,66,34,8,12,23]
#print(highest_even(numbers))