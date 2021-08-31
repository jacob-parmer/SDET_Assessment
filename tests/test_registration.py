from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

"""
1.) Loads landing page
2.) Clicks on "Registration" box and switches windows
3.) Types username, password, and description into login form boxes
4.) Hits login button
5.) Checks that text 'logged in!!' is present in current window.
"""
def test_registration_valid(driver):

    # 1.)
    driver.get("http://www.way2automation.com/protractor-angularjs-practice-website.html")

    # 2.)
    driver.find_element_by_link_text("Registration").click()
    driver.switch_to_window(driver.window_handles[1])
    driver.implicitly_wait(10)

    # 3.)
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    description = driver.find_element_by_id("formly_1_input_username_0")

    username.send_keys("angular")
    password.send_keys("password")
    description.send_keys("Valid")

    # 4.)
    driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

    # 5.)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'logged in!!')]")))
    except TimeoutException:
        assert False, "Login was not successful."

    assert True


"""
1.) Loads landing page
2.) Clicks on "Registration" box and switches windows
3.) Types username, password, and description into login form boxes - with INCORRECT password
4.) Hits login button
5.) Checks that text 'Username or password is incorrect' is present in current window.
"""
def test_registration_invalid(driver):

    # 1.)
    driver.get("http://www.way2automation.com/protractor-angularjs-practice-website.html")
    
    # 2.)
    driver.find_element_by_link_text("Registration").click()
    driver.switch_to_window(driver.window_handles[1])
    driver.implicitly_wait(10)

    # 3.)
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_id("password")
    description = driver.find_element_by_id("formly_1_input_username_0")

    username.send_keys("angular")
    password.send_keys("password1")
    description.send_keys("Invalid")

    # 4.)
    driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

    # 5.)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Username or password is incorrect')]")))
    except TimeoutException:
        assert False, "Login was not successful."

    assert True