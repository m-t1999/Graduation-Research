import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv


#Selenium
driver = webdriver.Chrome()

url = 'http://www.tennisabstract.com/' #開きたいページのURLをいれる
driver.get(url) 
#element = driver.find_element_by_css_selector("#rankings > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(2) > a")
element = driver.find_element_by_link_text("Novak Djokovic")
element.click()

#element = driver.find_element_by_css_selector("#tour-years > tbody > tr:nth-child(1) > td:nth-child(1) > b > a")
element = driver.find_element_by_link_text("2020")
element.click()

#element = driver.find_element_by_css_selector("#matches > tbody > tr:nth-child(4) > td:nth-child(9) > a")
element = driver.find_element_by_link_text("(ch)")
element.click()

time.sleep(2)
window = driver.window_handles[-1]
driver.switch_to.window(window)

element = driver.find_element_by_id("pointlog")
element.click()


 #time.sleep(3)


html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
table= soup.select('#forecast > table')
td_tags = soup.find_all("td")
text = [t.get_text().strip() for t in td_tags]
driver.quit()






with open('sample.csv','w',newline="",encoding='utf8')as f:
    writer = csv.writer(f)
    writer.writerow(text)






#     #time.sleep(1)
