import sys
import subprocess
import ctypes


import requests
from bs4 import BeautifulSoup
import lxml


User = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

site = "https://quotes.toscrape.com/page/" 

l1,l2 = [],[]
d = {}

for i in range(1,int(1E4)):
        print(i, site+str(i)+"/")
        
        page=BeautifulSoup((requests.get((site+str(i)+"/"), headers=User)).content, "lxml")
        print((requests.get(site+str(i)+"/", headers=User)).status_code)

        if (requests.get(site+str(i)+"/", headers=User)).status_code == 200 and str(page.find_all("div", "col-md-8")).find("No quotes found!")<0:
            
            for el in page.find_all('span',"text"):
                el=str(el)
                l1.append((el[el.rfind('">')+2:el.find("</")])[:])    

            for ath in page.find_all('small',"author"):
                ath=str(ath)
                l2.append((ath[ath.rfind('">')+2:ath.find("</")])[:])    

            for i in range(len(l1)):  
                d[l2[i]]=l1[i]
        else:
             break

for k in d:
    print(k,"\n",d[k])
