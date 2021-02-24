import vk_api
import time
from random import choice
from string import ascii_uppercase
import json

class GroupCreator:
    def __init__(self, account, vk_session=None):

        self.account = account
        self.vk_session = vk_api.VkApi(account[0], account[1])
        self.vk_session.auth()

    def createGroups(self, login):
        self.login = login
        vk = self.vk_session.get_api()
        for i in range(0, 2):
            group_name = ''.join(choice(ascii_uppercase) for i in range(6))
            group_description = ''.join(choice(ascii_uppercase) for i in range(12))
            result = vk.groups.create(title=f"{group_name}", 
                description=f"{group_description}", type="group")
            data[self.login]["groups"].append(result["id"])
            with open('./data.json', "w") as update:
                json.dump(data, update, ensure_ascii=False, indent=4)
            time.sleep(30)
            

def do():
    with open('./accounts.txt', 'r') as read_accounts:
        accounts = read_accounts.readlines()
        if ":" not in accounts[-1]:
            del accounts[-1]
        print(accounts)    
    for item in accounts:
        try:
            format_data = item.replace("\n", '')
            login = f"{format_data.split(':')[0]}"
            password = f"{format_data.split(':')[1]}"
            
            data[login] = {"login": login, "password": password, "groups": []}
        
            GroupCreator(format_data.split(':')).createGroups(login)
        except Exception:
            continue

def return_data():
    return data

if __name__ == "__main__":
    data = {}
    do()
    print("Первый цикл прошел")
    time.sleep(7200)
    do()
    return_data()

    
    
        







