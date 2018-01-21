import urllib.request
import urllib.parse
import re

search_query=input("Enter Keyword to search for: ")
url='https://en.wikipedia.org/wiki/'+search_query
resp=urllib.request.urlopen(url)
respData=resp.read()
try:
    parsed_data=re.findall(r'<p>(.*?)</p>',str(respData))
    save_data=open('parsed.html','w')
    for eachP in parsed_data:
        save_data.write(eachP)
    save_data.close()
    print('SUCCESS')
except Exception as e:
    print(str(e))


