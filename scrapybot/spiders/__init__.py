# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Section 1
import scrapy

#Section 2
class FirstSpider(scrapy.Spider):
    name = "Books"
    start_urls = [
        
        # "https://www.cmp.org.pe/conoce-a-tu-medico/",
        "https://www.cmp.org.pe/conoce-a-tu-medico/",
        "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
        ]
    
    #Section 3
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)