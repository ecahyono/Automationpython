from source import *
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler("./Log/Log10KalapasVerifikasiLaporanPelatihanKeterampilan.log", mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)
    
@pytest.mark.webtest
def test9_SetupOs_KalapasVerifikasiLaporanPelatihan():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_KTR_041():      
    KalapasKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role Kalapas')

@pytest.mark.webtest
def test_TC_KTR_042():
    sleep(driver)
    LaporanPelatihanKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Laporan Pelatihan Keterampilan')


@pytest.mark.webtest
def test_TC_KTR_043():
    sleep(driver)
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "buttonBulan-0-1")))
    
    if BulanFaker == "01":
        driver.find_element(By.ID, "buttonBulan-0-0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Laporan')
    elif BulanFaker == "02":
        driver.find_element(By.ID, "buttonBulan-0-1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Laporan')
    elif BulanFaker == "03":
        driver.find_element(By.ID, "buttonBulan-0-2").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Laporan')
    elif BulanFaker == "04":
        driver.find_element(By.ID, "buttonBulan-0-3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Laporan')
    elif BulanFaker == "05":
        driver.find_element(By.ID, "buttonBulan-0-4").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Laporan')
     
    elif BulanFaker == "06":
        driver.find_element(By.ID, "buttonBulan-0-5").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Laporan')
     
    elif BulanFaker == "07":
        driver.find_element(By.ID, "buttonBulan-0-6").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Laporan')
     
    elif BulanFaker == "08":
        driver.find_element(By.ID, "buttonBulan-0-7").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Laporan')
     
    elif BulanFaker == "09":
        driver.find_element(By.ID, "buttonBulan-0-8").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Laporan')
     
    elif BulanFaker == "10":
        driver.find_element(By.ID, "buttonBulan-0-09").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Laporan')
     
    elif BulanFaker == "11":
        driver.find_element(By.ID, "buttonBulan-0-10").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Laporan')
     
    elif BulanFaker == "12":
        driver.find_element(By.ID, "buttonBulan-0-11").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Laporan')

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Belum Verifikasi')]")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-button:nth-child(2) > span")))
    driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(2) > span").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-full .el-input__inner")))
    driver.find_element(By.CSS_SELECTOR, ".w-full .el-input__inner").click()
    driver.find_element(By.XPATH, "//div[5]/div/div/div/ul/li").click()
    driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys(KeteranganFaker)
    driver.find_element(By.ID, "submitButton").click()
    
    Log.info('Kalapas melakukan verifikasi pada Laporan Pelatihan Keterampilan yang telah di Verifikasi oleh Kasie')
    

@pytest.mark.webtest
def test_Exit10_KalapasVerifikasiLaporanPelatihanKeterampilan():
    sleep(driver)
    attach(data=driver.get_screenshot_as_png())
    quit(driver)
    Log.info('Exit Browser..')
