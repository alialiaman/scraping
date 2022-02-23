from bs4 import BeautifulSoup
import requests
from requests import get
import json
import os
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")



names = []
persent =[]
persian = []
lst =[]
picture = []
path =[]
id_costomer = []

# get url
url = "https://emalls.ir/%D9%84%DB%8C%D8%B3%D8%AA-%D9%82%DB%8C%D9%85%D8%AA"
page = requests.get(url)
suap = BeautifulSoup(page.content, 'html.parser')


namess = suap.find_all(class_="maintitle")  #name of all phones
names_of_persian = suap.find_all(class_="subtitle")
costomer = suap.find_all(class_="btn btn-red w100p")
ghetmat = suap.find_all(class_="col-md-2 col-sm-12 col-12 item-price")

for i in ghetmat:
    persent.append(i.text)

for i in namess:
    names.append(i.text)
    
for i in names_of_persian:
    persian.append(i.text)
 
for link in costomer:
    links_href = link.get('href')
    lst.append("https://emalls.ir/" + links_href)
    
for i in lst:
    id_costomer.append(i.split('~')[-1])
    
main_list = suap.find("div", id="mainlist")
x = 0
for img in main_list.find_all("img"):
    name = str(img.get("alt"))
    if(x < 3):
        link = img.get("src")
    else:
        link = img.get("data-lazysrc")
    ## create directory for save image
    if os.path.isdir('C:\\Users\\stokala\\Desktop\\a\\images\\mobile') == True:
        pass
    else:
        os.makedirs('C:\\Users\\stokala\\Desktop\\a\\images\\mobile')
## save image
    suffix = link.split(".")[-1]
    file_path = name + "." + suffix
    file_path = file_path.replace("/", "-")
    os.chdir('C:\\Users\\stokala\\Desktop\\a\\images\\mobile')
    file = open(file_path, "wb")
    image = get(link)
    file.write(image.content)
    names_of_image =file_path
    pathh = os.getcwd()
    path.append(pathh)
    file.close()
    x += 1

    picture.append(link)

d ={}
ll =[]
for (i,a,j,cos,pat,pic,pr) in (zip(names,persian,lst,id_costomer,path,picture,persent)):
    d["Current Time is"] = current_time
    d["name"]=i
    d["Name"]=a
    d["id_costomer"]=cos
    d["persent"] = pr
    d["link_image"]=pic
    d["path"] = pat
    d ["link_composer"] = j
   
    ll.append({**d})
os.chdir('C:\\Users\\stokala\\Desktop\\a')
with open('mobile.json', 'w') as fp:
    json.dump(ll, fp, indent=2)
