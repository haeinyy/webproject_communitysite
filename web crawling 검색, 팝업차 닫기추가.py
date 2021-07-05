from selenium import  webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'https://www.mangoplate.com/'

driver =  webdriver.Chrome(executable_path='chromedriver')
#("/static/chromedriver.exe")
driver.get(url)
time.sleep(3)
elem = driver.find_element_by_class_name('Header__LogoIcon')
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(elem, 0, 0).perform()
action_chains.click().perform()

element=driver.find_element_by_name('main-search') #검색란 찾기
element.send_keys("신포닭강정") #검색어 입력

ser_btn=driver.find_element_by_class_name("btn-search")# 검색찾기
ser_btn.click()

elem2 = driver.find_element_by_class_name('thumb')
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(elem2, 0, 0).perform()
action_chains.click().perform()

soup = BeautifulSoup(driver.page_source, 'html.parser')

name = soup.select('.title h1')
rest_name = name[0].text
print(rest_name)

img_list = soup.select('.restaurant-photos-item img')
img_list
for img in img_list: 
    rest_photo_url = img.attrs['src']
    print(rest_photo_url)


td = soup.select('.only-desktop td')
td
rest_address = td[0].text
print(rest_address)

rest_tel = td[1].text
print(rest_tel)



td = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(3) > td')
rest_kind = td[0].text
print(rest_kind)



td = soup.select('body > main > article > div.column-wrapper > div.column-contents > div > section.restaurant-detail > table > tbody > tr:nth-child(4) > td')
rest_price = td[0].text
rest_price

