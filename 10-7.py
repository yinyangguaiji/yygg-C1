print('Please enter two number')
active =  True
while active:
    try:
        number1 = int(input('First number:'))
        number2 = int(input('Second number:'))
    except ValueError:
        print('Please enter number,not other things!')
    else:
        print(number1 + number2)
        active = False
