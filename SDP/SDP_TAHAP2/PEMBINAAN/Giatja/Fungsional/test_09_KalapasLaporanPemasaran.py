from source import *
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/test_9_KalapasLaporanGiatja.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_SetupOsKalapas():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()  
    Log.info('Setup Os Akses aplikasi SDP')

@pytest.mark.webtest
def test_TC_GIATJA_036():
    Op_Giatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login Kalapas')

@pytest.mark.webtest
def test_TC_GIATJA_037():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Laporan Kegiatan Kerja dan Produksi')


@pytest.mark.webtest
def test_TC_GIATJA_038():
    sleep(driver)
    driver.implicitly_wait(60)
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
    
    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')

    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".circular")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Belum Otorisasi')]")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))
    driver.find_element(By.XPATH, "//span[contains(.,'Otorisasi')]").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton > span")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "cancel")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "statuVerifikasi")))
    driver.find_element(By.ID, "statuVerifikasi").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'Sudah Otorisasi')]")))
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[contains(.,'Sudah Otorisasi')]").click()
    Log.info('Pilih status verifikasi"')

    driver.find_element(By.ID, "keterangan").send_keys(keteranganFaker)
    Log.info('input Keterangan ')

    driver.find_element(By.ID, "submitButton").click()

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Laporan Berhasil Diperbarui')]")))


    Log.info('Kalapas melakukan otorisasi pada Laporan Kegiatan Kerja dan Produksi yang telah di verifikasi oleh kasie')
    quit(driver)