##################################

import requests
import csv
from bs4 import BeautifulSoup

###################################

def main():
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
    city =[]
    price_p = []
    change_p = []
    price_d = []
    change_d = []
    cprice_p = []
    cchange_p = []
    cprice_d = []
    cchange_d = []

    x = 1

#####################################

#extracting all elements under td tag

    for SData_P in results1.find_all("td"):
        match (x%3):
            case 1:
                state.append(SData_P.text)
            case 2:
                price_p.append(SData_P.text)
            case 0:
                if(SData_P.find(class_="chngBx up")):
                    change_p.append("- "+SData_P.text)
                elif(SData_P.find(class_="chngBx down")):
                    change_p.append("+ "+SData_P.text)
                else:
                    change_p.append("  "+SData_P.text)
        x+=1
    x=1
    for SData_D in results2.find_all("td"):
        match (x%3):
            case 2:
                price_d.append(SData_D.text)
            case 0:
                if(SData_D.find(class_="chngBx up")):
                    change_d.append("- "+SData_D.text)
                elif(SData_D.find(class_="chngBx down")):
                    change_d.append("+ "+SData_D.text)
                else:
                    change_d.append("  "+SData_D.text)
        x+=1
    x=1
    for s in state:
        URL3 = "https://www.ndtv.com/fuel-prices/petrol-price-in-"+s.replace(" ","-")+"-state"
        page3 = requests.get(URL3)
        URL4 = "https://www.ndtv.com/fuel-prices/diesel-price-in-"+s.replace(" ","-")+"-state"
        page4 = requests.get(URL4)
        soup3 = BeautifulSoup(page3.content, "html.parser")
        results3=soup3.find(id="myID")
        soup4 = BeautifulSoup(page4.content, "html.parser")
        results4=soup4.find(id="myID") 
        for CData_P in results3.find_all("td"):
            match (x%3):
                case 1:
                    city.append(CData_P.text)
                case 2:
                    cprice_p.append(CData_P.text)
                case 0:
                    if(CData_P.find(class_="chngBx up")):
                        cchange_p.append("- "+CData_P.text)
                    elif(CData_P.find(class_="chngBx down")):
                        cchange_p.append("+ "+CData_P.text)
                    else:
                        cchange_p.append("  "+CData_P.text)
            x+=1
        x=1
        for CData_D in results4.find_all("td"):
            match (x%3):
                case 2:
                    cprice_d.append(CData_D.text)
                case 0:
                    if(CData_D.find(class_="chngBx up")):
                        cchange_d.append("- "+CData_D.text)
                    elif(CData_D.find(class_="chngBx down")):
                        cchange_d.append("+ "+CData_D.text)
                    else:
                        cchange_d.append("  "+CData_D.text)
            x+=1
        out2=[]
        out2.append(["City","Price(P)","Change(P)","Price(D)","Change(D)"])
        for (i,j,k,l,m) in zip(city,cprice_p,cchange_p,cprice_d,cchange_d):
            list2=[i,j,k,l,m]
            out2.append(list2)
        f=open("./assets/"+s+".csv","w",encoding="utf-8")
        cswrite=csv.writer(f)
        cswrite.writerows(out2)
        f.close()
        
#####################################

    out1=[]
    out1.append(["State","Price(P)","Change(P)","Price(D)","Change(D)"])
    for (i,j,k,l,m) in zip(state,price_p,change_p,price_d,change_d):
        list1=[i,j,k,l,m]
        out1.append(list1)
    #tablemaker(out)

    # out2=[]
    # out2.append(["City","Price(P)","Change(P)","Price(D)","Change(D)"])
    # for (i,j,k,l,m) in zip(city,cprice_p,cchange_p,cprice_d,cchange_d):
    #     list2=[i,j,k,l,m]
    #     out2.append(list2)
    #tablemaker(out)

######################################

    f=open("State.csv","w",encoding="utf-8")

    cswrite=csv.writer(f)
    cswrite.writerows(out1)
    f.close()

    # f=open("City.csv","w",encoding="utf-8")

    # cswrite=csv.writer(f)
    # cswrite.writerows(out2)
    # f.close()

#######################################
if __name__ == '__main__':
    main()
    print("Updated Data!")
