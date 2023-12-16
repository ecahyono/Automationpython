from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_1_SkPerwalian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_SPPN_001_LoginOperator():
    print('Login aplikasi menggunakan akun dengan role Operator')
    Op_SPPN_Sorong(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_SPPN_002_AksesMenuSKPerwalian():
    print('Operator mengakses Operator mengakses submenu SK Perwalian')
    sleep(driver)
    MenuSkPerwalian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')
    attach(data=driver.get_screenshot_as_png())


@pytest.mark.webtest
def test_TC_SPPN_003_InputSK():
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        for i in range(1):
            NoSkFakerLoop                       = "Wi"+ fake.isbn10() + ".PASS" + ".PASS" + random.choice(nums) +".PK." + fake.date_between(start_date='today', end_date='today').strftime('%d.%m.%Y') + "-" + random.choice(nums)
            NamaFakerLoop                       = fake.name()
            TempatPenetapanFakerLoop         = fake.city()

        print('Operator Input no Sk')
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
        driver.find_element(By.ID, "createButton").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "noSk")))
        driver.find_element(By.ID, "noSk").send_keys(NoSkFakerLoop)

        print('Operator Input Penandatangan SK')
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "penandatanganSk")))
        driver.find_element(By.ID, "penandatanganSk").send_keys(NamaFakerLoop)

        driver.find_element(By.ID, "tempatPenetapan").send_keys(TempatPenetapanFakerLoop)
        driver.find_element(By.CSS_SELECTOR, "#tanggalDitetapkan").send_keys(TanggalPenetapanFaker)
        driver.find_element(By.CSS_SELECTOR, "#tanggalDitetapkan").send_keys(Keys.ENTER)


        print('Upload Sk Perwalian')
        sleep(driver)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonUpload")))
        driver.find_element(By.ID, "buttonUpload").click()
        upload(driver)  

        driver.find_element(By.ID, "AddWali").click()

        print('Operator Input Tanggal SK')
        sleep(driver)
        driver.find_element(By.ID, "namaPegawai0").send_keys("a")
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "list0-opt0")))
        driver.find_element(By.ID, "list0-opt0").click()

        # driver.find_element(By.ID, "namaPegawai1").click()
        # driver.find_element(By.ID, "namaPegawai1").send_keys("")
        # WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "list1-opt1")))
        # driver.find_element(By.ID, "list1-opt2").click()

        # driver.find_element(By.ID, "namaPegawai2").send_keys("a")
        # WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "list2-opt6")))
        # driver.find_element(By.ID, "list2-opt6").click()

        # driver.find_element(By.XPATH, "//div[@id='deleteWali2']").click()
        # driver.find_element(By.ID, "namaPegawai0").send_keys(Keys.DOWN)
        # time.sleep(0.5)
        # driver.find_element(By.ID, "namaPegawai0").send_keys(Keys.ENTER)

        print('Operator Click Button Submit SK')

        # driver.find_element(By.ID, "resetButton").click()
        # driver.find_element(By.XPATH, "//span[contains(.,'Ya')]").click()
        driver.find_element(By.ID, "submitButton").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")))
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
        Log.info("Berhasil menambahkan data")
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])

@pytest.mark.webtestx
def test_TC_SPPN_004_FilterData():
    print('Operator Filter Data Berdasarkan No SK')
    sleep(driver)
    driver.find_element(By.ID, "filterColumn").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "noSk")))
    driver.find_element(By.ID, "noSk").click()
    driver.find_element(By.ID, "filterKeyword").send_keys("PAS")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    driver.find_element(By.ID, "filterButton").click()
    time.sleep(1)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail0 .h-5")))

    print('Operator Filter Data Berdasarkan Penandatangan SK')
    sleep(driver)
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.CSS_SELECTOR, "#penandaTanganSk > span").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("A")
    driver.find_element(By.ID, "filterButton").click()
    time.sleep(1)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail0 .h-5")))


    print('Operator Filter Data Berdasarkan Nama')
    sleep(driver)
    driver.find_element(By.ID, "filterColumn").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "nama")))
    driver.find_element(By.ID, "nama").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("")
    driver.find_element(By.ID, "filterButton").click()
    time.sleep(2)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail0 .h-5")))

    print('Operator Filter Data Berdasarkan Pangkat Golongan')
    sleep(driver)
    driver.find_element(By.ID, "filterColumn").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pangkatGolongan > span")))
    driver.find_element(By.CSS_SELECTOR, "#pangkatGolongan > span").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("i")
    driver.find_element(By.ID, "filterButton").click()
    time.sleep(2)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#detail0 .h-5")))


@pytest.mark.webtestx
def test_TC_SPPN_005_AksesHalamanDetail():
    print('Operator Klik Button Detile')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#detail0 .h-5").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "previewSK")))

    driver.find_element(By.CSS_SELECTOR, '#backButton > span').click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    Log.info("Berhasil menampilkan detail data")

@pytest.mark.webtestx
def test_TC_SPPN_006_AksesHalamanUbah():
    print('Operator Klik Button Ubah')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#edit0 path").click()
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButton")))

@pytest.mark.webtestx
def test_TC_SPPN_007_EditData():
    print('Operator Ubah Data')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButton")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonUpload")))

    driver.find_element(By.ID, "penandatanganSk").clear()
    driver.find_element(By.ID, "penandatanganSk").send_keys(NamaFaker)

    driver.find_element(By.ID, "buttonUpload").click()
    upload(driver)

    driver.find_element(By.ID, "submitButton").click()

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Berhasil Diperbaharui')]")))
    
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "filterButton")))
    Log.info("Berhasil mengubah data")
    
@pytest.mark.webtestx
def test_TC_SPPN_008_DeleteData():
    print('Operator Hapus data')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".text-red-500 .h-5").click()
    driver.find_element(By.XPATH, "//span[contains(.,'Ya')]").click()
    Log.info("Berhasil menghapus data")
    quit(driver)

