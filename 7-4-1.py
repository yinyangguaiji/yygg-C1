prompt = '请输入您要添加的配料\n'
things = ''
while things != 'quit':
    things = input(prompt)
    if things != 'quit':
        print('我们会在披萨中添加' + things)

