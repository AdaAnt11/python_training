from selenium import webdriver
driver = webdriver.Firefox()
from session import login, open_home_page


open_home_page()

login(login=22, password='космос')

driver.close()
