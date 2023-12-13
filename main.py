from bs4 import BeautifulSoup
import requests
with open('home.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml' )
    course_card = soup.find_all("div",class_='card')
    for course in course_card:
        print(course.a.text.split()[-1])
 