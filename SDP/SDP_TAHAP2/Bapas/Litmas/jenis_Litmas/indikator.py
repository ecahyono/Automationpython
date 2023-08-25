from jenis_Litmas.src import *

def turu(driver):
  time.sleep(2)

def turu3det(driver):
  time.sleep(2)

def turu5detik(driver):
  time.sleep(5)
  
def lagiloading(driver):
  WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))
  WebDriverWait(driver, 60).until(EC.invisibility_of_element_located((By.CLASS_NAME, "el-loading-spinner")))

def tutuppopup(driver):
  WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tox-icon > svg')))
  popuptutup1 = driver.find_element(By.CSS_SELECTOR, 'div.tox-icon > svg')
  popuptutup1.click()

def simpansesi(driver):
  driver.find_element(By.ID, 'buttonSimpanSesi').click()

def Selanjutnya(driver):
  driver.find_element(By.XPATH, '//button[2]').click()

def simpansesipenjamininstrumen(driver):
  driver.find_element(By.ID, 'buttonSimpan').click()