import json

def z1():
    with open('продукты.json') as f:
        data = json.load(f)


    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z2():
    with open('продукты.json') as f:
        data = json.load(f)


    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()


    new_product = {}
    new_product['name'] = input("Введите название нового продукта: ")
    new_product['price'] = float(input("Введите цену нового продукта: "))
    new_product['weight'] = float(input("Введите вес нового продукта: "))
    new_product['available'] = bool(input("Есть ли новый продукт в наличии? (True/False): "))


    data['products'].append(new_product)

    with open('продукты.json', 'w') as f:
        json.dump(data, f)


    print("\nОбновленное содержимое файла products.json:")
    with open('продукты.json', 'r') as f:
        print(f.read())

def z3():  #?????
    d = {}

    with open("словарь.txt", "r") as file:
        for line in file:
            en_w = line.split("-")[0].strip()
            ru_ws = line.split("-")[1].strip().split(',')
            for i in ru_ws:
                i = i.strip()
                if i in d.keys():
                    d[i] = d[i] + ", " + en_w
                else:
                    d[i] = en_w

    with open("словарь.txt", "w") as file:
        for i in sorted(d.keys()):
            file.writelines(f"{i} - {d[i]}\n")

z3()