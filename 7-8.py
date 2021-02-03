sandwich_orders = ['Sandwich1','Sandwich2','Sandwich3']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print('I made your ' + sandwich + '.')
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)


