from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_2_SyaratRemisi.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtest
def test_TC_REM_009_loginPusat():
    print('Login aplikasi menggunakan akun dengan role pusat')
    PusatRemisi(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role Pusat")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_REM_010_AksesMenu():
    print('Operator mengakses submenu Syarat Remisi')
    sleep(driver)
    MenuSyaratRemisiLainLain(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_REM_011_InputData():
    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        peraturanPPWBP                            = ["Peraturan Menteri No. 7/2022","Peraturan Menteri No. 3/2018","Keputusan Presiden No. 120/1955"]
        JenisRemSyaratWBL                         = ["Remisi Dasawarsa","Remisi Umum","Remisi Kepramukaan","Non suscipit veritatis.","Natus ut quasi."]
        KategoriRemisiWBP                         = ["Kategori1","Kategori2","Kategori3",'Kategori4','Kategori0']
        for i in range(1):
            peraturanPPWBPLoop                    = random.choice(peraturanPPWBP)
            JenisRemSyaratWBPLoop                 = random.choice(JenisRemSyaratWBL)
            KategoriRemisiWBPLoop                 = random.choice(KategoriRemisiWBP)

        worksheet.append([

            peraturanPPWBPLoop,
            JenisRemSyaratWBPLoop
        
            ])
        workbook.save(file_path)


        print('Operator klick button tambah')
        driver.implicitly_wait(20)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
        driver.find_element(By.CSS_SELECTOR, "#createButton svg").click()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))

        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "jenisPer")))
        driver.find_element(By.ID, "jenisPer").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//li[contains(.,\'"+peraturanPPWBPLoop+"\')]").click()

        driver.find_element(By.ID, "jenisRem").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+JenisRemSyaratWBPLoop+"')]" )))
        driver.find_element(By.XPATH, "//li[contains(.,\'"+JenisRemSyaratWBPLoop+"')]").click()


        driver.find_element(By.ID, "dropdownKategori").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[@id=\'"+KategoriRemisiWBPLoop+"\']")))
        driver.find_element(By.XPATH, "//li[@id=\'"+KategoriRemisiWBPLoop+"\']").click()


        driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'"+ JenisRegistrasiWBPExcel +"')]" )))
        driver.find_element(By.XPATH, "//li[contains(.,\'"+ JenisRegistrasiWBPExcel +"')]").click()
        driver.find_element(By.CSS_SELECTOR, ".el-select__input").click()

        driver.find_element(By.ID, "op1").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+OperatorExcel+"")))
        driver.find_element(By.ID, ""+OperatorExcel+"").click()
        driver.find_element(By.CSS_SELECTOR, "#menjalaniPidana .el-input__inner").click()
        driver.find_element(By.CSS_SELECTOR, "#menjalaniPidana .el-input__inner").send_keys(MenjalaniPidanaExcel)
        driver.find_element(By.ID, "menjalaniPidanaWaktu").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+DropHariExcel+"")))
        driver.find_element(By.ID, ""+DropHariExcel+"").click()

        driver.find_element(By.ID, "peraturanPP").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+SudahPutusanExcel+"")))
        time.sleep(0.5)
        driver.find_element(By.ID, ""+SudahPutusanExcel+"").click()
        
        driver.find_element(By.ID, "berkelakuanBaik").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+BerkelaunBaikExcel+"")))
        driver.find_element(By.ID, ""+BerkelaunBaikExcel+"").click()
        driver.find_element(By.CSS_SELECTOR, "#KelakuanBaikBilangan .el-input__inner").click()
        driver.find_element(By.CSS_SELECTOR, "#KelakuanBaikBilangan .el-input__inner").send_keys(KelakuanBaikBilanganExcel)
        driver.find_element(By.ID, "KelakuanBaikWaktu").click()
        driver.find_element(By.ID, ""+KelakuanBaikWaktu+"").click()

        driver.find_element(By.ID, "SyaratUsia").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+SyaratUsiAExcel+"")))
        driver.find_element(By.ID, ""+SyaratUsiAExcel+"").click()

        driver.find_element(By.ID, "asalSk").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,""+AsalSKExcel+"")))
        driver.find_element(By.ID, ""+AsalSKExcel+"").click()

        driver.find_element(By.ID, "MelunasiDenda").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+MelunasiDendaExcel+"")))
        driver.find_element(By.ID, ""+MelunasiDendaExcel+"").click()

        driver.find_element(By.ID, "lamaRemisi").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,  ""+LamaRemisiExcel+"")))
        driver.find_element(By.ID, ""+LamaRemisiExcel+"").click()

        driver.find_element(By.ID, "submitButton").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
        Log.info("Berhasil input data Syarat Remisi")

        attach(data=driver.get_screenshot_as_png())
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])

@pytest.mark.webtest
def test_TC_REM_012_FilterData():
    print('Operator Filter Data')
    driver.implicitly_wait(20)
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
    driver.find_element(By.ID, "keyword").send_keys("a")
    driver.find_element(By.ID, "btnFilter").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#deleteButton0 .h-5")))
    attach(data=driver.get_screenshot_as_png())
   
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
    driver.find_element(By.ID, "column").click()
    driver.find_element(By.ID, "jenisRemisi").click()
    driver.find_element(By.ID, "keyword").send_keys("a")
    driver.find_element(By.ID, "btnFilter").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#deleteButton0 .h-5")))
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
    driver.find_element(By.ID, "column").click()
    driver.find_element(By.ID, "jenisPermen").click()
    driver.find_element(By.ID, "keyword").send_keys("a")
    driver.find_element(By.ID, "btnFilter").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#deleteButton0 .h-5")))
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
    driver.find_element(By.ID, "column").click()
    driver.find_element(By.ID, "kategNarapidana").click()
    driver.find_element(By.ID, "keyword").send_keys("a")
    driver.find_element(By.ID, "btnFilter").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#deleteButton0 .h-5")))
    attach(data=driver.get_screenshot_as_png())
    Log.info("Menampilkan data sesuai filter yang diinputkan")



@pytest.mark.webtest
def test_TC_REM_013_Detail():
    sleep(driver)
    print('Operator Klik Detail')
    driver.find_element(By.CSS_SELECTOR, "#detailButton0 .h-5").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
    time.sleep(5)
    driver.find_element(By.ID, "backButton").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtest
def test_TC_REM_014_Edit():
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
        sleep(driver)
        print('Operator Klik Edit')
        driver.find_element(By.CSS_SELECTOR, "#updateButton0 .h-5").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        driver.find_element(By.ID, "peraturanPP").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+SudahPutusanExcel+"")))
        time.sleep(0.5)
        driver.find_element(By.ID, ""+SudahPutusanExcel+"").click()
        driver.find_element(By.ID, "submitButton").click()
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "btnFilter")))
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<2)", vars["x"])