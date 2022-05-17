import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


html = requests.get("https://www.soyoustart.com/ie/essential-servers/")
soup = BeautifulSoup(html.text, 'html.parser')

# get list all of contry
contryy = []
for i in soup.find_all('div' , class_="custom-select"):

    contryy.append(i.text.replace("\n","").replace('\s','').replace('   ','').replace('                ', ''))
    
    
# get setupfee
link = soup.find_all('a')
text = []
name = []
a = "offers"
for lnk in link:
    b = lnk.get('href')
    if a in b :
        text.append("https://www.soyoustart.com" +b)
setup = []    
for i in text:
    html = requests.get(i)
    soup = BeautifulSoup(html.text, 'html.parser')
    names = soup.find_all('h1' , class_='fspx40 marginTop60')
    Ram = soup.find_all('span',class_='spanWithPrice red')
    cpu = soup.find_all(class_="flex-wrapper:nth-child(1) .clear:nth-child(1) span")



    for i in names:
        name.append(i.text)
    for i in Ram:
        
        setup.append(i.text)



driver_path = r"C:\\Users\\stokala\\Desktop\\chromedriver.exe\\chromedriver.exe"

# chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])



driver = webdriver.Chrome(driver_path, chrome_options=options)

# get url
url = "https://www.soyoustart.com/ie/essential-servers/"
driver.get(url)

# create lists for write
pricee = []
Disk = []
ram = []
Country = []
Order = []
Cpu = []
Rial = []
all = []
Setup = []
time.sleep(10) 


#get html info 
lists = driver.find_elements_by_class_name('text--large')
prices = driver.find_elements_by_class_name('red')
order = driver.find_elements_by_class_name("text--normal")
disk = driver.find_elements_by_class_name('col-md-1+ .col-md-2')
contry = driver.find_elements_by_xpath('//*[(@id = "servers-list")]//*[contains(concat( " ", @class, " " ), concat( " ", "select-selected", " " ))]')
Ram = driver.find_elements_by_class_name('col-md-1+ .col-md-1')
cpu = driver.find_elements_by_class_name('lm-auto+ .col-md-1')


#read euro 
with open("C:\\Users\\stokala\\Desktop\\a\\eurooooooooooo.txt" , "r") as f :
    euro = f.read()
a = 0

#write information in list
for i in prices:
    
    if a == 4:
        pricee.append(i.text)
    else:
        a+=1
        

for i in order:
    Order.append(i.text)        
    
    
for i in contry:
    Country.append(i.text)

   
d = 0
for i in Ram:
    if d == 1:
        ram.append(i.text)
    else :
        d+=1
e = 0
for i in cpu:
    if e == 1:
        Cpu.append(i.text.replace("\n"," "))
    else:
        e+=1
f = 0
for i in disk:
    if f == 1:
        Disk.append(i.text)
    else:
        f+=1
time.sleep(5)

for i in pricee:
    if len(i) == 5 or len(i) == 6:
        out = float(i) * float(euro)
        Rial.append(int(out))

for i in setup:
    test = setup[2::3]
    
for i in test:
    out = float(i) * float(euro)
    Setup.append(int(out))

time.sleep(5)
driver.quit()
d = {}


# read info and write in json file 
for (pr,na,orr,co,ra,cp,di,se,ali) in (zip(Rial,name,Order,Country,ram,Cpu,Disk,Setup,contryy)):
    d["Server"]=na
    d["CPU"]=cp
    d["RAM"]=ra
    d["Disks"]=di
    d["Datacentres"]=co
    d["Price/month"]=pr
    d["status"]=orr
    d["setupfee"]=se
    d["all of the contry"]=ali
    
    all.append({**d})

with open('france.json', 'w') as fp:
    json.dump(all, fp)
