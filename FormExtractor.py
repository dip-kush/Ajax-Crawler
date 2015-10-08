from BeautifulSoup import BeautifulSoup
import sys

formFieldsValues = {}
formFieldsValues['id'] = {}
formFieldsValues['xpath'] = {}
formFieldsValues['name'] = {}

print formFieldsValues

def getFormFieldValue(file):
    try:
        file = open(file).read()
        bs = BeautifulSoup(file)
        l = bs.findAll("tr")
        for i in range(1, len(l)):
            type = l[i].findAll("td")[0].text
            target = l[i].findAll("td")[1].text
            value = l[i].findAll("td")[2].text
            if value=="" and type=="clickAndWait":
                pass
                #formSubmitIds.append(target)
            elif value!="":
                #print target, value
                target = str(target)
                index = str(target).find('=')
                type = target[0:index]
                fieldVal = target[index+1:]
                if type=="id" :
                    formFieldsValues['id'][fieldVal] = value
                elif type=="name":
                    formFieldsValues['name'][fieldVal] = value
                else:
                    formFieldsValues['xpath'][fieldVal] = value
                    
        #return formFieldsValues
        #print formSubmitIds
        print formFieldsValues
    except IOError as e:
        print "I/O Error({0}): {1} ".format(e.errno, e.strerror)
    except ValueError as e:
        print "Value Error {}".format(e)
    except:
        print sys.exc_info()
    
        
def fillFormValues(dict, driver):
    idFields = formFieldsValues['id']
    nameFields = formFieldsValues['name']
    xpathFields = formFieldsValues['xpath']
    
    for fieldName, fieldValue in idFields.iteritems():
        try:
            element = driver.find_element_by_id(fieldName).send_keys(fieldValue)
        except:
            sys.exc_info()
            
    for fieldName, fieldValue in nameFields.iteritems():
        try:
            element = driver.find_element_by_name(fieldName).send_keys(fieldValue)
        except:
            sys.exc_info()
    
    for fieldName, fieldValue in xpathFields.iteritems():
        try:
            element = driver.find_element_by_xpath(fieldName).send_keys(fieldValue)
        except:
            sys.exc_info()
            
        
        
getFormFieldValue("submit_form2.html")

        
        
        
        
