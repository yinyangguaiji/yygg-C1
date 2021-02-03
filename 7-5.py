while True:
    number = input('请输入您的年龄\n')
    if number == 'quit':
        break
    else:
        age = int(number)
        if age < 0:
            print('数据错误')
        elif age < 3:
            print('您免费')
        elif 3 <= age <= 12:
            print('您的票价是10美元')
        else:
            print('您的票价是15美元')
