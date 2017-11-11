#!/usr/bin/python
import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webbrowser.open('http://webmail.tcs.com')
username = browser.find_element_by_name('Username')
#password = selenium.find_element_by_text('Password')

username.send_keys("**********")
password = browser.find_element_by_name('Password')
password.send_keys("*********")

#selenium.find_element_by_id("Login").click()
password.submit()

