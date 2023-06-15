from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach

from selenium.webdriver.support import expected_conditions as EC

def OpKemandirian(driver):
    driver.implicitly_wait(30)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "username")))
    # driver.find_element(By.ID, "username").send_keys("Fuad Zaidan")
    driver.find_element(By.ID, "username").send_keys("eko-suryono")
    
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 30)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())