# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://python.iamroot.eu/tutorial/index.html")
# page = response.content
# soup = BeautifulSoup(page, "html.parser")

# a = soup.find_all("a")
# count = 0

# for i in a:
#     if len(i.get("href")) >= 30:
#         count += 1

# print(count)

#copyright.html
#https://www.python.org/psf/donations/
#https://docs.python.org/3/bugs.html
#https://www.sphinx-doc.org/

import requests
from bs4 import BeautifulSoup

response = requests.get("https://python.iamroot.eu/tutorial/index.html")
page = response.content
soup = BeautifulSoup(page, "html.parser")

wrapper = soup.find("div", id = "the-python-tutorial")
p = wrapper.find_all("p")
count = 0

for i, el in enumerate(p):
    if i <= 3:
        word_list = el.text.split(" ")
        for word in word_list:
            word = list(word)
            if word[0] == "a" or word[0] == "A":
                print(word[0])
                count += 1

print(count)
    
    # if len(i.get("href")) >= 30:
    #     count += 1

# print(count)