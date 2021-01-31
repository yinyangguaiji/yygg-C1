pet1 = {'master_name':'Bill','pet_type':'cat'}
pet2 = {'master_name':'Shylock','pet_type':'dog'}
pet3 = {'master_name':'Benny','pet_type':'bird'}
pets = [pet1,pet2,pet3]
for pet in pets:
    for information in pet.keys():
        print(information + ':' + pet[information])
    print('\n')
          
