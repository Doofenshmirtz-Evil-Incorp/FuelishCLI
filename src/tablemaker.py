
#credits to @Asvin1 for this pretty tablemaker function
#link to project: https://github.com/asvin1/cli-table

###############################

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
    
###############################