def first_gui():
  picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
  ]

  image = ""
  i=0
  while i < len(picture):
      for item in picture[i]:
          if item == 0:
              image += " "
          else:
              image += "*"
      image+='\n'
      i+=1
  print(image)