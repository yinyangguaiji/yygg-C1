current_users = ['Shylock','admin','Bill','Sandy','Albert']
current_users1 = []
for current_user in current_users:
    current_users1.append(current_user.lower())
new_users = ['Shylock','BILL','Rosalia','Lilia','Terri']
for new_user in new_users:
    if new_user.lower() in current_users1:
        print('The user name "' + new_user + '" already in use,please enter a different user name.')
    else:
        print('This user name "' + new_user + '" has not been used.')
