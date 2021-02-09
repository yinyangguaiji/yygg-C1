class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is open')
restaurant = Restaurant('boloboloda','pasta')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant1 = Restaurant('sibalaxi','Chinese food')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('lamianyiku','hot pot')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('sigao','beef')
restaurant3.describe_restaurant()
