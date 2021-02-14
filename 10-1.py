with open('learning_python.txt') as project:
    project1 = project.read()
    print(project1)
    print('')
with open('learning_python.txt') as project:
    for line in project:
        print(line.rstrip())
with open('learning_python.txt') as project:
    lines = project.readlines()
    print('')
for line in lines:
    print(line.rstrip())
