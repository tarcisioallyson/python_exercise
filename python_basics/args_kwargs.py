def args_kwargs():
  #Rule: params, *args, default params, **kwargs
  def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
      total += items
    return sum(args) + total
  
  print(super_func('Tony',1,2,3,4,5, num1=5, num2=10))