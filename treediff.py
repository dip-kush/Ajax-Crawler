from selenium import webdriver
from BeautifulSoup import BeautifulSoup
from htmltreediff import diff
from selenium.webdriver.support.ui import WebDriverWait

f = open("a.html", 'w')
g = open("b.html", "w")


driver = webdriver.Chrome()

driver.get("http://demo.crawljax.com/")

WebDriverWait(driver, 5000)
#driver.get("http://127.0.0.1:81/ajaxweb/")
before_source = driver.page_source

clickable = "openPage('crawlConditions.html')"
driver.find_element_by_xpath(
            '//a[@onclick="openPage(\'crawlConditions.html\')"]').click()

WebDriverWait(driver, 5000)

after_source = driver.page_source

f.write(before_source)
g.write(after_source)

f.close()
g.close()

dif = diff(before_source, after_source, pretty=True)
bdif = BeautifulSoup(dif)

print bdif.findAll("ins")
print bdif.findAll("del")


