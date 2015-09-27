from BeautifulSoup import BeautifulSoup
file = open("submit_form.html").read()
bs = BeautifulSoup(file)
l = bs.findAll("tr")

dictFields = {}

for i in range(1, len(l)):
    target = l[i].findAll("td")[1].text
    value = l[i].findAll("td")[2].text
    if value=="":
        continue
    else:
        print target, value
        dictFields[target] = value
        
        
        