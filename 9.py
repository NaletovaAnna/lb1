from PIL import Image, ImageFilter
import os

def z1():
    a = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    count = 0
    for x in a:
        count += 1
        b = Image.open(x)
        c = b.filter(ImageFilter.FIND_EDGES)
        c.show()
        try:
            os.mkdir(c, Oo777)
        except:
            pass
        c.save("1.1" + x)

def z2():
    a =["1.gif", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    count = 0
    for x in a:
        if x.endswith('.jpg'):
            count += 1
            b = Image.open(x)
            c = b.filter(ImageFilter.FIND_EDGES)
            c.show()
            try:
                os.mkdir(c, Oo777)
            except:
                pass
            c.save("2.1" + x)

def z3():


z2()