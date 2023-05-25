def z1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):

            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")


        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    x = input("Введите название ресторана :")
    y =input("Введите название кухни")
    res = Restaurant(x,y)


    res.open_restaurant()
    res.describe_restaurant()



def z2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    restaurant1 = Restaurant("Банкай", "азиатскую")
    restaurant2 = Restaurant("Фьюче Симпл", "европейскую")
    restaurant3 = Restaurant("Осторожно, тут вкусно!", "русскую")

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()
def z3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}. Рейтинг: {self.rating}")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")

    restaurant1 = Restaurant("Банкай", "азиатскую", 4.7)
    restaurant2 = Restaurant("Фьюче Симпл", "европейскую", 4.8)
    restaurant3 = Restaurant("Осторожно, тут вкусно!", "русскую", 4.0)

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    restaurant1.update_rating(4.8)
    restaurant1.describe_restaurant()

z3()