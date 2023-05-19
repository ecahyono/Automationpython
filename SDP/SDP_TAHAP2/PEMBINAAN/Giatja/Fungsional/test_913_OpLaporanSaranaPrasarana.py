from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/log_13_OpLaporanSaranaPrasarana.txt', mode="w")
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
def test_TC_GIATJA_048():
    Op_Giatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login Operator')

@pytest.mark.webtest
def test_TC_GIATJA_049():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Laporan Produk')

@pytest.mark.webtest
def test_TC_GIATJA_050():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Kegiatan Kerja')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Kegiatan Kerja')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Kegiatan Kerja')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Kegiatan Kerja')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Kegiatan Kerja')
     
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Kegiatan Kerja')
     
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Kegiatan Kerja')
     
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustussarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Kegiatan Kerja')
     
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Kegiatan Kerja')
     
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktobersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Kegiatan Kerja')
     
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Kegiatan Kerja')
     
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Kegiatan Kerja')

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'OK')]")))
    driver.find_element(By.XPATH, "//button[contains(.,'OK')]").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Membuat Laporan Berhasil !')]")))
     
    Log.info('membuat Laporan Sarana Dan Prasaran')

@pytest.mark.webtest
def test_exit_Operator():
    sleep(driver)
    quit(driver)
    Log.info('Exit')







    
    