# HOW TO INSTALL
-  pip install selenium
-  pip3 install openpyxl
-  pip install pandas
-  pip3 install xlrd
-  pip3 install pytest-html (must be installed on directory file.py )
-  chrome driver must be new version or same as chrome

# Report test 
- pytest -v  -s --html=.\namafolder\report.html -contained-html test_gg.py 
- python3 -m pytest -v -s --html=.\namefolder\report.html -contained-html name.py
- python3 -m pytest file.py

# Automationpython
Automation Web testing using python &amp; selenium Web driver

## Using Selenium Web Driver for testing application SDP
- read  Data exel for automation Input when create New data 

## Extrack chromedriver and save to antoher folder
exemple :
- s = Service('C:\chromedriver\chromedriver.exe')
- driver = webdriver.Chrome(service=s)
.

# document test 

https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
