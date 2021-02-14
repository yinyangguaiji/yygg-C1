import json
number = input("What's your favourite name?\n")
filename = 'favourite_number.json'
with open(filename,'w') as obj:
    json.dump(number,obj)
with open (filename) as obj:
    f_number = json.load(obj)
    print('I know your favourite number!It is ' + f_number)
