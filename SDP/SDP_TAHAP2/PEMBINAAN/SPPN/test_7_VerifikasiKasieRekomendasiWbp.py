from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_6_LapbulananWBPWali.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



KasieGiatja(driver)

@pytest.mark.webtest
def test_TC_SPPN_033_AksesMenuGenerateLaporan():
    print('Kasie mengakses submenu Penilaian ')
    sleep(driver)
    laporanSPPN(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

   
@pytest.mark.webtest
def test_TC_SPPN_034_VerifikasiRekomendasiKasie():
    print('Kasie mengakses submenu Laporan Bulanan ')
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "searchButton")))
    driver.find_element(By.ID, "tab-sppn").click()
    if BulanWbpWaliFaker == "01":
        driver.find_element(By.ID, "buttonJanuari-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Verifikasi Penilaian Wbp')
    elif BulanWbpWaliFaker == "02":
        driver.find_element(By.ID, "buttonFebruari-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Verifikasi Penilaian Wbp')
    elif BulanWbpWaliFaker == "03":
        driver.find_element(By.ID, "buttonMaret-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Verifikasi Penilaian Wbp')
    elif BulanWbpWaliFaker == "04":
        driver.find_element(By.ID, "buttonApril-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Verifikasi Penilaian Wbp')
    elif BulanWbpWaliFaker == "05":
        driver.find_element(By.ID, "buttonMei-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "06":
        driver.find_element(By.ID, "buttonJuni-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "07":
        driver.find_element(By.ID, "buttonJuli-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "08":
        driver.find_element(By.ID, "buttonAgustus-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "09":
        driver.find_element(By.ID, "buttonSeptember-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "10":
        driver.find_element(By.ID, "buttonOktober-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "11":
        driver.find_element(By.ID, "buttonNovember-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Verifikasi Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "12":
        driver.find_element(By.ID, "buttonDesember-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Verifikasi Penilaian Wbp')

    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "buttonVerOt")))
    driver.find_element(By.CSS_SELECTOR, "#buttonVerOt path").click()
    driver.find_element(By.ID, "status").click()
    driver.find_element(By.ID, "verifikasi").click()
    driver.find_element(By.ID, "keterangan").send_keys(rekomendasiFaker)
    driver.find_element(By.ID, "submitButton").click()

    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "searchButton")))
    Log.info('Verifikasi Rekomendasi Wbp')

    



