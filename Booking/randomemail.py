import json
import random
import os


count = int(input("How many emails do you need:"))
accounts = []
for i in range(count):
    with open("userData.json", "r") as file:
        userData = json.load(file)
    first_names = userData["first_name"]
    last_names = userData["last_name"]

    first_name = first_names[random.randint(0, len(first_names)-1)].lower()
    last_name = last_names[random.randint(0, len(last_names)-1)].lower()
    email = f'{first_name}{last_name}3799@gmail.com'
    if not os.path.exists('accounts.json'):
        with open('accounts.json', 'w') as file:
            json.dump([], file)
    with open('accounts.json', 'r') as file:
        accounts = json.load(file)
    accounts.append({"first_name" : first_name, "last_name" : last_name, "email" : email, "registered"  : False})

    with open('accounts.json', 'w') as file:
        json.dump(accounts, file)