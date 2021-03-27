# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:21:31 2021

@author: misat
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def doctor_list_scrape():
    
    url = 'https://200.48.13.39/cmp/php/listaespecialidades.php?key=17'
    headers = ({'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    
    print(r.status_code)

    list_es = [i.text for i in soup.findAll('td')]
    df = pd.DataFrame(list_es)
    print(df)
    
    #add timer
    time.sleep(20)
    
end_timer = time.time() + 60 * 2
while time.time() < end_timer:
    doctor_list_scrape()
        