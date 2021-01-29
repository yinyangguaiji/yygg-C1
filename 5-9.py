users = ['Shylock','admin','Bill','Sandy','Albert']
if users:
    user = input("User's name:")
    if user in users:
        if user == 'admin':
            print('Hello admin, would you like to see astatus report?')
        else:
            print('Hello ' + user + ', thank you for logging in again.')
    else:
        print('You are not our user.')
else:
    print('We need to find some users!')
