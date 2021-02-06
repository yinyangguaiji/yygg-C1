def make_car(manufacturer,model,**parts):
    car = {}
    car['manufacturter'] = manufacturer
    car['model'] = model
    for part,things in parts.items():
        car[part] = things
    return car
print(make_car('subaru','outback',colour='bule',tow_package=True))
