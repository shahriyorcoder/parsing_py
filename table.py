import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.google.com/search?q=laliga+table&rlz=1C1IXYC_ruUZ1083UZ1083&oq=laliga+&gs_lcrp=EgZjaHJvbWUqDAgBECMYJxiABBiKBTIGCAAQRRg5MgwIARAjGCcYgAQYigUyBwgCEC4YgAQyBwgDEC4YgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQkxNDQzNWowajSoAgCwAgA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11khrmf0s3;2;/m/09gqx;st;fp;1;;;')
data = BeautifulSoup(url.content,'html.parser')

print(data)
