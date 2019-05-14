
from selenium import webdriver
driver = webdriver.Firefox()

driver.get("http://www.uchi.ru")

driver.find_element_by_id('login').send_keys(22)
driver.find_element_by_id('password').send_keys('космос')
driver.find_element_by_class_name('login-form__submit').click()

driver.close()
