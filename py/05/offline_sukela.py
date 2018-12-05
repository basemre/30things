from selenium import webdriver
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C://chromedriver.exe')
driver.get("https://eksisozluk.com")

search_box = driver.find_element_by_id("search-textbox")
search_box.clear()

userInput = "mustafa kemal atatürk" #Başlık örneği.
search_box.send_keys(userInput)
search_box.submit()

sukela_url = driver.current_url + '?a=nice'
driver.get(sukela_url)

#dıştaki loop, entry sayfaları için
for i in range(1,5):
    #sayfadaki her entry için
    for i in range(1,10):
        print(driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[2]/div[2]/section[1]/div[1]/ul[1]/li['+str(i)+']/div[1]').get_property('innerText'))

driver.quit()

#/html[1]/body[1]/div[3]/div[2]/div[2]/section[1]/div[1]/ul[1]/li[1]/div[1]
#/html[1]/body[1]/div[3]/div[2]/div[2]/section[1]/div[1]/ul[1]/li[2]/div[1]