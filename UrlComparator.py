from urlparse import urlparse, urlunparse

def compare_url(url1, url2):
    parsed1 = urlparse(url1)
    parsed2 = urlparse(url2)
    
    if parsed1.hostname != parsed2.hostname:
        return False
    if parsed1.params != parsed2.params:
        return False
    if parsed1.path != parsed2.path:
        return False
    query1 = parsed1.query.split("&")
    query2 = parsed2.query.split("&")
    if len(query1) != len(query2):
        return False
    else:
        for i in range(len(query1)):
            queryparam1 = query1[i].split("=")
            queryparam2 = query2[i].split("=")
            if len(queryparam1) == 1 and len(queryparam2) == 1:
                continue
            elif query1[i].split("=")[0] != query2[i].split("=")[0]:
                return False
    return True

#url1 = "http://127.0.0.1:81/TomatoCart/products.php?5&sid=vkp4fd7up38jdato7ghjgkora1"       
#url2 = "http://127.0.0.1:81/TomatoCart/products.php?6&sid=vkp4fd7up38jdato7ghjgkora2"
#print compare_url(url1, url2)

