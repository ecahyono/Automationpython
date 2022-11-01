from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import platform
from pytest import mark
import time
from pytest_html_reporter import attach
@mark.fixture_test()
def test_setup():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Downloads/chromedriver')
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        driver.get("https://mail.google.com/mail/u/0/#inbox")
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("hhttps://mail.google.com/mail/u/0/#inbox")
        driver.maximize_window()
        driver.implicitly_wait(5)
    print('.')
    print('=================================================================================Setup OS berhasil================================================================================= ')

#gue pengen looping dari sini
@mark.fixture_test()
def test_coba1(x):
    print('1')

@mark.fixture_test()
def test_coba2(x):
    print('2')


@mark.fixture_test()
def test_coba3(x):
    print('3')


@mark.fixture_test()
def test_coba4(x):
    print('4')

for x in range(100):
    test_coba1(x)
    test_coba2(x)
    test_coba3(x)
    test_coba4(x)

#sampe sini


def teardown():
    print('.')
    print('====================================================================================================== TEST   ======================================================================================================')
    time.sleep(10)
    driver.close()
    driver.quit