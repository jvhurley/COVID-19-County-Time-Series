#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

x = datetime.datetime.now()
url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
urld='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

couna='Yolo'   ##### name of County of interest

df = pd.read_csv(url, error_bad_lines=False)
dfa=np.array(df)
dfla=np.array(list(df.columns.values))

dfd=pd.read_csv(urld,error_bad_lines=False)
dfda=np.array(dfd)
dfdla=np.array(list(df.columns.values))

couco=np.where(dfla=='Admin2')[0][0]
print(couco)
yoro=np.where(dfa[:,couco]==couna)[0][0]
print(yoro)
print(dfa[yoro,:])
print(dfla)
fidat=np.where(dfla=='1/22/20')[0][0]
endat=np.shape(dfa[1])[0]
print(fidat)
print(endat)
#print(np.where(dfda[:,couco]=='Yolo')[0][0])
print(dfda[yoro,:])


plt.subplots(figsize=(10,8))
plt.plot(np.arange(fidat-fidat,endat-fidat),dfa[yoro,fidat:endat],'-md',markersize=3,label='confirmed')
plt.plot(np.arange(fidat-fidat,endat-fidat),dfda[yoro,fidat+1:endat+1],'-rd',markersize=3,label='deaths')
plt.legend()
#plt.xticks(np.arange(fidat-fidat,endat-fidat),dfla[fidat:endat],rotation=90)
plt.xticks(np.arange(fidat-fidat,endat-fidat,5),dfla[np.arange(fidat,endat,5)],rotation=90)
plt.title('COVID 19 in '+couna+' County, '+x.strftime("%x"))
plt.grid()





