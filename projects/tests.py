from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

interval = 2
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("localhost:8000/projects")
time.sleep(interval)
project = driver.find_element_by_css_selector("li a.project-1")
project.click()
time.sleep(interval)
feature = driver.find_element_by_link_text("Social Authentication")
feature.click()
time.sleep(interval)
testcase = driver.find_element_by_css_selector("li a.testcase-1")
testcase.click()
time.sleep(interval)
driver.quit()

