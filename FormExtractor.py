from BeautifulSoup import BeautifulSoup
from logger import LoggerHandler
import sys


# print formFieldsValues

logger = LoggerHandler(__name__)


def getFormFieldValue(filePath, fileHandler=None):
    formFieldsValues = {}
    formFieldsValues['id'] = {}
    formFieldsValues['xpath'] = {}
    formFieldsValues['name'] = {}

    try:
        #logger.info("Reading the Form Values File %s"%file)
        if fileHandler:
            file = fileHandler
        else:
            file = open(filePath).read()
        bs = BeautifulSoup(file)
        l = bs.findAll("tr")
        for i in range(1, len(l)):
            type = l[i].findAll("td")[0].text
            target = l[i].findAll("td")[1].text
            value = l[i].findAll("td")[2].text
            if value == "" and type == "clickAndWait":
                pass
                # formSubmitIds.append(target)
            elif value != "":
                # print target, value
                target = str(target)
                index = str(target).find('=')
                type = target[0:index]
                fieldVal = target[index + 1:]
                if type == "id":
                    formFieldsValues['id'][fieldVal] = value
                elif type == "name":
                    formFieldsValues['name'][fieldVal] = value
                else:
                    formFieldsValues['xpath'][fieldVal] = value
    except IOError as e:
        logger.error("I/O Error({0}): {1} ".format(e.errno, e.strerror))
    except ValueError as e:
        logger.error("Value Error {}".format(e))
    except:
        logger.error(sys.exc_info())
    return formFieldsValues    

def fillFormValues(formFieldValues, driver):
    idFields = formFieldValues['id']
    nameFields = formFieldValues['name']
    xpathFields = formFieldValues['xpath']

    for fieldName, fieldValue in idFields.iteritems():
        try:
            element = driver.find_element_by_id(
                fieldName).send_keys(fieldValue)
        except:
            logger.info(sys.exc_info())

    for fieldName, fieldValue in nameFields.iteritems():
        try:
            element = driver.find_element_by_name(
                fieldName).send_keys(fieldValue)
        except:
            logger.info(sys.exc_info())

    for fieldName, fieldValue in xpathFields.iteritems():
        try:
            element = driver.find_element_by_xpath(
                fieldName).send_keys(fieldValue)
        except:
            logger.info(sys.exc_info())


def pressSubmitButtons(driver):
    elements = driver.find_elements_by_xpath("//input[@type='submit']")
    submitButtonNumbers = len(elements)
    for i in range(1, submitButtonNumbers + 1):
        element = driver.find_elements_by_xpath(
            "(//input[@type='submit'])[" + i + "]")
        element.click()
        driver.back()


def getSubmitButtonNumber(domString, driver):
    elements = driver.find_elements_by_xpath("//input[@type='submit']")
    return len(elements)

#getFormFieldValue("submit_form2.html")
