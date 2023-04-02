import json
import requests


class MyUser:

    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email


    def __str__(self):
        return f'User id = {self.id}  name = {self.name}  username = {self.username} E-mail = {self.email}'



responce = requests.get("https://jsonplaceholder.typicode.com/users")
if 300 > responce.status_code >= 200:
    users = responce.json()
    search_name = input("Enter your name for search : ")
    # users1 = json.loads(users)   
    user_found = False
    for user in users:
        user_find = MyUser(user["id"],user["name"],user["username"],user["email"])
        if user_find.name == search_name:
            user_found = True
            print(user_find)
            break
        else:
            del user_find
    if not user_found:
        print(" user not found !")
else:
    print(f'responce from the site is = {responce.status_code}  for https://jsonplaceholder.typicode.com/users')        
    