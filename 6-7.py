person1 = {'first_name':'Sherlock','last_name':'Holmes','age':'71','city':'London'}
person2 = {'first_name':'William','last_name':'Shakespeare','age':'52','city':'London'}
person3 = {'first_name':'Albert','last_name':' Einstein','age':'76','city':'Ulm'}
people = [person1,person2,person3]
for person in people:
    for information in person.keys():
        print(information + ':' + person[information])
    print('\n')

