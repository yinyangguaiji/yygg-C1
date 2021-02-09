class User():
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name + ','+ self.age +','+ self.nationality)
    def greet_user(self):
        print('Hello,' + self.first_name.title() + ' '+ self.last_name)
class Admin(User):
    def __init__(self,first_name,last_name,age,nationality):
        super().__init__(first_name,last_name,age,nationality)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        print(self.privileges)
admin = Admin('Zhang','San','20','China')
admin.show_privileges()
