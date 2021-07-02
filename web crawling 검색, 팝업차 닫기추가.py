#!/usr/bin/env python
# coding: utf-8

# In[241]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.mangoplate.com/'


# In[254]:


driver =  webdriver.Chrome(executable_path='chromedriver')
#("/static/chromedriver.exe")
driver.get(url)


# In[78]:


time.sleep(5)


# In[182]:


# main = driver.window_handles 
# print(main)
# for handle in main: 
#     if handle != main[0]: 
#         driver.switch_to_window(handle) 
#         driver.close()


# In[243]:


elem = driver.find_element_by_class_name('Header__LogoIcon')
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(elem, 0, 0).perform()
action_chains.click().perform()


# In[260]:


element=driver.find_element_by_name('main-search') #검색란 찾기
element.send_keys("가산디지털단지") #검색어 입력


# In[261]:


ser_btn=driver.find_element_by_class_name("btn-search")# 검색찾기
ser_btn.click()


# In[262]:


elem2 = driver.find_element_by_class_name('thumb')
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(elem2, 0, 0).perform()
action_chains.click().perform()


# In[247]:


soup = BeautifulSoup(driver.page_source, 'html.parser')
soup


# In[249]:


name = soup.select('.title h1')
name
rest_name = name[0].text
rest_name


# In[250]:


img_list = soup.select('.restaurant-photos-item img')
img_list
for img in img_list:
    rest_photo_url = img.attrs['src']
    print(rest_photo_url)


# In[251]:


td = soup.select('.only-desktop td')
td
rest_address = td[0].text
print(rest_address)

rest_tel = td[1].text
print(rest_tel)


# In[252]:


td = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(3) > td')
rest_kind = td[0].text
rest_kind


# In[253]:


td = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(4) > td')
rest_price = td[0].text
rest_price

