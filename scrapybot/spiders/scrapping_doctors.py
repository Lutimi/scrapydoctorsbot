# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:08:42 2021

@author: misat
"""

import scrapy


class SolutionSpider(scrapy.Spyder):
    name = "Solutions"
    #allow_domains[]
    
    medicos_urls = [
        
        'https://200.48.13.39/cmp/php/listaxespecialidad.php?id=00008&key=17&des=CARDIOLOGIA',
        
    ]
    

    def parse(self, response):
        page = response,url,split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename,"wb") as f:
            f.write(response.body)
