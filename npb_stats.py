import requests
from bs4 import BeautifulSoup
import re

teams = ["g","t","d","db","c","s","h","m","e","l","f","b"]
url = "https://npb.jp/bis/2020/stats/id"
for team in teams:
    for p in ["b","p"]:
        print(team)
        url = "https://npb.jp/bis/2020/stats/id{}1_{}.html".format(p,team)
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'html.parser')
        players = soup.find_all('tr',{'class':'ststats'})
        if p == "b":
            for player in players:
                stats = player.find_all("td")
                for stat in stats:
                    # print(stat.text)
                    pass
        else:
            for player in players:
                stats = player.find_all("td")
                for stat in stats:
                    print(stat.text)