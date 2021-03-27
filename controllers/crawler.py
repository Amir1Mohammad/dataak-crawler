# -*- coding: utf-8 -*-
from lxml import html
import requests
from bs4 import BeautifulSoup
from models.base import session
from models.user import User
from models.post import Post
from utilities import constants


def start_crawling():
    session_requests = requests.session()
    page = session_requests.post(constants.url, data=constants.values, verify=False, cookies=constants.cookies)

    my_page = page.text
    soup = BeautifulSoup(my_page, 'html.parser')
    tree = html.fromstring(page.content.decode())
    category = tree.xpath('//div//strong//a/text()')

    for each in category:
        football = soup.find(text=each)
        user = football.parent.parent.parent.parent.contents[-2].find_all('a')[-1].text
        new_user = User(name=user)
        session.add(new_user)
        session.commit()

        new_item = Post(user=user, title=each)
        session.add(new_item)
        session.commit()

    tree = html.fromstring(page.content.decode())
    category = tree.xpath('//div//strong//a/text()')
    span_user = tree.xpath('//td/span[@class="smalltext"]//strong/text()')

    print(category)
    print(span_user)


start_crawling()
