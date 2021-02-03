prompt = '请输入您的年龄\n'
act = True
while act:
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 0:
            print('数据错误')
        elif age < 3:
            print('您免费')
        elif 3 <= age <= 12:
            print('您的票价是10美元')
        else:
            print('您的票价是15美元')
    else:
        act = False
