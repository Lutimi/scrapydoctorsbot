# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:50:24 2021

@author: misat
"""

import requests
from bs4 import BeautifulSoup

r= requests.get('https://200.48.13.39/cmp/php/listaespecialidades.php?key=17')


soup = BeautifulSoup(r.content, 'lxml')

ls_especialidades = soup.find_all("a", alt_="Visualizar") 

for x in ls_especialidades:
    print(x)

# print(soup.prettify())