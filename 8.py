from PIL import Image, ImageDraw, ImageFont
def z1():
   a = Image.open('котик.jpg')
   a.show()
   b = a.crop((150, 350, 450, 650))
   b.show()
   b.save('котик с тортиком.jpg')

def z2():
   a = {"23 февраля": "23.jpg", "День рождения": "др.jpg", "14 февраля": "14.jpg"}
   print("У нас есть открытки к таким праздникам: 23 февраля, День рождения, 14 февраля")
   b = input("Открытка к какому празднику вас интерисует? ")

   if b in a:
      x = Image.open(a[b])
      x.show()
   else:
      print("У нас нет подходящей картинки :(")

def z3():
   x = Image.open('котик с тортиком.jpg')
   a = input("Напишите, кого вы хотите поздравить с днем рождения в именительном падеже: ")

   font = ImageFont.truetype("calibri.ttf", 15)
   drawer = ImageDraw.Draw(x)
   drawer.text((15,15), a + ", поздравляю с Днем рождения!", font=font, fill='red' )

   x.show()
   x.save('др.png')


z3()