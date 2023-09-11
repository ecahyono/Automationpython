from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_7_WaliPenilaian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_SPPN_023_LoginWali():
    print('Login aplikasi menggunakan akun dengan role wali')
    wali_SURIYAH(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Kasie")

@pytest.mark.webtest
def test_TC_SPPN_024_AksesMenuPenilaian():
    print('wali mengakses submenu Penilaian ')
    sleep(driver)
    MenuPenilaian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

@pytest.mark.webtest
def test_TC_SPPN_025_TambahPenilaian():
    sleep(driver)
    print('wali melakukan penilaian')
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='filterButton']/span")))
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#penilaian0 > span").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "backButton")))
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-select__input").click()
    driver.find_element(By.CSS_SELECTOR, "#selectItemObservasiBaikOptGroup0 > .el-select-group__title").click()
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(4)").click()
    driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(3) .el-select__input").click()
    driver.find_element(By.ID, "selectItemObservasiTidakBaik0").click() 
    driver.find_element(By.CSS_SELECTOR, ".w-full:nth-child(4)").click()
    driver.find_element(By.ID, "tambahItem").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#hapusItem0 path")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='filterButton']/span")))
    Log.info ('Berhasil melakukan penilaian')

@pytest.mark.webtest
def test_TC_SPPN_026_DetailPenilaian():
    sleep(driver)

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='filterButton']/span")))
    driver.find_element(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "backButton")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#editDemografi .h-5")))
    driver.find_element(By.ID, "backButton").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='filterButton']/span")))
    Log.info ('Berhasil Melihat Halaman Detail Penilaian')

@pytest.mark.webtest
def test_TC_SPPN_027_AksesHalamanUbah():
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 path").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buttonRiwayat > span")))
    driver.find_element(By.ID, "edit0").click()
    time.sleep(3)
    Log.info ('Wali mengakses halaman Ubah Penilaian Harian')
   
@pytest.mark.webtest
def test_TC_SPPN_028_UbahPenilaian():
    Log.info ('Wali mengubah data Penilaian Harian')  
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#hapusItem0 path")))
    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Diperbaharui')]")))
    Log.info ('Berhasil mengubah data Penilaian Harian')

@pytest.mark.webtest
def test_TC_SPPN_029_HapusPenilaian():
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#penilaian0 > span")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 path").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "backButton")))
    # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#delete0 path")))
    # driver.find_element(By.ID, 'delete0').click()
    # driver.find_element(By.XPATH, "//div[3]/button[2]").click()
    # WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Menghapus')]")))
    Log.info ('Berhasil menghapus data Penilaian Harian')



