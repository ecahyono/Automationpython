from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_MenuPenilaianPembinaan.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_SPPN_001():
    print('Login aplikasi menggunakan akun dengan role pusat')
    Op_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_SPPN_002():
    print('Operator mengakses Operator mengakses submenu Tim Perwalian')
    sleep(driver)
    MenuSPPNPerwalian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_SPPN_003():
    sleep(driver)

    for row in worksheet.iter_rows(min_row=1, values_only=True):
        NoSkExcel                            = row[0]
        NamaExcel                            = row[1]
        PegawaiExcel                         = row[2]
    print(PegawaiExcel)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Cari')]")))
    print('Operator klick button tambah')
    driver.find_element(By.ID, "createButton").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//td[2]/div/div/div/div/input")))
    
    print('Input No sk')
    driver.find_element(By.ID, "nomor_sk").send_keys(NoSkExcel)

    print('Input Penandatangan sk')
    driver.find_element(By.ID, "penandatangan_sk").send_keys(NamaFaker)
    driver.find_element(By.XPATH, "//h1[contains(.,'Wali *')]").click()
    input("")

    print('Clik Form Input Wali')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//td[2]/div/div/div/div/input")))
    driver.find_element(By.XPATH, "//td[2]/div/div/div/div/input").click()
  
    
    print('Input Nama Wali')
    # driver.find_element(By.XPATH, "//td[2]/div/div/div/div/input").send_keys(PegawaiExcel)
    # time.sleep(0.5)

    driver.find_element(By.XPATH, "//td[2]/div/div/div/div/input").send_keys(Keys.DOWN)
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//td[2]/div/div/div/div/input").send_keys(Keys.ENTER)
    time.sleep(0.5)

    # WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(.,"+PegawaiExcel+")]")))
    # time.sleep(1)
    # driver.find_element(By.XPATH, "//td[contains(.,"+PegawaiExcel+")]").click()

    print('Tambah WBP')
    driver.find_element(By.XPATH, "//h1[contains(.,'Narapidana *')]").click()
    nav1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div[2]/div[1]/div[2]/table/thead/tr/th[6]')
    ActionChains(driver).move_to_element(nav1).perform()
    nav1.click()
    print('pilih Nama Narapidana')
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-checkbox__inner").click()
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(2) .el-checkbox__inner").click()


    driver.find_element(By.XPATH, "//button[contains(.,'Pilih')]").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Ditambahkan')]")))
    LogOut(driver)

@pytest.mark.webtest
def test_TC_SPPN_004():
    print('Operator mengakses halaman Detail Tim Perwalian')

@pytest.mark.webtest
def test_TC_SPPN_005():
    print('Operator mengakses halaman Ubah Tim Perwalian')

@pytest.mark.webtest
def test_TC_SPPN_006():
    print('Operator mengubah data Tim Perwalian')

@pytest.mark.webtest
def test_TC_SPPN_007():
    print('Operator menghapus data Tim Perwalian')
 

def exit():
    driver.quit()

    



