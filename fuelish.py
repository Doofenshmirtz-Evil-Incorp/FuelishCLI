import requests
import csv
from bs4 import BeautifulSoup

###################################

def tablemaker(data):     #OPTIMIZED VARIANT
    l=len(data[0])
    lf=[]
    for p in range(l):
        li=[]
        mx=0
        for i in data:
            aa=len(str(i[p]))
            li.append(aa)
            mx=max(li)
        else:
            lf.append(mx)
    print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="")
    for p in data:
        for i in range(l):
            print("|"," ",p[i]," "," "*(lf[i]-len(str(p[i]))),"|",end="",sep="")
        if data[0]==p:
            print()
            print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="",end="")            
        print()
    print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="")# table making end

#####################################


URL = "https://www.ndtv.com/fuel-prices/petrol-price-in-all-state"
page = requests.get(URL)

#print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
results=soup.find(id="myID")

#create lists for each parameters
state = []
price = []
change = []
x = 1

#####################################

#extracting all elements under td tag
for Data in results.find_all("td"):
    match (x%3):
        case 1:
            state.append(Data.text)
        case 2:
            price.append(Data.text)
        case 0:
            change.append(Data.text)
    x+=1
out=[]
out.append(["State","Price","Change"])
for (i,j,k) in zip(state,price,change):
    l=[i,j,k]
    out.append(l)
tablemaker(out)

#########################################

f=open("Data.csv","w")

cswrite=csv.writer(f)
cswrite.writerows(out)
f.close()

#########################################