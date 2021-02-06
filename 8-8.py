def make_album(name,album,number=''):
    singer = {}
    singer['name'] = name
    singer['album'] = album
    if number:
        singer['number of album'] = number
    return singer
print("(You can enter 'q' at any time to quit)")
while True:
    name = input("Please input the shinger's name:\n")
    if name == 'q':
        break
    album = input('And his/her album:\n')
    if album == 'q':
        break
    number = input("If you want to add the number of the singer's album,please input it,or press 'Enter' to continue.\n")
    if number == 'q':
        break
    result = make_album(name,album,number)
    print(result)
    print('')
