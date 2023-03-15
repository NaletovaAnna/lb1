def z4():
  import random
  a = 0
  b = 0
  while a != 3:
      x = random.randint(1, 9)
      y = random.randint(1, 9)
      res = x + y
      otvet = input(str(x) + "+" + str(y) + "=")

      if otvet == str(res):
          print ("Молодец :)")
          a += 1
      else:
          print("Ой, ты ошибся :(")
          b += 1

      if b == 3:
          break
  print("Всего правильных ответов: ", a)
z4()