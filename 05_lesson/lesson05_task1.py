from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.google.com/")

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element("xpath", "//button[contains(@class, 'btn-primary')]")
blue_button.click()

sleep (10)