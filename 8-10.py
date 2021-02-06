def shou_magicians(names):
    for name in names:
        print(name.title())
def make_great(names):
    g_names = []
    for name in names:
        name = 'the Great ' + name.title()
        g_names.append(name)
    return g_names
a = ['shylock','bill','benny']
shou_magicians(make_great(a))

    
        
