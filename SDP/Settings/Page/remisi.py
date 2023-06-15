
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import os, platform, time, pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




def MenuSPPNPerwalian(driver):
    driver.implicitly_wait(100)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'pembinaan-10')))
    nav1 = driver.find_element(By.CSS_SELECTOR, ".el-sub-menu__title > #pembinaan-10")
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.2)
    nav2 = driver.find_element(By.ID, "SPPN-11")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav2).perform()
    time.sleep(0.2)
    nav3 = driver.find_element(By.ID, "perwalian-11")
    time.sleep(0.2)
    ActionChains(driver).move_to_element(nav3).perform()
    driver.find_element(By.LINK_TEXT, "Tim Perwalian").click()