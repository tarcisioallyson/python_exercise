def tricky_counter():
  my_list = [1,2,3,4,5,6,7,8,9,10]

  counter = 0
  for item in my_list:
    print(item)
    counter += item
  print(f'the sum is {counter}')