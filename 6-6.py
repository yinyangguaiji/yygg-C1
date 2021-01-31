names = ['bill','shylock','benny','wendy']
done_names = {'bill':'a','benny':'b'}
for name in names:
    if name in done_names:
        print(name.title() + ' thank you for participating in our survey.')
    else:
        print(name.title() + ' please participate in our servey.')
