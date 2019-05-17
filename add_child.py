from selenium import webdriver
from session import login, open_home_page
import time


open_home_page()

login(login='antonevich+1@uchi.ru', password=1234)


driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/a').click()


driver.close()