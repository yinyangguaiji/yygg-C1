class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)
    def open_restaurant(self):
        print('The restaurant is open')
    def set_number_served(self,number):
        self.number_served = number
        return self.number_served
restaurant = Restaurant('boloboloda','pasta','30')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
restaurant.number_served = 30
print(restaurant.number_served)
print(restaurant.set_number_served('15'))
