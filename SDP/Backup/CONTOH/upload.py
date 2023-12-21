from selenium import webdriver

driver = webdriver.Chrome('/Users/will/Documents/chromedriver')
driver.get("https://demoqa.com/upload-download")

driver.find_element_by_id("uploadFile").send_keys("C:/Users/ASUS/Desktop/SDP/Backup/CONTOH/CONTOH.jpg")