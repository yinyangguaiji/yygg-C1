try:
    with open('cat.txt') as cat:
        cat1 = cat.read()
except FileNotFoundError:
    pass
else:
    print(cat1)
try:
    with open('dog.txt') as dog:
        dog1 = dog.read()
except FileNotFoundError:
    pass
else:
    print(dog1)

