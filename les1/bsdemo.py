#encoding  = utf-8

import requests
from bs4 import BeautifulSoup
import re

if __name__ == '__main__':
    url = 'https://python123.io/ws/demo.html'
    r = requests.request('get',url)
    demo = r.text;
    soup = BeautifulSoup(demo,'html.parser')
    # print(soup.head.title.string)
    # print(soup.head.contents)
    # print(soup.body.contents)
    # print(len(soup.body.contents))
    # print(soup.body.contents[1])



    # print(soup.a.next_sibling.next_sibling)
    # print(soup.a.previous_sibling)

    # print(soup.prettify())


    # for link in soup.find_all('a'):
    #     print(link['href'])

    # for tag in soup.find_all(True):
    #     print(tag.name)


    # for link in soup.find_all(re.compile('a')):
    #     print(link.name)

    # for link  in soup.find_all('p','course'):
    #     print(link)


    for link in soup.find_all(id='link1'):
        print(link)