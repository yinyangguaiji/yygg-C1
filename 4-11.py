print('[4-1-1]')
pizzas = ['Assorted Pizza','Vegetable Pizza','Hawaii Pizza']
for pizza in pizzas :
    print(pizza)
print('[4-1-2]')
pizzas = ['Assorted Pizza','Vegetable Pizza','Hawaii Pizza']
for pizza in pizzas :
    print('I like '+pizza+'!')
print('[4-1-3]')
pizzas = ['Assorted Pizza','Vegetable Pizza','Hawaii Pizza']
for pizza in pizzas :
    print('I like '+pizza+'!')
print('I rally love pizza!\n')
friend_pizzas = pizzas[:]
pizzas.append('Chicken Pizza')
friend_pizzas.append('Mushroom pizza')
print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
