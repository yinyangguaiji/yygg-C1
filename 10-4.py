with open('guest_book.txt','a') as project1:
    while True:
        name = input('Please input your name:')
        if name == 'quit':
            break
        else:
            project1.write(name + '\n')
            print('Welcome' + name)
