from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_6_LapbulananWBPWali.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)



wali_SURIYAH(driver)

@pytest.mark.webtest
def test_TC_SPPN_030_AksesMenuGenerateLaporan():
    print('wali mengakses submenu Penilaian ')
    sleep(driver)
    LaporanBulananWali(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

   
@pytest.mark.webtest
def test_TC_SPPN_031_GenerateLaporan():
    print('wali mengakses submenu Laporan Bulanan ')
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "searchButton")))
    if BulanWbpWaliFaker == "01":
        driver.find_element(By.ID, "buttonJanuari-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Generate Penilaian Wbp')
    elif BulanWbpWaliFaker == "02":
        driver.find_element(By.ID, "buttonFebruari-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Generate Penilaian Wbp')
    elif BulanWbpWaliFaker == "03":
        driver.find_element(By.ID, "buttonMaret-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Generate Penilaian Wbp')
    elif BulanWbpWaliFaker == "04":
        driver.find_element(By.ID, "buttonApril-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Generate Penilaian Wbp')
    elif BulanWbpWaliFaker == "05":
        driver.find_element(By.ID, "buttonMei-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "06":
        driver.find_element(By.ID, "buttonJuni-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "07":
        driver.find_element(By.ID, "buttonJuli-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "08":
        driver.find_element(By.ID, "buttonAgustus-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "09":
        driver.find_element(By.ID, "buttonSeptember-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "10":
        driver.find_element(By.ID, "buttonOktober-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "11":
        driver.find_element(By.ID, "buttonNovember-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Generate Penilaian Wbp')
     
    elif BulanWbpWaliFaker == "12":
        driver.find_element(By.ID, "buttonDesember-index0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Generate Penilaian Wbp')

    
@pytest.mark.webtest
def test_TC_SPPN_32_InputRekomendasi():
    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "variabelV1").send_keys("Catatan Skor Pembinaan Kepribadian")
    Log.info('Catatan Skor Pembinaan Kepribadian')
    driver.find_element(By.ID, "variabelV2").send_keys("Catatan Skor Pembinaan Kemandirian")
    Log.info('Catatan Skor Pembinaan Kemandirian')
    driver.find_element(By.ID, "variabelV3").send_keys("Catatan Skor Sikap Narapidana")
    Log.info('Catatan Skor Sikap Narapidana')
    driver.find_element(By.ID, "variabelV4").send_keys("Catatan Skor Kondisi Mental Narapidana")
    Log.info('Catatan Skor Kondisi Mental Narapidana')
    driver.find_element(By.ID, "buttonSimpanCatatan").click()
    Log.info('Berhasil Tambah Catatan')

    driver.find_element(By.ID, "rekomendasi").send_keys(rekomendasiFaker)
    Log.info('Input Rekomendasi')

    # driver.find_element(By.ID, "submitButton").click()
    # Log.info('Berhasil Input Rekomendasi')



