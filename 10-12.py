import json
filename = 'favourite_number.json'
try:
    with open(filename) as obj:
        number1 = json.load(obj)
except FileNotFoundError:
    number = input("What's your favourite name?\n")
    with open(filename,'w') as obj:
        json.dump(number,obj)
        print('I will remember your favourite number.')
else:
    print("I know your favourite number is " + number1)
