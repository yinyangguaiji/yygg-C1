class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is open')
class Icecreamstand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Chocolate Icecream','Strawberry icecream','Banana icecream']
    def print_icecream(self):
        for icecream in self.flavors:
            print(icecream)
icecreamstand = Icecreamstand('BBLice','icecream')
icecreamstand.print_icecream()
