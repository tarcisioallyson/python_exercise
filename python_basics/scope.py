def scope():
  #Rules: 1 - start with local;
  #       2 - Parent local?
  #       3 - Global
  #       4 - built in python functions
  a = 1
  
  def parent():
    def confusion():
      return sum
    return confusion()

  print(parent())
  print(a)