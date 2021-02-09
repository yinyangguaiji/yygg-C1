class User():
    def __init__(self,first_name,last_name,age,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.login_attempts = 0
    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name + ','+ self.age +','+ self.nationality)
    def greet_user(self):
        print('Hello,' + self.first_name.title() + ' '+ self.last_name)
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user = User('zhang','san','19','China')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
