from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_WaktuRemisi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_REM_001_LoginPusat():
    print('Login aplikasi menggunakan akun dengan role pusat')
    PusatRemisi(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Pusat")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_REM_002_AksesMenu():
    print('Operator mengakses Operator mengakses submenu Pemberian Remisi')
    sleep(driver)
    MenuWaktuRemisiLainLain(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_REM_003_TambahPemberianRemisi():
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        namaRemisiRemisiWBP                         = ["namaRemisi1","namaRemisi2","namaRemisi3",'namaRemisi4','namaRemisi0']
        for i in range(1):
            NamaRemisiLoop                = random.choice(namaRemisiRemisiWBP)
            TanggalPemberianRemisiLoop    = fake.date_between(start_date='-1years', end_date='today').strftime('%d.%m.%Y')
            CatatanLoop                   = fake.text(max_nb_chars=200)

        worksheet.append([

            NamaRemisiLoop,
            TanggalPemberianRemisiLoop,
            CatatanLoop
        
            ])
        workbook.save(file_path)




        print('pusat Pusat menambahkan data tim Pemberian Remisi')
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, "#createButton > span").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))

        driver.find_element(By.ID, "Namaremisi").click()
        time.sleep(0.5)
        driver.find_element(By.ID, ""+NamaRemisiLoop+"").click()
        
        driver.find_element(By.ID, "tanggalPemberian").send_keys(TanggalPemberianRemisiLoop)

        driver.find_element(By.ID, "catatan").send_keys(CatatanLoop)

        driver.find_element(By.ID, "submitButton").click()
       
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

        Log.info ('Berhasil mengisi form tambah Pemberian Remisi')

        attach(data=driver.get_screenshot_as_png())
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])

@pytest.mark.webtest
def test_TC_REM_004_SearchData():
    time.sleep(2)
    print('Pusat Search data index Semua')
    sleep(driver)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "semua").click()
    driver.find_element(By.ID, "keyword").send_keys("a")
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
    driver.find_element(By.ID, "namaRemiFilter").click()
    driver.find_element(By.ID, "keyword").clear()
    driver.find_element(By.ID, "keyword").send_keys("a")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data index Peraturan PP')

    print('Pusat Search data index Tahun Pemberian Remisi')
    time.sleep(1)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "TahunFilter").click()
    driver.find_element(By.ID, "filterTahun").send_keys("2023")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data Tahun Pemberian Remisi')

    print('Pusat Search data Agama')
    time.sleep(1)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "AgamaFil").click()
    driver.find_element(By.ID, "keyword").clear()
    driver.find_element(By.ID, "keyword").send_keys("i")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data index Peraturan PP')

    print('Pusat Search data Catatan')
    time.sleep(1)
    driver.find_element(By.ID, "column").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "catatanFil").click()
    driver.find_element(By.ID, "keyword").clear()
    driver.find_element(By.ID, "keyword").send_keys("i")
    driver.find_element(By.ID, "buttonCari").click()
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    time.sleep(0.5)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 path")))
    Log.info ('Berhasil search data index Catatan')


@pytest.mark.webtest
def test_TC_REM_005_HalamanDetail():
    print('Pusat mengakses Halaman Detail Pemberian Remisi')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, '#detailButton0 .h-5').click()
    time.sleep(2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
    driver.find_element(By.ID, "backButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))

    Log.info ('Berhasil mengakses halaman detail Pemberian Remisi')

@pytest.mark.webtest
def test_TC_REM_006_HalamanEdit():
    print('Pusat mengakses Halaman Edit Pemberian Remisi')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, '#updateButton0 .h-5').click()
    time.sleep(2)

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton"))) 

    Log.info ('Berhasil mengakses halaman Edit Pemberian Remisi')

@pytest.mark.webtest
def test_TC_REM_007_EditData():
    print('Pusat Mengubah Data Pemberian Remisi')
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))

    driver.find_element(By.ID, "catatan").send_keys(" EDIT DATA")
    driver.find_element(By.ID, "submitButton").click()

    Log.info ('Berhasil mengubah data Pemberian Remisi')

@pytest.mark.webtest
def test_TC_REM_008_DeleteData():
    print('Pusat Menghapus Data Pemberian Remisi')
    sleep(driver)

    driver.find_element(By.ID, "hapusButton0").click()
    driver.find_element(By.XPATH, "//button[contains(.,'OK')]").click()
    time.sleep(1)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonCari")))
    

    Log.info ('Berhasil menghapus data Pemberian Remisi')








