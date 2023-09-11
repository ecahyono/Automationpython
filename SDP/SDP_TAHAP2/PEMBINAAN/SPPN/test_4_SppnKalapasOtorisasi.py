from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_6_KalapasOtorisasi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test_TC_SPPN_036():
    print('Login aplikasi menggunakan akun dengan role Kasie')
    Kalapas_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Kasie")

@pytest.mark.webtest
def test_TC_SPPN_037():
    print('Kasie mengakses submenu Persetujuan Perwalian')
    sleep(driver)
    MenuSPPNPerwalianPersetujuan(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

@pytest.mark.webtest
def test_TC_SPPN_038():
    
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        # Status   = ['Revisi','Verifikasi']
        Status   = ['Revisi']
        for i in range(1):
            StatusFaker                = random.choice(Status)

        
    
            print('Kasie melakukan verifikasi')
            sleep(driver)
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))
            driver.find_element(By.ID, "inputStatus").click()

            driver.find_element(By.ID, "sudahVerifikasi").click()
            driver.find_element(By.ID, "buttonSearch").click()
            time.sleep(1)
            WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonSearch')))

            driver.find_element(By.CSS_SELECTOR, ".text-yellow-500").click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "simpanButton")))
            driver.find_element(By.ID, "status").click()
            driver.find_element(By.ID, "diSetujui").click()
            driver.find_element(By.ID, "keterangan").send_keys("Persetujuan Perwalian kalapas otorisasi")
            driver.find_element(By.CSS_SELECTOR, "#simpanButton > span").click()
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Memperbarui data')]")))
            WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
            Log.info ('Verifikasi berhasil dilakukan oleh Kasie')
            input('Press ENTER to continue')
    
      

        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])