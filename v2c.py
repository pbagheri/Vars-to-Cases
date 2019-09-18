# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 10:26:36 2018

@author: Payam
"""

import pandas as pd
import numpy as np
from os import path
#from cx_Freeze import setup, Executable

dir_path = path.dirname(path.dirname(path.abspath(__file__)))
print(dir_path)


res_dat = pd.read_csv(dir_path + '/0_input_data/love-reason-data.csv', low_memory=False)

cols = list(res_dat.columns)[2:]
cols[0]
cols[-1]
res_dat.shape

'''
for colnam in cols:
    if len(colnam[colnam.find('_',13)+1:]) > 3:
        res_dat.drop(colnam, axis=1, inplace=True)
'''


reasons_v2c = pd.DataFrame() 

resps = []
weights = []
ten_loved_brands = []



for i in range(154):
    weights = weights + list(res_dat['weights_completes_to_census'])
    resps = resps + list(res_dat['resp_id'])
    ten_loved_brands = ten_loved_brands + list(i*np.ones(len(res_dat['resp_id'])))
    
reasons_v2c['resp_id'] = pd.Series(resps)
reasons_v2c['weights'] = pd.Series(weights)
reasons_v2c['ten_loved_brands'] = pd.Series(ten_loved_brands)




for i in range(12):
    sfx = 'r' + str(i)
    selnams = [x for x in cols if x[x.find('_',13)+1:] == sfx]
    seldat = res_dat[selnams]
    #print(seldat)
    numrows = seldat.shape[0]*seldat.shape[1]
    seldat_arr = np.array(seldat)
    seldat_arr.shape
    seldat_arr_reshaped = np.array(seldat).reshape((1,numrows), order = 'F')
    seldat_arr_reshaped[0].shape    
    #print(seldat_arr)
    reasons_v2c[sfx] = pd.Series(seldat_arr_reshaped[0])




reasons_v2c.to_csv(dir_path + '\\0_output\\reasons_v2c.csv', index=False)


    
    
    
    
