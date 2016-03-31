# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:22:31 2016

@author: yiyuezhuo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

demand_df=pd.read_csv('data/demand_2016.03.10_510100_.csv',index_col=0)

demand_df['value'].groupby(demand_df['hour']).sum().plot()
plt.title('demand')
plt.show()

def _value_weight(df,lon,lat,alpha=1.0):
    dis=np.sqrt((df['longitude']-lon)**2+(df['latitude']-lat)**2)
    return np.sum(np.exp(-alpha*dis)*df['value'])
    
def weight_plot(df,bins=100,left=0.02,right=0.98,alpha=1.0):
    x=np.linspace(df['longitude'].quantile(left),df['longitude'].quantile(right),bins)
    y=np.linspace(df['latitude'].quantile(left),df['latitude'].quantile(right),bins)
    X,Y=np.meshgrid(x,y)
    shape=X.shape
    Z=np.zeros(shape)
    for x in range(shape[0]):
        for y in range(shape[1]):
            Z[(x,y)]=_value_weight(df,X[(x,y)],Y[(x,y)],alpha=alpha)
    plt.imshow(Z)
    plt.show()
    return Z
    
    
def loc_seq(df,longitude=104.06,latitude=30.67):
    distance=np.sqrt((df['longitude']-longitude)**2+(df['latitude']-latitude)**2)
    df2=df.groupby(df['hour']).apply(lambda df:df.ix[distance.ix[df.index].sort(inplace=False)[:3].index].mean())
    df2.index=df2['hour']
    return df2
    
satisfy_df=pd.read_csv('data/satisfy_2016.03.10_510100_.csv')
df2=loc_seq(satisfy_df)
df2['value'].plot()
plt.title('satisfy')
plt.plot()
#def bi_arg(df,distance):
#    return df.ix[distance==distance.ix[df.index].min()]