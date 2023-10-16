from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log5KasiePersetujuanPesertaKegiatan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test5_SetupOs_KasiePersetujuanPesertaKegiatan():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_KTR_020():
    attach(data=driver.get_screenshot_as_png())      
    kasieKeterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('"Login aplikasi menggunakan akun dengan role kasie"')

@pytest.mark.webtest
def test_TC_KTR_021():
    sleep(driver)
    MenuPersetujuanPresensiPesertaKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kasie mengakses halaman Persetujuan Presensi Peserta Kegiatan')


@pytest.mark.webtest
def test_TC_KTR_022():
    attach(data=driver.get_screenshot_as_png())
    driver.implicitly_wait(60)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    
    driver.find_element(By.CSS_SELECTOR, "#verifikasi-0 .h-5").click()

    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) > .el-form-item__content > .el-select .el-input__inner").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton > span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "chooseVerifikasi")))
    driver.find_element(By.ID, "verifikasi").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "keterangan")))
    driver.find_element(By.ID, "keterangan").send_keys("Verifikasi")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Memverifikasi Data')]")))

    Log.info("Kasie melakukan v erifikasi pada presensi peserta kegiatan")

@pytest.mark.webtest
def test_TC_KTR_023():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, "#detail-0 .h-5").click()
    
    Log.info('Kasie mengakses halaman Detail Absensi Kegiatan')

@pytest.mark.webtest
def test_5_exit_OpPersetujuanPesertaKegiatan():
    quit(driver)
    Log.info('Exit')







    
    