try:
    with open('cat.txt') as cat:
        cat1 = cat.read()
except FileNotFoundError:
    print('The file "cat.txt" is no be found.')
else:
    print(cat1)
try:
    with open('dog.txt') as dog:
        dog1 = dog.read()
except FileNotFoundError:
    print('The file "dog.txt" is not be found.')
else:
    print(dog1)

