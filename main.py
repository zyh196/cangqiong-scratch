# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:15:08 2016

@author: yiyuezhuo
"""

'''
cityId:510100
scope:city
date:3
dimension:satisfy
num:300
'''

import requests
import json
import pandas as pd

def get(cityId='510100',scope='city',date='3',dimension='satisfy',num=1000):
    url='http://v.kuaidadi.com/point'
    params={'cityId':cityId,'scope':scope,'date':date,'dimension':dimension,'num':num}
    res=requests.get(url,params=params)
    return json.loads(res.content)
    
class Downloader(object):
    def __init__(self):
        self.cityId_list=['510100']
        self.scope_list=['city']
        self.date_list=[str(i) for i in range(7)]
        self.dimension_list=['distribute','satisfy','demand','response','money']
        # money好像get字段不太一样，不过暂且用一样的方法请求
        self.num_list=[1000]
        
        self.pkey=('cityId','scope','date','dimension','num')
        
        self.data={}
    def keys(self):
        for cityId in self.cityId_list:
            for scope in self.scope_list:
                for date in self.date_list:
                    for dimension in self.dimension_list:
                        for num in self.num_list:
                            yield (cityId,scope,date,dimension,num)
    def download(self,verbose=True):
        for key in self.keys():
            pkey=self.pkey
            params=dict(zip(pkey,key))
            self.data[key]=get(**params)
            if verbose:
                print 'clear',key
                
def to_csv(key,json_d,prefix='data/'):
    data=json_d['result']['data']
    city_id=json_d['result']['cityID']
    date=json_d['result']['date']
    dimension=key[3]
    fname='_'.join([dimension,date,city_id,'.csv'])
    fname=fname.replace('/','.')
    fname=prefix+fname
    cdata=[]
    for hour,section in enumerate(data):
        for record in section:
            cdata.append([hour]+record[1:])
    df=pd.DataFrame(cdata,columns=['hour','longitude','latitude','value'])
    df.to_csv(fname)
    
def to_csv_all(datas,path='data/'):
    for key,json_d in datas.items():
        to_csv(key,json_d,prefix=path)

'''
downloader=Downloader()
downloader.download()
to_csv_all(downloader.data)
'''