def fuctions():
  #parameters
  def say_hello(name='Darth Vader', emoji='😈'):
    print(f'Hello {name}{emoji}')

  #positional arguments
  say_hello('Emily','😜')

  #keywords arguments
  say_hello(name='Dan', emoji='🥳')

  #default parameters
  say_hello()