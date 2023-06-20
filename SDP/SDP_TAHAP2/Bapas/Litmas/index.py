from src import *

def filtertable(driver):
  kolom = driver.find_element(By.XPATH, "//input[@placeholder='Cari berdasarkan kolom']")
  kolom.click()
  kolom.send_keys('Jenis Litmas')
  kolom.send_keys(Keys.DOWN)
  kolom.send_keys(Keys.ENTER)
  time.sleep(2)
  driver.find_element(By.XPATH, '//input[@placeholder="Masukan kata kunci"]').send_keys('Litmas Diversi')
  time.sleep(2)
  driver.find_element(By. XPATH, "//button[@type='submit']").click()
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/div/div/button')))

  
  