# import requests
# from bs4 import BeautifulSoup

# url = requests.get('https://www.theguardian.com/football/premierleague/table')
# data = BeautifulSoup(url.content,'html.parser')
# data1 = data.find('table',class_='table table--football table--league-table table--responsive-font table--striped')
# data1 = data1.find('tbody').find_all('tr')
# data.findChild()
# for x in data1:
#     print(x.contents[0])
# # print(data1)


# import os
# os.system('shutdown /s /t 1')

from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.theguardian.com/football/premierleague/table')
data = BeautifulSoup(url.content,'html.parser')
data.findChild('')

data1 = data.find('div',class_='u-cf').div.table.tbody.findChildren('tr',recursive=False)
for x in data1:
    # print(x.findChild('td',{'class':'table-column--sub'}))
    print(x.findChild('td',{'class':'table-column--main'}).a.text.strip())
    # print(x)
    
