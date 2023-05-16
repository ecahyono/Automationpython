from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log7KasieVerifikasiKelulusanPeserta.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)
    
@pytest.mark.webtest
def test7_SetupOs_KasieVerifikasiKelulusanPeserta():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_KTR_027():      
    kasieKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role operator')

@pytest.mark.webtest
def test_TC_KTR_028():
    sleep(driver)
    VerifikasiKelulusanPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Program Pelatihan Keterampilan')


@pytest.mark.webtest
def test_TC_KTR_029():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, "#verifikasi-0 .h-5").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "chooseVerifikasi").click()
    driver.find_element(By.ID, "verifikasi").click()

    driver.find_element(By.ID, "keterangan").send_keys(PredikatFaker0)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Memverifikasi Data')]")))


    

    Log.info("Kasie melakukan v erifikasi pada presensi peserta kegiatan")

@pytest.mark.webtest
def test_TC_KTR_030():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    driver.find_element(By.ID, "detail-0").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))

@pytest.mark.webtest
def test_exit_7_KasieVerifikasiKelulusanPeserta():
    sleep(driver)
    quit(driver)
    Log.info('exit session')