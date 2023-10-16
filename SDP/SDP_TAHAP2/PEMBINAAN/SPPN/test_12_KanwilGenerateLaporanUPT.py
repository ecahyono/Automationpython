from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_9_OpGenerateLaporanUPTi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



kanwilPembinaan(driver)

@pytest.mark.webtest
def test_TC_SPPN_033_AksesMenuGenerateLaporan():
    print('Kanwil mengakses submenu Penilaian ')
    sleep(driver)
    laporanSPPN(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

   
@pytest.mark.webtest
def test_TC_SPPN_034_OpGenerateLaporanUPT():
    print('Kanwil mengakses submenu Laporan Bulanan ')
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "searchButton")))
 
    if BulanWbpWaliFaker == "01":
        driver.find_element(By.ID, "januariButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari generate laporan Kanwil')
    elif BulanWbpWaliFaker == "02":
        driver.find_element(By.ID, "februariButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari generate laporan Kanwil')
    elif BulanWbpWaliFaker == "03":
        driver.find_element(By.ID, "maretButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret generate laporan Kanwil')
    elif BulanWbpWaliFaker == "04":
        driver.find_element(By.ID, "aprilButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April generate laporan Kanwil')
    elif BulanWbpWaliFaker == "05":
        driver.find_element(By.ID, "meiButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "06":
        driver.find_element(By.ID, "juniButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "07":
        driver.find_element(By.ID, "juliButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "08":
        driver.find_element(By.ID, "agustusButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "09":
        driver.find_element(By.ID, "septemberButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "10":
        driver.find_element(By.ID, "buttonOktober").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "11":
        driver.find_element(By.ID, "novemberButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November generate laporan Kanwil')
     
    elif BulanWbpWaliFaker == "12":
        driver.find_element(By.ID, "desemberButton").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember generate laporan Kanwil')

    

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Ya')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Ya')]").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Laporan Bulanan Berhasil Dibuat')]")))
    # driver.find_element(By.ID, "selectStatus").click()
    # driver.find_element(By.ID, "otorisasi").click()
    # driver.find_element(By.ID, "keterangan").send_keys(rekomendasiFaker)
    # time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()
    
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Laporan UPT Berhasil Diotorisasi')]")))
    # Log.info ('Verifikasi kasie laporan bulanan upt')
    quit(driver)



    



