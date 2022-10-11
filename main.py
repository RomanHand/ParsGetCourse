<<<<<<< HEAD
=======
import requests
from bs4 import BeautifulSoup
import csv

link = "https://school-operator.getcourse.ru/cms/system/login?"
url = "https://school-operator.getcourse.ru/teach/control"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

data = {
    "action": "processXdget",
    "xdgetId": "99945",
    "params[action]": "login",
    "params[url]": "https://school-operator.getcourse.ru/cms/system/login?required=true",
    "params[email]": "o.bezgina@vladlink.ru",
    "params[password]": "77db2d",
    "params[null]": "",
    "params[object_type]": "cms_page",
    "params[object_id]": "-1",
    "requestTime": "1665374322",
    "requestSimpleSign": "e4fce222bdb6d03ea49539180eff0b8e",
    "gcSession": "{\"id\":3345798427,\"last_activity\":\"2022-10-10+06:58:45\",\"user_id\":241468848,\"utm_id\":null}",
    "gcVisit": "{\"id\":6069096345,\"sid\":3345798427}",
    "gcVisitor": "{\"id\":3507077287,\"sfix\":1}",
    "gcSessionHash": "16bd073cf39add0fa03f20f4bbb281f4"
}

session = requests.Session()
responce = session.post(link, data=data, headers=headers).text


def get_html(url, params=None):
    r = session.get(url, headers=headers, params=params).text
    # print(r)
    return r


html = get_html(url)

razdel = "https://school-operator.getcourse.ru/teach/control/stream/view/id/"
ids = ["566691142", "566948246", "605050184", "629267033", "637559614"]

fak1 = []
fak2 = []
fak3 = []

faks = []


def parspegas():
    i = 0
    while i < 5:
        page = get_html(razdel + ids[i])
        soup = BeautifulSoup(page, 'html.parser')
        items = soup.find_all('div', class_='link title')
        i = i + 1
        a = 0
        arr = len(items)
        print(items[0].get('href'))
        print(arr)
        while a < arr:
            faks.append(items[a].get('href'))
            a = a + 1





def parsuroki():
    a = len(faks)
    i = 0
    while i < a:
        page = get_html("https://school-operator.getcourse.ru" + faks[i])
        soup = BeautifulSoup(page, 'html.parser')
        items1 = soup.find('h2', class_='lesson-title-value')
        # items2 = soup.find('h1').get('href')
        # items3 = soup.find('iframe').get('src')
        print(items1.get_text())
        fak1.append(str(items1.get_text()))
        i = i + 1



def zapis():
    a = len(fak1)
    i = 0
    while i < a:
        itog = str(fak1[i])
        i = i + 1
        with open("out.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(
                itog
            )

#parspegas()
#parsuroki()
fak1 = ['абаоба', 'абоба2']
zapis()
>>>>>>> c488201 (add main.py)

