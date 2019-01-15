from selenium import webdriver

driver = webdriver.Chrome('C://chromedriver.exe') #Declare an environment variable
driver.get("https://eksisozluk.com")

search_box = driver.find_element_by_id("search-textbox")
search_box.clear()

userInput = "mustafa kemal atatürk" #Header example
search_box.send_keys(userInput)
search_box.submit()

sukela_url = driver.current_url + '?a=nice'
driver.get(sukela_url)

#print each entry on the first page, it will be edited and deleted. soon.
for i in range(1,10):
    print(driver.find_element_by_xpath('//*[@id="entry-item-list"]/li['+str(i)+']/div[1]').get_property('innerText'))

driver.quit()