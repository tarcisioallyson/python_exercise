def exercise_log_op(is_magician = True, is_expert = False):
  #check if magician AND expert: "you are a master magician"
  #check if magician but not expert: "at least you're getting there"
  #if you're not magician: "you need magic powers"

  if is_magician and is_expert:
    print("you are a master magician")
  elif is_magician and not is_expert:
    print("at least you're getting there")
  else:
    print("you need magic powers")
  #another way to check if you're not magician
  #elif not is_magician:
  #  print("you need magic powers")