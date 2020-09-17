import shutil
from selenium import webdriver

HOST = 'https://www.instagram.com/'
LOGIN_URL = HOST + 'accounts/login/?source=auth_switcher/'

TIMEOUT = 30

path_to_chrome = shutil.which('chromedriver')
DRIVER = webdriver.Chrome(path_to_chrome)
