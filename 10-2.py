with open('learning_python.txt') as project:
    project1 = project.read()
    project2 = project1.replace('Python','C++')
    print(project2)

