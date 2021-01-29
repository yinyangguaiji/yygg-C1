ages = input("The man's age is:")
age = int(ages)
if age < 0:
    print('Are kidding me?')
elif 0 <= age < 2:
    print('This man is just a baby.')
elif 2 <= age < 4:
    print('This man is a toddler.')
elif 4 <= age < 13:
    print('This man is a child.')
elif 13 <= age < 20:
    print('This man is a teenager.')
elif 20 <= age < 65:
    print('This man is a adult.')
else:
    print('This man is an old man')
