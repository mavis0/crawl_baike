# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
from bs4 import BeautifulSoup
import re

old_url = set()
new_url = set()

#'http://baike.baidu.com/item/Python'
root_url = 'http://baike.baidu.com/item/Python'
new_url.add(root_url)
title = []
count = 0

while len(new_url) != 0 and count < 1000:
    url = new_url.pop()
    try:
        res = urllib.request.urlopen(url, timeout = 0.5).read()
    except:
        print('%s isn\'t reachable' % url)
        continue
    finally:
        old_url.add(url)
    soup = BeautifulSoup(res, 'html.parser', from_encoding= 'utf-8')
    #print(soup.find('a', re.compile('view/\d*')))
    title.append(soup.h1.string)
    links = soup.find_all('a', href = re.compile('view/\d*.htm'))
    for link in links:
#        print(link.attr)
        new_url.add('http://bike.baidu.com' + link['href'])
        #print(link[''])
    count = count + 1
    print(str(count) + ':' + soup.h1.string)
    print(url)

print(title)