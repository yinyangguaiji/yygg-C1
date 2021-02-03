sandwich_orders = ['Sandwich1','Sandwich2','Sandwich3','pastrami','pastrami','pastrami']
print('Pastrami is sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
