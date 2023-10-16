from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log4OpAbsensiKegiatan.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test4_SetupOs__OpAbsensiKegiatan():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_KTR_016():      
    Op_Keterampilan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login aplikasi menggunakan akun dengan role operator')

@pytest.mark.webtest
def test_TC_KTR_017():
    sleep(driver)
    MenuPresensiKegiatan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Program Pelatihan Keterampilan')

@pytest.mark.webtest
def test_TC_KTR_018():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#absensi-0 > span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, "#absensi-0 > span").click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "backButton")))

    driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "pesertaOption-0")))

    if JumlahPeserta == 1:  
        driver.find_element(By.ID, "pesertaOption-0").click()
    elif JumlahPeserta == 2:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
    elif JumlahPeserta == 3:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
        driver.find_element(By.ID, "pesertaOption-2").click()
    elif JumlahPeserta == 4:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
        driver.find_element(By.ID, "pesertaOption-2").click()
        driver.find_element(By.ID, "pesertaOption-3").click()
    elif JumlahPeserta == 5:
        driver.find_element(By.ID, "pesertaOption-0").click()
        driver.find_element(By.ID, "pesertaOption-1").click()
        driver.find_element(By.ID, "pesertaOption-2").click()
        driver.find_element(By.ID, "pesertaOption-3").click()
        driver.find_element(By.ID, "pesertaOption-4").click()

    driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(2) > #submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")))
    driver.find_element(By.CSS_SELECTOR, ".mt-6 > #submitButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))


    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mencatat absensi peserta kegiatan')


@pytest.mark.webtest
def test_TC_KTR_019():
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))


    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#absensi-0 > span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#detail-0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#detail-0 .h-5").click()

    driver.find_element(By.CSS_SELECTOR, ".el-breadcrumb__item:nth-child(4) > .el-breadcrumb__inner").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    Log.info('Operator mengakses halaman Detail Absensi Kegiatan')
    
@pytest.mark.webtest
def test_4_exit_OpAbsensiKegiatan():
    quit(driver)
    Log.info('Exit')







    
    