from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def test_registration_valid(driver):
    driver.get("http://www.way2automation.com/protractor-angularjs-practice-website.html")
    driver.find_element_by_link_text("Registration").click()
    
    driver.switch_to_window(driver.window_handles[1])

    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element_by_id("password")
    description = driver.find_element_by_id("formly_1_input_username_0")

    username.send_keys("angular")
    password.send_keys("password")
    description.send_keys("Valid")

    driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'logged in!!')]")))
    except TimeoutException:
        assert False, "Login was not successful."

    assert True

def test_registration_invalid(driver):
    driver.get("http://www.way2automation.com/protractor-angularjs-practice-website.html")
    driver.find_element_by_link_text("Registration").click()
    
    driver.switch_to_window(driver.window_handles[1])

    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password = driver.find_element_by_id("password")
    description = driver.find_element_by_id("formly_1_input_username_0")

    username.send_keys("angular")
    password.send_keys("password1")
    description.send_keys("Invalid")

    driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Username or password is incorrect')]")))
    except TimeoutException:
        assert False, "Login was not successful."

    assert True