cities = {
    'Chengdu':{'country':'China',
             'population':'16 million 581 thousand',
             'fact':'safe and peacful'},
    'New_York':{'country':'America',
             'population':'8 million 510 thousand',
             'fact':'terrible and terrible'},
    'London':{'country':'Britain',
             'population':'8 million 900 thousand',
             'fact':'terrible'}
}
for city,information in cities.items():
    print(city + ':')
    for infor1,infor2 in information.items():
        print('\t' + infor1 + ':' + infor2)
    print('\t')
             
             
