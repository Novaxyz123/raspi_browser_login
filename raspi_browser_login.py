#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://example.com")
driver.maximize_window()

username = (By.XPATH, "//input[@id='username']")
password = (By.XPATH, "//input[@id='password']")
submit = (By.XPATH, "//*[@type='submit']")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable(username)).send_keys("admin")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(password)).send_keys("password")
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(submit)).click()

driver.maximize_window()