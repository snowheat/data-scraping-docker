from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# https://stackoverflow.com/questions/53073411/selenium-webdriverexceptionchrome-failed-to-start-crashed-as-google-chrome-is

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("/bin/chromedriver", options=options)
driver.get("https://mecha.id")
print(driver.title)
driver.quit()
