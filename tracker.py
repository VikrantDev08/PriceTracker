import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}
url = "https://www.flipkart.com/apple-iphone-17-lavender-256-gb/p/itm5c650337c09ee?pid=MOBHQV9YDG7CGRAM&param=2765&BU=Mobile&pageUID=1792568731294"
request1=requests.get(url,headers=headers)
soup=BeautifulSoup(request1.text,'html.parser')
price = soup.find("div",class_="_1psv1zeb9").text

cleanprice=price.replace("₹","").replace(",","").strip()  #make a string of numbers

finalprice=float(cleanprice)  #convert price ro a number
print(price)
print(finalprice)

datetime=datetime.now()  # holds vale in a datetime object not string

finaldatetime=datetime.strftime("%d-%m-%y , %H:%M:%S")  # converts datetime object into a formatted string
print(finaldatetime[0])