#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

x = datetime.datetime.now()
url='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
urld='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

#couna='New York'   ##### name of County of interest
#stana='New York'   ##### 
couna='Yolo'   ##### name of County of interest
stana='California'   ##### 
#couna='Monmouth'  ##### name of County of interest
#stana='New Jersey'   ##### 
#couna='Ventura'  ##### name of County of interest
#stana='California'   ##### 
#couna='Sacramento'  ##### name of County of interest
#stana='California'   ##### 

df = pd.read_csv(url, error_bad_lines=False)
dfa=np.array(df)
dfla=np.array(list(df.columns.values))

dfd=pd.read_csv(urld,error_bad_lines=False)
dfda=np.array(dfd)
dfdla=np.array(list(df.columns.values))

couco=np.where(dfla=='Admin2')[0][0]
print(couco)
yoro1=np.where(dfa[:,couco]==couna)[0]
staro1=np.where(dfa[:,couco+1]==stana)[0]
yoro=np.intersect1d(yoro1,staro1)[0]
print(yoro1,staro1,yoro)
#if dfa[yoro,couco+1]==stana:
#    yoro=yoro1
print(yoro)
print(dfa[yoro,:])
print(dfla)
fidat=np.where(dfla=='1/22/20')[0][0]
endat=np.shape(dfa[1])[0]
print(fidat)
print(endat)
#print(np.where(dfda[:,couco]=='Yolo')[0][0])
print(dfda[yoro,:])

#wlcos_cola=np.array(list(lofi_wlcos_df.columns.values))
#casd_a_scrix=np.where(casd_a[:,10]=="Screen")
#casd_a_scrixa=(np.array(casd_a_scrix))[0,:]


fig,(ax1,ax2)=plt.subplots(2,1,figsize=(12,8))
ax1.plot(np.arange(fidat-fidat,endat-fidat),dfa[yoro,fidat:endat],'-o',color='darkgoldenrod',markerfacecolor='none',markeredgecolor='indigo',linewidth=3,markersize=6,label='confirmed')
ax1.plot(np.arange(fidat-fidat,endat-fidat),dfda[yoro,fidat+1:endat+1],'--v',color='darkgoldenrod',markerfacecolor='none',markeredgecolor='indigo',linewidth=1,markersize=4,label='deaths')
ax1.set_xticks(np.arange(fidat-fidat,endat-fidat,5))
ax1.set_xticklabels(dfla[np.arange(fidat,endat,5)])
ax1.legend()
#ax1.set_xticklabels(np.arange(fidat-fidat,endat-fidat,5),dfla[np.arange(fidat,endat,5)],rotation=90)
#ax1.xticks(np.arange(fidat-fidat,endat-fidat,5),dfla[np.arange(fidat,endat,5)],rotation=90)
fig.suptitle('COVID 19 in '+couna+', '+stana+': '+x.strftime("%x"))
ax1.grid()
ax1.set_ylabel('occurrences')
ax2.plot(np.arange(fidat-fidat,endat-fidat-1),np.diff(dfa[yoro,fidat:endat]),'-d',color='darkgoldenrod',markerfacecolor='none',markeredgecolor='indigo',linewidth=2,markersize=5,label='daily change')
ax2.set_xticks(np.arange(fidat-fidat,endat-fidat,5))
ax2.set_xticklabels(dfla[np.arange(fidat,endat,5)])
ax2.legend()
ax2.grid()
ax2.set_ylabel('daily change')
ax2.set_xlabel('date')
plt.figtext(0.035,0.04,'data: Johns Hopkins Univ., https://coronavirus.jhu.edu/map.html',color='teal')
plt.figtext(0.41,0.04,' || ',color='darkblue')
plt.figtext(0.43,0.04,'python script by John V Hurley: https://github.com/jvhurley/COVID-19-County-Time-Series',color='teal')
  
figfina=('./'+couna+'_tseries.png')
plt.savefig(figfina)
plt.show()


# In[ ]:




