places = {}
act = True
while act:
    name = input("What's your name?\n")
    place = input('If you could visit one place in the world,where would you go?\n')
    places[name] = place
    repead = input('Would you like to let another person respond? (yes/ no)')
    if repead == 'no':
        break
for name,place in places.items():
    print(name.title() + ' want to go to ' + place.title() + '.')
                 
    
