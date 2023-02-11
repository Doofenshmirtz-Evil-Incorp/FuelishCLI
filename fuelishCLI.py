import csv
from tablemaker import tablemaker

######################################

dic={"State":[],"Price(P)":[],"Change(P)":[],"Price(D)":[],"Change(D)":[]}
with open("Data.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        dic["State"].append(row["State"].lower())
        dic["Price(P)"].append(row["Price(P)"])
        dic["Change(P)"].append(row["Change(P)"])
        dic["Price(D)"].append(row["Price(D)"])
        dic["Change(D)"].append(row["Change(D)"])
#print(dic)

######################################

print("Welcome to Fuelish-CLI")
print("Don't be foolish and know your prices")
state = input("Enter your State: ").lower()
fuel = input("Petrol or Diesel?(P/D)").lower()
i=dic["State"].index(state)
l=[]
if fuel == "p":
    l.append(["State","Price","Change"])
    l.append([dic["State"][i].capitalize(),dic["Price(P)"][i],dic["Change(P)"][i]])
elif fuel == "d":
    l.append(["State","Price","Change"])
    l.append([dic["State"][i].capitalize(),dic["Price(D)"][i],dic["Change(D)"][i]])

######################################

tablemaker(l)