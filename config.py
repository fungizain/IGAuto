from selenium import webdriver

path_to_chrome = '/usr/local/bin/chromedriver'

DRIVER = webdriver.Chrome(path_to_chrome)

TIMEOUT = 30

HOST = 'https://www.instagram.com/'

LOGIN_URL = HOST + 'accounts/login/?source=auth_switcher/'