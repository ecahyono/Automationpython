from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_4_KasieVerifikasi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test_TC_SPPN_016_LoginKasie():
    print('Login aplikasi menggunakan akun dengan role Kasie')
    kasie_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Kasie")

@pytest.mark.webtest
def test_TC_SPPN_017_AksesMenu():
    print('Kasie mengakses submenu Persetujuan Perwalian')
    sleep(driver)
    MenuSPPNPerwalianPersetujuan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

@pytest.mark.webtest
def test_TC_SPPN_018_KasieMelakukanVerifikasi():
    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:

        print('Kasie melakukan verifikasi')
        sleep(driver)
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
        driver.find_element(By.ID, "inputStatus").click()

        driver.find_element(By.ID, "belumVerifikasi").click()
        driver.find_element(By.ID, "buttonSearch").click()
        time.sleep(1)
        WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

        driver.find_element(By.CSS_SELECTOR, ".text-yellow-500").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "simpanButton")))
        driver.find_element(By.ID, "status").click()
        driver.find_element(By.ID, "verifikasi").click()
        driver.find_element(By.ID, "keterangan").send_keys("Persetujuan Perwalian")
        driver.find_element(By.CSS_SELECTOR, "#simpanButton > span").click()
        time.sleep(1)
        WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
        Log.info ('Verifikasi berhasil dilakukan oleh Kasie')

        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])
    


@pytest.mark.webtestx
def test_TC_SPPN_019_FilterData():
    print('Kasie melakukan filter data')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "filterKeyword").send_keys("W")
    driver.find_element(By.ID, "buttonSearch").click()
    time.sleep(0.5)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    Log.info ('Filter data Semua berhasil dilakukan oleh Kasie')
 
    
    print('Kasie melakukan filter data Nomor SK')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "nomorSk").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("W")
    driver.find_element(By.ID, "buttonSearch").click()
    time.sleep(0.5)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    Log.info ('Filter data Nomor SK berhasil dilakukan oleh Kasie')
    
    print('Kasie melakukan filter data penandatanganSk')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "penandatanganSk").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("a")
    driver.find_element(By.ID, "buttonSearch").click()
    time.sleep(0.5)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    Log.info ('Filter data Penandatangan SK berhasil dilakukan oleh Kasie')


    # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    # driver.find_element(By.ID, "filterColumn").click()
    # driver.find_element(By.ID, "tglDitetapkan").click()
    # driver.find_element(By.ID, "filterKeyword").send_keys("W")
    # driver.find_element(By.ID, "buttonSearch").click()
    # time.sleep(0.5)
    # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

    print('Kasie melakukan filter data namaWali')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "namaWali").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("a")
    driver.find_element(By.ID, "buttonSearch").click()
    time.sleep(0.5)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    Log.info ('Filter data Nama Wali berhasil dilakukan oleh Kasie')

    print('Kasie melakukan filter data jumlah Narapidana')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "jumlahNarapidana").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("")
    driver.find_element(By.ID, "buttonSearch").click()
    time.sleep(0.5)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    Log.info ('Filter data Jumlah Narapidana berhasil dilakukan oleh Kasie')

@pytest.mark.webtestx
def test_TC_SPPN_020_HalamanDetail():
    sleep(driver)
    print('Kasie melakukan akses halaman detail')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#view0 .h-5").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'backButton')))
