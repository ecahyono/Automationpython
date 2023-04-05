import platform
import time
from os import environ
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def bapasbdg(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("bpsbdg")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def loginOperatorSumedang(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("op-keamanan-sumedang")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())



def loginwaru(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("master-rutan1bdg")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def SpvRutanBdg(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("spv-keamanan-rutan-bandung")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def op_keamanan_mp(driver):
    
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("op-keamanan-mp")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def Op_Keamanan_p2u(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("op-keamanan-p2u")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')


def loginSumedang(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-sumedang")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def LapasPerempuan(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("lapasperempuan")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def loginBpsBdg(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("bpsbdg")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

def testsukamiskin(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-sukamiskin")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def loginBanjar(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-banjar")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())

def loginSPV(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-gal")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')

    attach(data=driver.get_screenshot_as_png())


def oprupbasanbdg(driver):
	WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'login')))
	driver.find_element(By.ID, "login").click()
	# ini masuk ke form input username
	driver.find_element(By.ID, "username").click()
	driver.find_element(By.ID, "username").send_keys("oprup")
	time.sleep(2)
	driver.find_element(By.ID, "password").send_keys("password")
	# click button login
	driver.find_element(By.ID, "kc-login").click()
	WebDriverWait(driver, 10)
	print('==========================================================================')
	print('''@@@&GJ7!~~~!?5B@@&P?!~^^^~!JG&@@&PJ7~~~~!?5#@@@@@
@@#J^^!?YYYYJ7~^!?^^!J55P55J!^~YJ^^!?Y55YJ7~^!P@@@
@P^:?PGP7^^^~GG7.:?PGJ!~~!JPGP!.:?PGY!!!7JGG5!.7&@
G::YGGG7 ^55YGY::YGGG7 !?~ ^PY:^5GGG7 ^?^ !GGG7.7@
7.?GPPGY: ^?PG!.!GGPG7 YGG! ?!.?GPPG7 7G? ^PGGP^:B
7.?GPPPGPY! .57.!GGPG7 JGG7 ?!.JGPPG7 .^:~5GPGP^:G
P:^5GGGJ!J?. 55::JGGG7 7Y! ^PJ:^5GGG7 !PPGGPGG?.!@
@P::JPGY!~~75GGJ..75GJ^^^~?PG5^.^JPGJ:?GGGGG57.!#@
@@@?^^7J5555Y?!^~J~^~?JYYYY?~^!5?^^7JY555Y?!^~5@@@
@@@@&P?!~^^~~7JG&@@BY7!~~~!?5B@@@#5?!~^^~~7YB@@@@@''')
	print('==========================================================================')
    
	attach(data=driver.get_screenshot_as_png())

def supcirebon(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'login')))
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("supcirebon")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

def lapastesting(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'login')))
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("lapastesting")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    attach(data=driver.get_screenshot_as_png())
def bpstesting(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'login')))
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("bpstesting")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    attach(data=driver.get_screenshot_as_png())
def oprupbasaninternal(driver):
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID , 'login')))
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("oprupbasaninternal")
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    attach(data=driver.get_screenshot_as_png())