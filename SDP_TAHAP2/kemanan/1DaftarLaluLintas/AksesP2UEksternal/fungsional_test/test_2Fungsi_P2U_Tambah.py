from distutils.archive_util import make_archivefrom selenium import webdriverfrom selenium.webdriver.support.ui import WebDriverWaitfrom selenium.webdriver.support import expected_conditions as ECfrom selenium.webdriver.common.by import Byfrom selenium.common.exceptions import TimeoutExceptionfrom selenium.webdriver import ActionChainsfrom selenium.webdriver.common.keys import Keysfrom selenium.webdriver.chrome.service import Servicefrom selenium.webdriver.support.select import Selectimport platformfrom pytest import markimport timefrom pytest_html_reporter import attachimport sysfrom os import environ, pathfrom dotenv import load_dotenvload_dotenv()from openpyxl import load_workbookif platform.system() == 'Darwin':    sys.path.append(environ.get("MACPARENTDIR"))    wb = load_workbook(filename=r"/Users/will/Documents/work/Automationpython/Filexel/Keamanan.xlsx")    sys.path.append(environ.get("MACEXCELDIR"))elif platform.system() == 'Windows':    sys.path.append(environ.get("WINPARENTDIR"))    sys.path.append(environ.get("WINEXCELDIR"))from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep, waituntillfrom Settings.login import loginimport loggingLog = logging.getLogger(__name__)log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'fh = logging.FileHandler('Fungsi_P2U_Input.log', mode="w")fh.setLevel(logging.INFO)formatter = logging.Formatter(log_format)fh.setFormatter(formatter)Log.addHandler(fh)sheetrange = wb['Fungsi_P2U_Input']print("1.pegawai 2.Tamu Dinas")xr = input("")i = xrinputKategori                       = sheetrange['B' + str(i)].valueNamaAtauNip                         = sheetrange['C' + str(i)].valueinputNip                            = sheetrange['D' + str(i)].valueinputNama                           = sheetrange['E' + str(i)].valueinputJabatan                        = sheetrange['F' + str(i)].valueInputInstansi                       = sheetrange['G' + str(i)].valueinputKeperluan                      = sheetrange['H' + str(i)].valueKunjunganOnsite                     = sheetrange['I' + str(i)].valueKunjunganOnline                     = sheetrange['J' + str(i)].value@mark.fixture_test()def test_1_SetupOS():    global driver, pathData    driver = initDriver()    pathData = loadDataPath()@mark.fixture_test()def test_2_Login():    login(driver)@mark.fixture_test()# Akses menu ke halaman akses pintu p2udef test_3_Akses_menu():        sleep(driver)    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])    ActionChains(driver).move_to_element(nav1).perform()    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])    time.sleep(1)    ActionChains(driver).move_to_element(element2).perform()    time.sleep(1)    driver.find_element(By.LINK_TEXT, 'Akses Pintu P2U').click()    print('.')    Log.info('akses menu daftar lalu lintas')    attach(data=driver.get_screenshot_as_png())# ==================================================== TAMBAH PEGAWAI ====================================================@mark.fixture_test()# pergi ke halaman tambahdef test_4_ButtonTambah_PegawaiTambah():        sleep(driver)    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))    print('.')    Log.info(' Membuka Halaman Tambah ')    attach(data=driver.get_screenshot_as_png())@mark.fixture_test()# Memilih kategori pegawaidef test_5_Input():    driver.implicitly_wait(30)    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="inputKategori"]')))    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()    if inputKategori == 'Pegawai':        driver.find_element(By.ID, "pegawai").click()        driver.find_element(By.ID, 'inputSearch').send_keys(NamaAtauNip)        if driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label'):            driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)        else:            driver.find_element(By.ID, 'inputNip').click()            driver.find_element(By.ID, 'inputNip').send_keys(inputNip)            Log.info(' Input NIP ')            sleep(driver)            attach(data=driver.get_screenshot_as_png())            driver.find_element(By.ID, 'inputNama').send_keys(inputNama)            Log.info(' Input Nama ')            sleep(driver)            attach(data=driver.get_screenshot_as_png())            driver.find_element(By.ID, 'inputJabatan').send_keys(inputJabatan)            Log.info(' Input Jabatan ')            sleep(driver)            attach(data=driver.get_screenshot_as_png())            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)            Log.info(' Input Keperluan ')            sleep(driver)            attach(data=driver.get_screenshot_as_png())    elif inputKategori == 'Tamu Dinas':        driver.find_element(By.ID, "tamuDinas").click()        Log.info(' Memilih Kategori Tamu Dinas ')        driver.find_element(By.ID, 'inputSearch').send_keys(NamaAtauNip)        Log.info(' Cari Nama atau Nip Kategori Tamu Dinas ')        attach(data=driver.get_screenshot_as_png())        if driver.find_elements(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label'):            driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(1) > .el-descriptions__label').click()            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)        else:            driver.find_element(By.ID, 'inputNip').send_keys(inputNip)            sleep(driver)            driver.find_element(By.ID, 'inputNama').send_keys(inputNama)            sleep(driver)            driver.find_element(By.ID, 'inputInstansiId').send_keys(InputInstansi)            if InputInstansi == "POLRES BANDUNG":                driver.find_element(By.CSS_SELECTOR, '#optionInstansi0').click()            elif InputInstansi == "POLDA JABAR":                driver.find_element(By.ID, '//div[contains(.,\'POLDA JABAR\')]').click()            elif InputInstansi == "POLRES MAGELANG":                driver.find_element(By.ID, '//div[contains(.,\'POLRES MAGELANG\')]').click()            sleep(driver)            driver.find_element(By.ID, 'inputJabatan').send_keys(inputJabatan)            sleep(driver)            driver.find_element(By.ID, 'inputKeperluan').send_keys(inputKeperluan)            print('.')            Log.info(' Input NIP ')            attach(data=driver.get_screenshot_as_png())    elif inputKategori == 'Kunjungan Onsite':        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))        driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()        driver.find_element(By.ID, "kunjungan").click()        driver.find_element(By.ID, 'pickKunjungan0').click()    buttonSubmit(driver)@mark.fixture_test()def test_exit():    quit(driver)# INPUT MANUAL KUNJUNGAN ONLINE BELUM ( TIDAK ADA DATA )# INPUT MANUAL KUNJUNGAN ONSITE BELUM ( TIDAK ADA DATA )