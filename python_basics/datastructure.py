def datastructure():
  name = input('What\'s your name? ')
  password = input('Digit your password: ')

  password_length = len(password)
  hidden_password = '*' * password_length

  print(
      f'{name}, your password {hidden_password} is {password_length} letters long'
  )