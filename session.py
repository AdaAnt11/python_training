from selenium import webdriver
driver = webdriver.Firefox()

def open_home_page():
    driver.get("http://www.uchi.ru")


def login( login, password):
    driver.find_element_by_id('login').send_keys(login)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_class_name('login-form__submit').click()
    driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/a').click()