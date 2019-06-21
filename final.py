#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import numpy as np
#from netCdf4 import Dataset
import pandas
import os
import math


# In[3]:


path="C:\\Users\\ayush\\Desktop\\cmip5_download-master\\cdnc_swcf\\historical\\MIROC5\\"


# In[53]:





# In[56]:





# In[51]:


# lat=data["lat"].values
# lat[69]


# In[44]:


# lon=data["lon"].values
# lon[91]


# In[48]:


# for i in range(len(lat)):
#     if(lat[i]==7.70422148):
#         x1=i
#     if(lat[i]==38.52105553):
#         x2=i
#         break
        
# for i in range(len(lon)):
#     if(lon[i]==68.90625):
#         y1=i
#     if(lon[i]==97.03125):
#         y2=i
#         break
        
# print(x1,x2)
# print(y1,y2)


# In[64]:


# india=data.isel(lon=range(49,69),lat=range(69,91))
# india


# In[78]:


# india2=data1.isel(lon=range(49,69),lat=range(69,91))
# len(india2["time"])


# In[76]:


combined = xr.concat((india,india2),dim = 'time')


# In[77]:


len(combined["time"])


# In[4]:


data=xr.open_dataset(path+str(os.listdir(path)[0]))
for i in range(1,len(os.listdir(path))):
    print(i)
    dataset=path+str(os.listdir(path)[i])
    temp=xr.open_dataset(dataset)
    data=xr.concat((data,temp))
    temp.close()
    
    
data.to_netcdf("india_pr.nc")
    


# In[ ]:


def correlation(arr1,arr2):
    mean_1=sum(arr1)/len(arr1)
    mean_2=sum(arr2)/len(arr2)
    numo=0
    deno=0
    x=0
    y=0
    for i in range(len(arr1)):
        numo+=(arr1[i]-mean_1)*(arr2[i]-mean_2)
        x+=(arr1[i]-mean_1)**2
        y+=(arr1[i]-mean_1)**2
        
    deno+=math.sqrt(x*y)
    return(numo/deno)
        
        


# In[ ]:


thresh=0.5


# In[ ]:


data=xr.open_dataset("india_pr.nc")
values = data.pr.values
lats = data.         
        


# In[ ]:


for i in range(69,91):
    for j in range(49,69):
        arr1=data.isel(lon=j,lat=i)
        edges=[]
        for i1 in range(69,91):
            for j1 in range(49,69): 
                arr2=data.isel(lon=j1,lat=i1)
                coff=correlation(arr1,arr2)
                print(coff)
                if(coff>=thresh):
                    edges.append((i1,j1))
        values[i][j] = edges
        


# In[ ]:




