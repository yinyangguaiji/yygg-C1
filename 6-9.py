favourite_places = {'Bill':['Shenzhen','Shanghai'],
                     'Shylock':['Chengdu',"Ya'an"],
                     'Benny':['Guilin','Beijing','Chongqing']
                     }
for name,places in favourite_places.items():
    print(name + "'s favourite places :",end='')
    for place in places:
        print(place + '   ',end='')
    print('\n')

