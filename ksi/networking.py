import requests

# data = {
#     'username': 'Loskarlos',  
#     'password': 'JednohoDneOvladnuKSI',
# }

# response = requests.post('https://losoviny.iamroot.eu/part_one_login', data=data)
# print(response.json()) 

# headers = {'Authorization': 'Bearer 5860c8f1-e6c9-402c-80cb-7c1c275ad9a1'}

# response = requests.get('https://losoviny.iamroot.eu/part_one', headers=headers)
# print(response.text)

#NevERgONnALEtYOuDown

import requests
from time import sleep


data = {
    'username': 'Loskarlos',  
    'password': 'JednohoDneOvladnuKSI',
}

session = requests.Session()
post_response = session.post('https://losoviny.iamroot.eu/part_two_login', data=data)
sleep(2)

get_response = session.get('https://losoviny.iamroot.eu/part_two')
print(get_response.text) # stránka s Karlíkovim tajným receptom na sušienky

# import requests


# data = {
#     'username': 'Loskarlos',
#     'password': 'JednohoDneOvladnuKSI',
# }

# response_login = requests.post(
#     'https://losoviny.iamroot.eu/part_one_login', data=data
# )

# print(response_login.json())

# token = response_login.json()["auth_token"]
# headers = {'Authorization': f'Bearer {token}'}
# response_logged = requests.get(
#     'https://losoviny.iamroot.eu/part_one', headers=headers
# )

# print(response_logged.json())

# import requests


# data = {
#     'username': 'Loskarlos',
#     'password': 'JednohoDneOvladnuKSI',
# }

# session = requests.Session()
# response_login = session.post(
#     'https://losoviny.iamroot.eu/part_two_login', data=data
# )

# print(session.cookies)

# response_logged = session.get(
#     'https://losoviny.iamroot.eu/part_two', headers=headers
# )

# print(response_logged.json())