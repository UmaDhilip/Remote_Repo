import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from datetime import datetime

np.random.seed(50)
df = pd.DataFrame(random.randn(6,4),['R1','R2','R3','R4','R5','R6'],['C1','C2','C3','C4'])
#print(df)
d = {'A': [1,2,np.nan,np.nan,np.nan], 'B': [9, np.nan, np.nan,10,np.nan], 'C': [1,4,9,12,22]}
#df = pd.DataFrame(d)
#print(df,'\n')

#MATPLOT LIB
#------------
#years = [1981, 1991, 2001, 2011, 2016]
#Average_populations = [716493000, 891910000, 1071374000, 1197658000, 1273986000]

#plt.plot(years, Average_populations)
#plt.title("Census of India: sample registration system")
#plt.xlabel("Year")
#plt.ylabel("Average_populations")
#plt.show()
#dates = pd.date_range("20220220",periods=6)
#print(dates)

in_data = {'eid':[101,102,103,104],'ename':['Uma','Dhil','Rithu','Prana'],'emarks':[90,89,95,94]}
df = pd.DataFrame(in_data)
#df = pd.read_json("C:\\Users\\mahii\\Project\\schoolinfo\\school_info.json")
#print(df['eid'])
#print(df[['eid']])
#print(len(df))
#print(df.columns)
#print(df.eid.head(2))
#print(df.eid.std())
#print(df.emarks.mean())
#print(df.emarks.median())
#print(df.emarks.mode())
#print(df.emarks.plot())
#print(df.emarks.hist())
#plt.show()
#df.plot(kind='scatter',x='eid',y='emarks')
#plt.show()

#df2 = df.sort_index(axis=1, ascending=False)
#df2 = df.sort_values(by='emarks')
#print(df2)


#list1 = df['student_fname'] # returns single dim array
#list2 = df['total marks']

#plt.scatter
#plt.plot
#plt.plot(list1,list2,'ro--')
#plt.xlabel('Students Name')
#plt.ylabel('Students Marks')
#plt.title("Students Academic Performance")
#plt.show()

lab = ['Python','C++','Java','Perl']
sz = [123,87,120,180]
clr = ['gold','yellow','blue','red']
expl = (0.2,0,0,0)

#plt.pie(sz,explode=expl,labels=lab,colors=clr,autopct='%1.1f%%',shadow=False)
#plt.axis('equal')
#plt.show()

# DROPNA AND FILLNA
#x = df.dropna()
#print(x)

#x1 = df.dropna(axis=1)
#print(x1)

#x2 = df.dropna(how="any")
#print(x2)

#x3 = df.dropna(how="all")
#print(x3)

#4 = df.dropna(thresh=2)
#print(x4)

#x = df.fillna(value= df.mean())
#print(x)

#Bulk operatios with apply()
df = pd.read_csv("C:\\Users\\mahii\\Project\\schoolinfo\\Test3.csv")
df.columns = ['ID','Bank_Name','City','States','Cert','Acq_Inst','Closing_Dt','Fund']

#fdate = df.Closing_Dt.values[0]
#print(datetime.strptime(fdate, "%B %d, %Y"))
#df.Closing_dt = df.Closing_Dt.apply(lambda dt: datetime.strptime(dt, "%B %d, %Y"))
#print(df.Closing_Dt.head())

#Check empty Values
df.isna().any()[lambda x : x]

print(df.isnull().values.any())


