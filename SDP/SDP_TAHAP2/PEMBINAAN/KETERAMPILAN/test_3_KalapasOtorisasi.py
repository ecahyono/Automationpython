from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log3KalapasOtorisasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test3_SetupOs_KalapasOtorisasi_():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_KTR_012():      
    KalapasKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info("Login aplikasi menggunakan akundengan role kalapas")

@pytest.mark.webtest
def test_TC_KTR_013():
    sleep(driver)
    MenuPersetujuanPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Persetujuan Peserta Kegiatan')

@pytest.mark.webtest
def test_TC_KTR_015():
    sleep(driver)
    d = driver.find_element
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#verifikasi-0 path:nth-child(2)")))

    d(By.CSS_SELECTOR, "#verifikasi-0 path:nth-child(2)").click()
    Log.info('Click Action Verifikasi')

    wait.until(EC.element_to_be_clickable((By.ID, "chooseVerifikasi")))
    d(By.ID, "chooseVerifikasi").click()
    wait.until(EC.element_to_be_clickable((By.ID, "verifikasi")))
    d(By.ID, "verifikasi").click()
    Log.info ('Click Verifikasi')

    d(By.ID, "keterangan").send_keys("Verifikasi Peserta Kegiatan")
    Log.info('Input Keterangan')
    
    wait.until(EC.element_to_be_clickable((By.ID, "submitButton")))
    d(By.ID, "submitButton").click()
    Log.info('Click Submit')
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))

    Log.info('Kasie melakukan verifikasi peserta kegiatan pada kegiatan yang telah ditambahkan oleh operator')

@pytest.mark.webtest
def test_TC_KTR_014():
    sleep(driver)
    d=driver.find_element
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    d(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
   

    Log.info('Kalapas mengakses halaman Detail Program Pelatihan Keterampilan')


@pytest.mark.webtest
def test3_exit_KalapasOtorisasi():
    quit(driver)
    Log.info('Exit')







    
    