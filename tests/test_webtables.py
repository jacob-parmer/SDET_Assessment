"""
1.) Loads landing page
2.) Clicks on "WebTables" box and switches windows
3.) Deletes user with username 'admin' from table
4.) Checks that user with username 'admin' no longer exists in table
"""
def test_delete_user(driver):
    
    # 1.)
    driver.get("http://www.way2automation.com/protractor-angularjs-practice-website.html")
    
    # 2.)
    driver.find_elements_by_link_text("WebTables")[1].click()
    driver.switch_to_window(driver.window_handles[1])
    driver.implicitly_wait(10)

    # 3.)
    table = driver.find_elements_by_xpath("//*[@class= 'smart-table table table-striped']/tbody/tr")

    for row in table:
        if row.text.split(" ")[2] == "admin": # [2] is because the 'username', which we want to check for, is contained in the third column
            row.find_elements_by_tag_name("button")[1].click()
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()

    # 4.)
    table = driver.find_elements_by_xpath("//*[@class= 'smart-table table table-striped']/tbody/tr")
    
    for row in table:
        if row.text.split(" ")[2] == "admin":
            assert False, "Username 'admin' still found in table after deletion attempt"

    assert True