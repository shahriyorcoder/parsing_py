from bs4 import BeautifulSoup
import requests

#  STADION UZ 
######################################################
# page = requests.get('https://stadion.uz/')
# data = BeautifulSoup(page.content,'html.parser')
# komand = []

# serch = data.find(id='online_tablo').find('ul')
# data = serch.findChildren('li',recursive=False)
# for s in data:
#     if s  != None:
#         for f in s.findChildren('ul'):
#             komand.append([ f.find('li',id='online_tablo_day').text, f.find('li',id='online_tablo_team1').text,f.find('li',id='online_tablo_result').text,f.find('li',id='online_tablo_team2').text])
# setdata = str(input('Komanda kirit : ' ))
# for i in komand:
#     pass
#     if setdata == str(i[3]):
#         print(i[0])
#         print(i[1].strip() , i[2].strip() , i[3].strip())
#         break
#     elif  str(i[1]).endswith(setdata) :
#         print(i[0])
#         print(i[1].strip() , i[2].strip() , i[3].strip())
#         continue
#     else:
#         print('Komanda topilmadi')
#         break
######################################################




# OLX_PARSING
######################################################
# page = requests.get('https://www.olx.uz/nedvizhimost/')
# data = BeautifulSoup(page.content,'html.parser')
# olx_data = []
# count =0
# page_size = 10
# for b in data.find('div',class_='css-oukcj3' ).find_all('div',class_='css-1sw7q4x'):
#     count+=1
#     img  = b.find('a').find('div').find('div').find('div',class_='css-1ut25fa').find('div').find('div').find('img').attrs['src'] 
#     title = b.find('a').find('div').find('div').find('div',class_='css-1apmciz').find('div',class_='css-u2ayx9').find('h6')
#     price = b.find('a').find('div').find('div').find('div',class_='css-1apmciz').find('div',class_='css-u2ayx9').find('p')
#     location = b.find('a').find('div').find('div').find('div',class_='css-1apmciz').find('div',class_='css-odp1qd').find('p')
#     kvadrat = b.find('a').find('div').find('div').find('div',class_='css-1apmciz').find('div',class_='css-odp1qd').find('div')
#     olx_data.append({
#         "img":img,
#         "title":title.text,
#         "price":price.text,
#         "location":location.text,
#         "kvadrat":kvadrat.text,}
#         )
#     if page_size==count:
#         break
# print(olx_data)
# print(count)
################## ####################################

