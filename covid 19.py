import csv, json
import pandas as pd
import numpy  as np
import urllib.request as url
import matplotlib.pyplot as pt
import requests

response=url.urlopen("https://api.covid19india.org/raw_data.json")
temp_data=json.load(response)
file=pd.DataFrame(temp_data["raw_data"])
print('covid 19 data is Ready to use :')
print()
file.fillna("undefined", inplace = True) 

#line graph
a=0
b=0
c=0
d=0
e=0
for i in file['nationality']:
    if(i=='India'):
        a=a+1
    elif(i=='Italy'):
        b=b+1
    elif(i=='United Kingdom'):
        c=c+1
    elif(i=='Indonesia'):
        d=d+1
    else:
        e=e+1
print("India :",a)
print("Italy :",b)
print("United Kingdom :",c)
print("Indonesia :",d)
print("others :",e)

nationality=["India","Italy","UK","Indonesia","others"]
value=[a,b,c,d,e]
pt.title("COVID_19 DATA")
pt.xlabel("Natinality")
pt.ylabel("Total number of people")
pt.plot(nationality,value,color='red')
pt.show()

#bar graph
aa=0
bb=0
cc=0
dd=0
ee=0
for i in file['agebracket']:
    if(i>='1' and i<='20'):
        aa=aa+1
    elif(i>='21' and i<='40'):
        bb=bb+1
    elif(i>='41' and i<='60'):
        cc=cc+1
    elif(i>='61' and i<='80'):
        dd=dd+1
    elif(i>='81'):
        ee=ee+1       
    
print("Between 1 to 20 :",aa)
print("Between 21 to 40 :",bb)
print("Between 41 to 60:",cc)
print("Between 61 to 80 :",dd)
print("above80 :",ee)
pt.title("COVID_19 DATA")
ob=("1 to 20","21 to 40","41 to 60","61 to 80","above80")
z=np.arange(len(ob))
val=[aa,bb,cc,dd,ee]
pt.xlabel("Age bracket")
pt.ylabel("Total number of people")
toplabel=pt.bar(z,val,color=['green', 'orange', 'black', 'red', 'blue'])
pt.xticks(z,ob)
for i in toplabel:
    height = i.get_height()
    pt.text(i.get_x() + i.get_width()/2, 1*height,height,ha='center', va='bottom')
pt.show()

#pie chart
print('In this pie chart the gender is represented:')
f=0
m=0
for i in file['gender']:
    if(i=='M'):m=m+1
    elif(i=='F'):f=f+1
        
print("-----> male :",m)
print("-----> female :",f)

fig = pt.figure()
ax = fig.add_axes([0,0,1,1])
lab = ['Male', 'Female']
coviddata = [m,f]
pt.title("COVID_19 DATA")
pt.xlabel("Current Status")
pt.ylabel("Total number of people")
ax.pie(coviddata, labels = lab,autopct='%1.2f%%')
pt.show()
