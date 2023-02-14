##################################

import requests
import csv
from bs4 import BeautifulSoup
from tablemaker import tablemaker

###################################

URL1 = "https://www.ndtv.com/fuel-prices/petrol-price-in-all-state"
page1 = requests.get(URL1)
URL2 = "https://www.ndtv.com/fuel-prices/diesel-price-in-all-state"
page2 = requests.get(URL2)

#print(page.text)
soup1 = BeautifulSoup(page1.content, "html.parser")
results1=soup1.find(id="myID")

soup2 = BeautifulSoup(page2.content, "html.parser")
results2=soup2.find(id="myID")

#create lists for each parameters
state = []
price_p = []
change_p = []
price_d = []
change_d = []

x = 1

#####################################

#extracting all elements under td tag

for Data_P in results1.find_all("td"):
    match (x%3):
        case 1:
            state.append(Data_P.text)
        case 2:
            price_p.append(Data_P.text)
        case 0:
            change_p.append(Data_P.text)
    x+=1
#####################################

x=1
for Data_D in results2.find_all("td"):
    match (x%3):
        case 2:
            price_d.append(Data_D.text)
        case 0:
            change_d.append(Data_D.text)
    x+=1

#####################################

out=[]
out.append(["State","Price(P)","Change(P)","Price(D)","Change(D)"])
for (i,j,k,l,m) in zip(state,price_p,change_p,price_d,change_d):
    list1=[i,j,k,l,m]
    out.append(list1)
#tablemaker(out)

######################################

f=open("Data.csv","w",encoding="utf-8")

cswrite=csv.writer(f)
cswrite.writerows(out)
f.close()

#########################################