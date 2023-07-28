#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Created on Fri Oct 7 13:20:12 2022

@author: Januario Cipriano
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Users\\a248433\\Documents\\drivers\\chromedriver.exe")
driver.get('http://www.python.org')
assert "Python" in driver.title

elem = driver.find_element(By.NAME, 'q')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()



















