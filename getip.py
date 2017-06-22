# 获取github和其子域名的IP地址
import requests
from bs4 import BeautifulSoup

for i in open("url.txt"):
    url = "http://ip.chinaz.com/" + i.strip()
    resp = requests.get(url)
    soup=BeautifulSoup(resp.text)
    x=soup.find(class_="IcpMain02")
    x=x.find_all("span",class_="Whwtdhalf")
    print(x[5].string.strip(),i.strip())