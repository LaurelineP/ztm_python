## 15 - TESTING AUTOMATION
It is about automatically test End To End in order to test how the application reacts.
A common tool is to use Selenium
Selenium with Python: https://selenium-python.readthedocs.io/

It gives the ability to emulate the browser to test the app

### INSTALLATION
- Optional - local env:
	- have an env to install selenium: `python -m venv my-env`
	- activate the interpreter: in your project location:  
	`source my-env/bin/activate`
- Install Selenium : `pip install selemium`
- Install a "driver" ( refers to which browser to use ) - take the latest
	- Using Chrome: ( in doc ) : download the zip file for your system
	- Folder composition:
		- `chromedriver.exec`: an executable that would run binary code

### SETTING CHROME DRIVER
The course uses a way that did not work
What worked:
```python
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
chrome = webdriver.Chrome(options=options)
```

An alternative proposed by the course
```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./chromedriver')

chrome_browser = webdriver.Chrome(service=service)
```


OTHER ALTERNATIVE TO FOLLOW THE COURSE PROPOSED
```python
# old way selenium v < 4
button = chrome_browser.find_element_by_class_name('btn-default')
# becoming the following ( new way : selenium v > 4)
button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')


### total code
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# This solves the issue with the Popup for those that encounter it:
chrome_browser.implicitly_wait(2)
popup =chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
popup.click()



user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I AM EXTRA COOOOL' in output_message.text
```


### SELENIUM BASICS
Resources: 
- Selenium with Python: https://selenium-python.readthedocs.io/
- Selenium test ground: https://demo.seleniumeasy.com/
- Selenium Cheatsheet: http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/