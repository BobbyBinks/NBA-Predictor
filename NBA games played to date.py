import requests
from bs4 import BeautifulSoup
import re

# Make a request to the webpage
URL = "https://www.basketball-reference.com/leagues/NBA_2024_games-december.html"

#for n in range(0,len(URL)):
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
month_tables = soup.find_all('table', {"id":"schedule"})

list=[]
for i in month_tables[0].find_all('td'):
    for table in i.find_all('a',href=True):
        if re.match("^/boxscores/",table["href"]):
            list.append(str(table['href']))
print([x for x in list if x.startswith('/boxscores/')])
