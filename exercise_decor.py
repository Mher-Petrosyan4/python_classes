'''
Homework:
create class User: (username, password, email, age, phone)
In a json file store all user information as database
create class named PyRequest which will be initialised with:
headers: list, default []
authorization: True/False, default None
body: {}, default None
user: User obj, default None
class should have method called

loacal_login(username, password) : which updates self.user with user if one is found with given credentials if not updates with None: You should search for users in json file
create function get_user_info(request):
decorate it with login_required decorator:
the point of decorator is to check weather there is user inside request or not:
if there is user get_user_info function should return user all information if not should raise an error with message “401 Unauthorized request error”
implementation:
create PyRequest object.
ask user to provide username and password with input and call login function
 3. call get_user_info for the specific request
'''
import json


class User:
    list_of_users = []

    def __init__(self, username, password, email, age, phone):
        self.username = username
        self.password = password
        self.email = email
        self.age = age
        self.phone = phone
        self.list_of_users.append(self.user_dict())

    def user_dict(self):
        dict_ = {'username': self.username, 'password': self.password, 'email': self.email, 'age': self.age,
                 'phone': self.phone}
        return dict_

    @classmethod
    def json_converter(cls):
        with open('users_info.json', 'a') as json_file:
            json.dump(cls.list_of_users, json_file, indent=4)
        return json_file


def login_required(func):
    def inner(self, *args):
        try:
            result = func(self, *args)
        except Exception as err:
            result = f'{err} 401 Unauthorized request error'

        return result
    return inner


class PyRequest:
    list_ = User.list_of_users

    def __init__(self):
        self.headers = []
        self.authorization = None
        self.body = None
        self.user = None
        self.request = None

    def local_login(self):
        username = input('Enter you username: ')
        password = input('Enter you password: ')
        for dict_ in self.list_:
            if username == dict_['username'] and password == dict_['password']:
                self.user = dict_
                break
            else:
                self.user = None

    @login_required
    def get_user_info(self, request):
        if self.user['username'] == request:
            return self.user
        else:
            raise ValueError('No such username')


user_1 = User('Mher.Petrosyan', '12345', 'mherpetrosyan2@gmail.com', 26, '095753197')
user_2 = User('Hayk.Petrosyan', '6789', 'haykpetrosyan2@gmail.com', 28, '093753197')
user_3 = User('Erik.Danielyan', '101010', 'erik.danielyan@gmail.com', 27, '099999999')
print(User.list_of_users)
request_1 = PyRequest()
request_1.local_login()
print(request_1.get_user_info('Hayk.Petrosyan'))