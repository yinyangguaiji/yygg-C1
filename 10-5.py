with open('reasons.txt','a') as project1:
    print('Why do you like programming?')
    while True:
        reason = input('')
        if reason == 'quit':
            break
        else:
            project1.write(reason + '\n')
