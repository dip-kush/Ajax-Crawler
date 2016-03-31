import logging
import logging.config


'''
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': '%(asctime)s %(name)-12s %(lineno)s %(levelname)-8s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
})

'''

def LoggerHandler(name):
    '''
    Prints the logs of Crawling
    '''
    logger = logging.getLogger(name)
    #handler = logging.FileHandler('crawling.log',mode='w')
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(lineno)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger



def printRequest():
    path = "/home/deepak/programs/proxy/requests.txt"
    data = ""
    try:    
        f = open(path, "r")
        data = f.readlines()
        data = ''.join(data)
    except Exception as e:
        print e
    if data.find("HEADEREND")!=-1:
        data = data.strip("HEADEREND")
        headers = data.split("HEADEREND")
        header = headers[0].strip()	
        return header
        #print headers[0].split('\n')
    else:
        data = data.strip("RESPONSEHEADERS")
        headers = data.split("RESPONSEHEADERS")
        header = headers[0].strip()
        return header    
        #print headers[0].split('\n')

def clearContent():
    path = "/home/deepak/programs/proxy/requests.txt"
    f = open(path, "w")
