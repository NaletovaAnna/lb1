from PIL import Image, ImageFilter
def z1():
    a = Image.open('1.jpg')
    a.show()

    widht, height = a.size
    format = a.format
    mode = a.mode

    print('Ширина: ', widht)
    print('Высота: ', height)
    print('Формат: ', format)
    print('цветовая модель: ', mode)

def z2():
    a = Image.open('2.jpg')
    a.show()

    b = a.resize((a.width // 3, a.height // 3))
    b.show()

    c = b.rotate(90)
    c.save('2.1.jpg')
    c.show()

    d = b.transpose(Image.FLIP_LEFT_RIGHT)
    d.save('2.2.jpg')
    d.show()

def z3():
    a = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for x in a:
        with Image.open(x) as b:
            b.load()
            c = b.filter(ImageFilter.SMOOTH)
            d = c.filter(ImageFilter.FIND_EDGES)
            d.show()
            d.save("3.1" + x)

def z4():
    a = Image.open("3.jpg")
    b = Image.open("он добрый.png")

    b = b.resize([100, 100])
    a.paste(b, [350, 400], mask = b)
    a.show()

z4()