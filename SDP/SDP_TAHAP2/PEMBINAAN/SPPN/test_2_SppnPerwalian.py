from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_2_PerwalianSPPN.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtestx
def test_TC_SPPN_009_LoginOperator():
    print('Login aplikasi menggunakan akun dengan role Operator')
    Op_SPPN(driver)
    Log.info("Berhasil login dan menu yang ditampilkan sesuai hak akses role operator")
    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtestx
def test_TC_SPPN_010_AksesMenuTimPerwalian():
    print('Operator mengakses Operator mengakses submenu Tim Perwalian')
    sleep(driver)
    MenuSPPNPerwalian(driver)
    Log.info ('Menampilkan index halaman Tim Perwalian berikut dengan data pada tabel yang sesuai')

    attach(data=driver.get_screenshot_as_png())

@pytest.mark.webtestx
def test_TC_SPPN_011_InputTimPerwalian():
    driver.implicitly_wait(20)
    sleep(driver)

    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    SkPerwalianLoop = ['opt0','opt2','opt3','opt4','opt5','opt6']
    checkboxPeseeta1Loop = ['#check0 .el-checkbox__inner','#check1 .el-checkbox__inner','#check2 .el-checkbox__inner','#check3 .el-checkbox__inner','#check4 .el-checkbox__inner','#check5 .el-checkbox__inner']
    checkboxPeseeta2Loop = ['#check6 .el-checkbox__inner','#check7 .el-checkbox__inner','#check8 .el-checkbox__inner','#check9 .el-checkbox__inner']
    while condition:
        for i in range(1):
            SkPerwalianFakerLoop         = random.choice(SkPerwalianLoop)
            checkboxPeseta1FakerLoop    = random.choice(checkboxPeseeta1Loop)
            checkboxPeseta2FakerLoop    = random.choice(checkboxPeseeta2Loop)



        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, 'createButton')))

        print('Operator klick button tambah')
        driver.find_element(By.ID, "createButton").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "submitButton")))
        
        print('Input No sk')
        driver.find_element(By.ID, "noSk").click()
        driver.find_element(By.ID, ""+SkPerwalianFakerLoop+"").click()

        print('Clik Form Input Wali')
        driver.find_element(By.ID, "namaPegawai0").send_keys("a")
        # WebDriverWait(driver, 100).until(EC.invisibility_of_element_located((By.LINK_TEXT, "Memuat")))
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="namaPegawai0-opt0"]')))
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="namaPegawai0-opt0"]').click()

        

        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, ".w-5 > svg").click()
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#filterButton > span")))

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ""+checkboxPeseta1FakerLoop+"").click()
        driver.find_element(By.CSS_SELECTOR, ""+checkboxPeseta2FakerLoop+"").click()
        driver.find_element(By.ID, "pilihWbp").click()

        driver.find_element(By.ID, "submitButton").click()
        driver.find_element(By.XPATH, "//p[contains(.,'Berhasil Ditambahkan')]")
        Log.info('SK Perwalian Berhasil Ditambahkan')
        vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
        condition = driver.execute_script("return (arguments[0]<10)", vars["x"])


@pytest.mark.webtest
def test_TC_SPPN_012_FilterData():
    print('Operator Search data Tim Perwalian')
    sleep(driver)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    driver.find_element(By.ID, "filterKeyword").send_keys("a")
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    Log.info('Operator berhasil Search Data Tim Perwalian')

    print('Operator Search data Nomor SK')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "nomorSk").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("")
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    Log.info('Operator berhasil Search Data SK Tim Perwalian')

    print('Operator Search data penandatanganSk')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "penandatanganSk").click()
    driver.find_element(By.ID, "filterKeyword").send_keys("a")
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    Log.info('Operator berhasil Search Data penandatanganSk Tim Perwalian')


    print('Operator Search data namaWali')  
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "namaWali").click()
    driver.find_element(By.ID, "filterKeyword").clear()
    driver.find_element(By.ID, "filterKeyword").send_keys("")
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    Log.info('Operator berhasil Search Data namaWali Tim Perwalian')


    print('Operator Search data status sudahVerifikasi')
    driver.find_element(By.ID, "filterStatus").click()
    driver.find_element(By.ID, "sudahVerifikasi").click()
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    Log.info('Operator berhasil Search Data status sudahVerifikasi Tim Perwalian')

    print('Operator Search data status sudahOtorisasi')
    driver.find_element(By.ID, "filterStatus").click()
    driver.find_element(By.ID, "sudahOtorisasi").click()
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    Log.info('Operator berhasil Search Data status sudahOtorisasi Tim Perwalian')

    print('Operator Search data status revisi')
    driver.find_element(By.ID, "filterStatus").click()
    driver.find_element(By.ID, "revisi").click()
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    Log.info('Operator berhasil Search Data status revisi Tim Perwalian')

    print('Operator Search data status')
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    driver.find_element(By.ID, "filterStatus").click()
    driver.find_element(By.ID, "belumVerifikasi").click()
    driver.find_element(By.ID, "buttonFitler").click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    Log.info('Operator berhasil Search Data status Tim Perwalian')
@pytest.mark.webtest
def test_TC_SPPN_013_AksesHalamanDetail():
    print('Operator mengakses halaman Detail Tim Perwalian')
    sleep(driver)
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "buttonFitler")))
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#detail0 .h-5").click()
    # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__content')))
    input('Press ENTER to continue after page loaded...')
    driver.find_element(By.ID, "backButton").click()
    Log.info('Operator berhasil mengakses halaman Detail Tim Perwalian')


@pytest.mark.webtest
def test_TC_SPPN_014_AksesHalamanUbah():
    print('Operator mengakses halaman Ubah Tim Perwalian')
    sleep(driver)

    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    Log.info('Operator berhasil mengakses halaman Ubah Tim Perwalian')



@pytest.mark.webtest
def test_TC_SPPN_015_EditData():
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

    



