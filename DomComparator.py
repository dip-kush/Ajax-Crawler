import xml.dom.minidom
from Queue import *


def htmlCompare(document1,document2,document3):
    '''
    Compare the two DomString
    document1 and document2 are DOM from Same RequestURL but with different TimeStamp 
    document1 and document2 are compared to each after removing noise elements
    
    '''
    dom1=xml.dom.minidom.parseString(document1)
    dom3=xml.dom.minidom.parseString(document3)
    root1=dom1.childNodes[0]
    root3=dom3.childNodes[0]
    flag=0
    if document2 is not None:
        dom2=xml.dom.minidom.parseString(document2)
        root2=dom2.childNodes[0]
        print root1
        #finding noise
        q1=Queue()
        q2=Queue()
        if(root1.nodeName==root2.nodeName):
            q1.put(root1)
            q2.put(root2)
        else:
            print('Err:Benign inputs should have same structure')
        while(q1.empty()==False and q2.empty()==False):
            b1=q1.get()
            b2=q2.get()
            l1=len(b1.childNodes)
            l2=len(b2.childNodes)
            if(l1!=l2):
                print('Err:Benign inputs should have same structure')
                break
            else:
                i=0
                flag=0
                while(i<l1):
                    x=b1.childNodes[i]

                    y=b2.childNodes[i]
                    if x.nodeName=='#text' and y.nodeName=='#text':
                            print str(x.nodeName +" " +  x.nodeValue)
                            if x.nodeValue!=y.nodeValue:
                                #mark parent of x as noise=y
                                print "noisy elements" + str(y.nodeValue)
                                b1.setAttribute('noise','y')
                            else:
                                #mark parent of x as noise=n
                                b1.setAttribute('noise','n')
                    elif x.nodeName!='#text' and y.nodeName!='#text':
                        print str(y.nodeName) + str(y.nodeValue)
                        if x.nodeName==y.nodeName:
                            q1.put(x)
                            q2.put(y)
                        else:
                            print('Err:Benign inputs should have same structure')
                            flag=1
                            break
                    else:
                        print('Err: Benign inputs should have same structure')
                        flag=1
                        break
                    i=i+1
                if  flag==1:
                    break
                   
    #finding State already Exist
    if flag==0:
        flag=0
        q1=Queue()
        q2=Queue()
        if(root1.nodeName==root3.nodeName):
            q1.put(root1)
            q2.put(root3)
        else:
            flag=1
        while(q1.empty()==False and q2.empty()==False):
            b1=q1.get()
            b2=q2.get()
            l1=len(b1.childNodes)
            l2=len(b2.childNodes)
            if(l1!=l2):
                flag=1
                break
            else:
                i=0
                while(i<l1):
                    x=b1.childNodes[i]
                    y=b2.childNodes[i]
                    if x.nodeName!='#text' and y.nodeName!='#text':
                        if x.nodeName!=y.nodeName:
                            flag=1
                            break
                        else:
                            q1.put(x)
                            q2.put(y)
                    elif x.nodeName=='#text' and y.nodeName=='#text':
                        if x.nodeValue!=y.nodeValue and (b1.getAttribute('noise')=='n' or document2 is None):
                            flag=1
                            break
                    else:
                        flag=1
                        break
                    i=i+1
                if flag==1:
                    break
        if flag==0:
            print ' State Exists with Given Dom String '
            return 1
        else:
            print 'No State Exists with Same Dom String'
            return 0    
    else:
        print 'No State Exists with Same Dom String'
        return 0

'''
file1 = open("page1", "r").read()
file3 = open("page1", "r").read()
benign1="<html><head><title>Title1</title></head><body><b>Hi</b><a href='a'></a><p>hello1</p></body></html>"
benign2 = None
benign2="<html><head><title>Title2</title></head><body><b>Hi</b><a href='a'></a><p>hello2</p></body></html>"
hostile1="<html><head><title>Title3</title></head><body><b>Hi</b><a href='a'></a><p>hello3</p></body></html>"
htmlCompare(file1,None,file3)
'''
