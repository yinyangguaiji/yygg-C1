number1 = input('Please enter two number\nFirst number:')
number2 = input('Second number:')
try:
    numberF = int(number1)
    numberC = int(number2)
except ValueError:
    print('Please enter number,not other things!')
else:
    print(numberF + numberC)
