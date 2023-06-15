from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_2_KasieVerifikasi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test_TC_SPPN_008():
    print('Login aplikasi menggunakan akun dengan role Kasie')
    kasie_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Kasie")

@pytest.mark.webtest
def test_TC_SPPN_009():
    print('Kasie mengakses submenu Persetujuan Perwalian')
    sleep(driver)
    MenuSPPNPerwalianPersetujuan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

@pytest.mark.webtest
def test_TC_SPPN_010():
    # WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".circular")))
    sleep(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.el-table__row:nth-child(1) a .h-5')))
    # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div/label/div/div/div/input').click()
    # driver.find_element(By.XPATH, "//li[contains(.,'Nomor SK')]").click()
    # driver.find_element(By.CSS_SELECTOR, ".el-input--prefix > .el-input__inner").send_keys(NoSkFaker)
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".space-x-2 > .el-button > span")))
    # driver.find_element(By.CSS_SELECTOR, ".space-x-2 > .el-button > span").click()
    # time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".text-yellow-500").click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-table__row > .el-table_4_column_20 > .cell")))
    driver.find_element(By.CSS_SELECTOR, ".el-input--large > .el-input__inner").click()
    driver.find_element(By.XPATH, "//div[6]/div/div/div/ul/li[2]").click()
    driver.find_element(By.CSS_SELECTOR, "#simpanButton > span").click()
    driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("Persetujuan Perwalian")
    WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Ditambahkan')]")))




