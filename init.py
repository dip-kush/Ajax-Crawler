from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:81/login/login.php")
assert "Login Form" in driver.title
email  = driver.find_element_by_name("e-mail")

email.send_keys("vinaysharma@gmail")

password  = driver.find_element_by_name("Password")

password.send_keys("vinaykool")

password.send_keys(Keys.RETURN)
print driver.page_source
#assert "Welcome, " in driver.page_source
driver.close()
