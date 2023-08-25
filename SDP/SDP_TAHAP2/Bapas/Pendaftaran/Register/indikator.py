from src import *

def turu(driver):
  time.sleep(2)

def klicki(driver):
  input('Menuggu sampai data ter load kemudian klik ENTER')

def lamaturu(driver):
  time.sleep(3)

def tutuppopup(driver):
  WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tox-icon > svg')))
  popuptutup1 = driver.find_element(By.CSS_SELECTOR, 'div.tox-icon > svg')
  popuptutup1.click()

def lagiloading(driver):
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))

def simpandatanya(driver):
  driver.find_element(By.ID, 'submitButton').click()