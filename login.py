from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time
import re
from unittest import TestCase


def login_unsuccessful(driver):

    username = driver.find_element(By.XPATH, '//*[@id="idToken1"]')
    username.send_keys('kholo')
    password= driver.find_element(By.XPATH, '//*[@id="idToken2"]')
    password.send_keys('1234')
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginButton_0"]').click()
    
    # check if message is visible
    time.sleep(5)
    text='User name/password combination is invalid.'
    if text in driver.page_source:
        print('------------login was unssucessful------------------')
    
def login_successful(driver):
   
    username = driver.find_element(By.XPATH, '//*[@id="idToken1"]')
    username.send_keys('oauth-kholofelomasela1-b473e')
    password= driver.find_element(By.XPATH, '//*[@id="idToken2"]')
    password.send_keys('FVF@fF5izwjXqq3')
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="loginButton_0"]').click()  
    time.sleep(5)

    # check if log in was successful
    time.sleep(10)
    text ='Go to the Get Started Guide'
    if text in driver.page_source:
        print('----------------login succussful-------------------------')
    else:
        print('------------login was unssucessful------------------')







if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get('https://accounts.saucelabs.com/am/XUI/#login/')
    time.sleep(5)
    login_unsuccessful(driver)
    time.sleep(5)
    login_successful(driver)
    
    

