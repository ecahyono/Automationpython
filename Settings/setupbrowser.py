from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
def initoption():
    # Dapatkan nomor port pada Remote Debugging Port yang sudah dicatat sebelumnya
    remote_debugging_port = 9222

    # Tentukan path ke file Chrome Driver
    chromedriver_path = "C:/Users/user/Documents/110.0.5481.exe"

    # Atur opsi untuk Chrome
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", f"localhost:{remote_debugging_port}")
    chrome_options.add_argument("user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data/Default")

    # Buat objek Service
    chrome_service = Service(chromedriver_path)

    # Buat objek Remote WebDriver
    driver = Remote(service=chrome_service, options=chrome_options)

    # Lakukan navigasi ke situs web
    driver.get("https://www.google.com")
    return driver

def loadDataPath():
    if platform.system() == 'Darwin':
        file = open(environ.get("MACJSONDATA"), 'r')
    elif platform.system() == 'Windows':
        file = open(environ.get("WINJSONDATA"), 'r')

    data = json.load(file)
    return data