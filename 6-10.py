favourite_numbers = {'Bill':['6','8'],
                     'Shylock':['5','16'],
                     'Benny':['6','4','8'],
                     'John':['22','22'],
                     'Morax':['666','777','888']
                     }
for name,numbers in favourite_numbers.items():
    print(name + "'s favourite numbers are: ",end='')
    for number in numbers:
        print(number + ' ',end='')
    print('\n')
