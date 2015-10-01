from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Crawler import initState



def main():
    ''' 
    crawls the website http://127.0.0.1:81/login/login.php
    with login credentials 
    email = vinaysharma@gmail 
    password = vinaykool    

    '''
    
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/login/login.php")
    assert "Login Form" in driver.title
    
    email  = driver.find_element_by_name("e-mail")
    email.send_keys("vinaysharma@gmail")
    password  = driver.find_element_by_name("Password")
    password.send_keys("vinaykool")
    password.send_keys(Keys.RETURN)

    #print driver.page_source
    print driver.current_url, driver.title
    
    #move the controller to Initiate Crawler Activity
    initState(driver.page_source, driver.current_url, driver.title, driver)

    #assert "Welcome, " in driver.page_source
    driver.close()


if __name__ == '__main__':
    main()
