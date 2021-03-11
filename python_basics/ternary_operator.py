#ternary operator
def ternary_operator(is_friend = False):
  """cond_is_true if codition else cond_if_false"""
  can_message = "message allowed" if is_friend else "not allowed to message"
  return (print(can_message))