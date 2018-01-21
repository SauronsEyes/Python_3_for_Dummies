import urllib.request
import urllib.parse

#url='http://www.pythonprogramming.net'
#params={'s':'basic',
#        'submit':'Search'}
#
#data=urllib.parse.urlencode(params)
#data=data.encode('utf-8')
#req=urllib.request.Request(url,data)
#resp=urllib.request.urlop
url=input('URL:')

try:
    headers = {"User-Agent":"Mozilla/4.0"}
   
    req=urllib.request.Request(url,headers=headers)
    resp=urllib.request.urlopen(req)
    respData=resp.read()
    
    save=open('new.html','w')
    save.write(str(respData))
    save.close()
except Exception as e:
    print(str(e))
    