def while_loops():
  i= 0
  while i < 10:
    print(i+1)
    i+=1
  else:
    print('done with all the work')
  
  print('')
  my_list = [1,2,3]
  for i in my_list:
    print(i)
  
  print('')
  i = 0
  while i < len(my_list):
    print(my_list[i])
    i+=1
  
  print('')
  while True:
    response = input('Say something: ')
    if response == 'bye':
      break