from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_7_OperatorLaporanPemasaran.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test_1_SetupOs():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()   

@pytest.mark.webtest
def test_TC_GIATJA_030():
    sleep(driver)   
    Op_Giatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_GIATJA_031():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Laporan Kegiatan Kerja dan pemasaran-pnbpsi')

@pytest.mark.webtest
def test_TC_GIATJA_032():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Sarana')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Sarana')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Sarana')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Sarana')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Sarana')
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Sarana')
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Sarana')
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustuspemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Sarana')
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Sarana')
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktoberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Sarana')
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Sarana')
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Sarana')

    WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.ID, ".circular")))
    driver.find_element(By.XPATH, "//span[contains(.,'OK')]").click()
    WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.ID, ".circular")))
    time.sleep(2)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "Aprilpemasaran-pnbp1")))
    Log.info('Operator membuat Laporan Kegiatan Kerja dan pemasaran-pnbpsi')
     

   

@pytest.mark.webtest
def test_exit():
    quit(driver)
    Log.info('Exit')







    
    