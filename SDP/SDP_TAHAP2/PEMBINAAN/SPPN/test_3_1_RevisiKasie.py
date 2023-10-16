from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_2_RevisiKasie.txt', mode="w")
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
def test_TC_SPPN_018_KasieMelakukanRevisi():

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    driver.find_element(By.ID, "inputStatus").click()

    driver.find_element(By.ID, "belumVerifikasi").click()
    driver.find_element(By.ID, "buttonSearch").click()
    time.sleep(1)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

    driver.find_element(By.CSS_SELECTOR, ".text-yellow-500").click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "simpanButton")))
    driver.find_element(By.ID, "status").click()
    driver.find_element(By.XPATH, "(//li[@id='revisi'])[2]").click()
    driver.find_element(By.ID, "keterangan").send_keys("revisi Perwalian")
    driver.find_element(By.CSS_SELECTOR, "#simpanButton > span").click()
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Ditambahkan')]")))
    Log.info ('Revisi berhasil dilakukan oleh Kasie')

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
    LogOut(driver)

@pytest.mark.webtestx
def test_TC_SPPN_019_LoginOperator():
    sleep(driver)
    print('Login aplikasi menggunakan akun dengan role operator')
    Op_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")


@pytest.mark.webtestx
def test_TC_SPPN_020_AksesMenuTimPerwalian():
    sleep(driver)
    print('Operator mengakses Operator mengakses submenu Tim Perwalian')
    MenuSPPNPerwalian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    sleep(driver)
    print('Operator mengakses halaman Ubah Tim Perwalian')
    sleep(driver)
    print('Operator Search data status')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    driver.find_element(By.ID, "filterStatus").click()
    driver.find_element(By.ID, "revisi").click()
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    Log.info('Operator berhasil Search Data status Tim Perwalian')

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    Log.info('Operator berhasil mengakses halaman Ubah Tim Perwalian')

@pytest.mark.webtestx
def test_TC_SPPN_021_UbahTimPerwalian():
    sleep(driver)
    print('Operator mengubah data Tim Perwalian')

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "backButton")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    time.sleep(1)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-5 > svg")))
    driver.find_element(By.CSS_SELECTOR, ".w-5 > svg ").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#filterButton svg")))
    time.sleep(1)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ""+checkboxPeseeta1Excell+"")))
    driver.find_element(By.CSS_SELECTOR, ""+checkboxPeseeta1Excell+"").click()
    driver.find_element(By.CSS_SELECTOR, ""+checkboxPeseeta2Excell+"").click()
    driver.find_element(By.CSS_SELECTOR, "#pilihWbp > span").click()

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Menambahkan Narapidana Baru')]")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    driver.find_element(By.CSS_SELECTOR, "#submitButton svg").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Diperbaharui')]")))
    Log.info('Operator berhasil mengubah data Tim Perwalian')

    quit(driver)

    



    


