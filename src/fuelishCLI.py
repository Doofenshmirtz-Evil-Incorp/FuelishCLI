import csv
import re
from tablemaker import tablemaker 
import datetime
import os
import fuelish

######################################

#check if the data file exists 

if os.path.exists("Data.csv"):
    pass
else:
    try:
        fuelish.main()
    except:
        print("kindly connect to the internet for first time run")
        exit()

######################################

#download data only when updated in realtime

now=datetime.datetime.now()
updtime=now.replace(hour=6,minute=5,second=0)
last_mod=os.path.getmtime("Data.csv")
last_mod=datetime.datetime.fromtimestamp(last_mod)
if(last_mod<updtime):
    print("Updated")
    try:
        fuelish.main()
    except:
        print("you are offline, falling back to last known data")

######################################

#abbreviations for the available locations

abv=["an","ap","ar","as","br","ch","ct","dn","dd","dl","ga","gj","hr","hp","jk","jh","ka","kl","mp","mh","mn","ml","mz","nl","od","py","pb","rj","sk","tn","ts","tr","up","uk","wb"]
dic={"State":[],"Price(P)":[],"Change(P)":[],"Price(D)":[],"Change(D)":[],"abb":[]}
with open("Data.csv", "r",encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row,i in zip(csv_reader,abv):
        dic["State"].append(row["State"].lower())
        dic["Price(P)"].append(row["Price(P)"])
        dic["Change(P)"].append(row["Change(P)"])
        dic["Price(D)"].append(row["Price(D)"])
        dic["Change(D)"].append(row["Change(D)"])
        dic["abb"].append(i)

######################################

print("Welcome to Fuelish-CLI")
print("Don't be foolish and know your prices")
while True:
    try:
        ind=-1
        state_input = input("Enter your State: ").strip()
        #Check if abbreviation matches
        if(len(state_input)==2):
            try:
                ind=abv.index(state_input.lower())
            except:
                ind=-1
        #Generate regex pattern
        tempin=""
        for i in state_input:
            tempin+=i+"+.*"
        #Check if input matches regex pattern
        lt=[x if(re.match(tempin,x)) else "" for x in dic["State"]]
        fuel = input("Petrol or Diesel?(P/D)").lower()
        l=[]
        if(ind!=-1):
            i=ind
            if fuel == "p":
                l.append([dic["State"][i].capitalize(),dic["Price(P)"][i],dic["Change(P)"][i]])
            elif fuel == "d":
                l.append([dic["State"][i].capitalize(),dic["Price(D)"][i],dic["Change(D)"][i]])
        else:
            for j in lt:
                if(j!=""):
                    i=dic["State"].index(j)
                    if fuel == "p":
                        l.append([dic["State"][i].capitalize(),dic["Price(P)"][i],dic["Change(P)"][i]])
                    elif fuel == "d":
                        l.append([dic["State"][i].capitalize(),dic["Price(D)"][i],dic["Change(D)"][i]])
        if(len(l)==0):
            print("*Skill issue. it's a you problem!*")
        else:
            l.insert(0,["State","Price","Change"])
            tablemaker(l)
    except KeyboardInterrupt:
        break
    except:
        print("*Kuch to hua hai*")

######################################