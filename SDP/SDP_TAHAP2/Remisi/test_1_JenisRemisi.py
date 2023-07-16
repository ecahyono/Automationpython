from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_JenisRemisi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtestx
def test_TC_REM_001():
    print('Login aplikasi menggunakan akun dengan role pusat')
    PusatRemisi(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Pusat")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtestx
def test_TC_REM_002():
    print('Operator mengakses Operator mengakses submenu Jenis Remisi')
    sleep(driver)
    MenuJenisRemisiLainLain(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtestx
def test_TC_REM_003():
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        for i in range(1):
            JenisRemisiFakerLoop                = fake.text(max_nb_chars=25)

        worksheet.append([

            JenisRemisiFakerLoop
        
            ])
        workbook.save(file_path)




        print('pusat Pusat menambahkan data tim Jenis Remisi')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, "#createButton > span").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))

        #Input Peraturan PP
        driver.find_element(By.ID, "peraturanPP").click()
        driver.find_element(By.XPATH, "//li[contains(.,\'"+peraturanPPExcel+"\')]").click()

        #input Jenis Remisi
        driver.find_element(By.ID, "jenisRemisi").send_keys(JenisRemisiFakerLoop)

        #input Keterangan
        driver.find_element(By.ID, "keterengan").send_keys(KeteranganExcel)
        time.sleep(1)
        driver.find_element(By.ID, "submitButton").click()

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

        Log.info ('Berhasil mengisi form tambah jenis remisi')

        attach(data=driver.get_screenshot_as_png())
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<4)", vars["x"])

@pytest.mark.webtest
def test_TC_REM_004():
    time.sleep(2)
    print('Pusat Search data index Semua')
    sleep(driver)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "semua").click()
    driver.find_element(By.ID, "keyword").send_keys("Kepres")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data index Semua')


    print('Pusat Search data index Peraturan PP')
    time.sleep(1)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//li[@id='peraturanPerundang']/span").click()
    driver.find_element(By.ID, "keyword").clear()
    driver.find_element(By.ID, "keyword").send_keys("kepres")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data index Peraturan PP')

    print('Pusat Search data index jenis Remisi')
    time.sleep(1)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "jenisRemi").click()
    driver.find_element(By.ID, "keyword").clear()
    driver.find_element(By.ID, "keyword").send_keys("a")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data index jenis Remisi')

@pytest.mark.webtest
def test_TC_REM_005():
    print('Pusat mengakses Halaman Detail Jenis Remisi')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="detailButton0"]').click()
    time.sleep(2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
    driver.find_element(By.ID, "backButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

    Log.info ('Berhasil mengakses halaman detail Jenis Remisi')

@pytest.mark.webtest
def test_TC_REM_006():
    print('Pusat mengakses Halaman Edit Jenis Remisi')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="UpdateButton0"]').click()
    time.sleep(2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
    driver.find_element(By.ID, "backButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

    Log.info ('Berhasil mengakses halaman Edit Jenis Remisi')

@pytest.mark.webtest
def test_TC_REM_007():
    print('Pusat Mengubah Data Jenis Remisi')
    sleep(driver)

    driver.find_element(By.CSS_SELECTOR, "#UpdateButton0 .h-5").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))

    #Input Peraturan PP
    driver.find_element(By.ID, "peraturanPP").click()
    driver.find_element(By.XPATH, "//li[contains(.,\'"+peraturanPPExcel+"\')]").click()

    #input Jenis Remisi
    driver.find_element(By.ID, "jenisRemisi").send_keys("EDIT")

    #input Keterangan
    driver.find_element(By.ID, "keterengan").send_keys(KeteranganExcel)
    driver.find_element(By.ID, "submitButton").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

    Log.info ('Berhasil mengubah data Jenis Remisi')

@pytest.mark.webtest
def test_TC_REM_008():
    print('Pusat Menghapus Data Jenis Remisi')
    sleep(driver)

    driver.find_element(By.CSS_SELECTOR, "#DeleteButton0 .h-5").click()
    driver.find_element(By.XPATH, "//button[contains(.,'Ya')]").click()
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    

    Log.info ('Berhasil menghapus data Jenis Remisi')








