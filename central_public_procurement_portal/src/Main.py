#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dependencies.scraping.Scraper import Scraper
from dependencies.cleaning.Cleaning import Cleaning
from dependencies.standardization.Standardization import Standardization
class Main:
    def __init__(self):
        self.obj1 = Scraper()
        self.obj1.crawler()
        
        self.obj2 = Cleaning()
        self.obj2.cleaning()
        self.obj2.saving()
        self.obj2.cleanup()
        
        self.obj3 = Standardization()
        self.obj3.snake_case()
        self.obj3.saving()
        
        
        
        
        


# In[ ]:

if __name__ == '__main__':
    obj = Main()