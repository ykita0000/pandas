#!/usr/bin/python
#coding:utf-8
'''
name   : .py
author : ykita
date   : 
memo   :  
'''
import os, os.path
import sys

import numpy as np
import datetime
import functools
import itertools
import pandas as pd
from gimei import Gimei

import matplotlib.pyplot as plt
import seaborn as sns

pkl = pd.read_pickle('data/createMasterTables.pkl')
df_order = pkl["order"]
df_goods = pkl["goods"]
df = pd.merge(df_order, df_goods, how="inner")

pv1 = pd.pivot_table(df, values='price', index=['user_id','date'])
print pv1

df.groupby(['user_id', 'user_id']).sum()
pv2 = pd.pivot_table(df, values='price',index=['date',], columns='user_id')
pv2.fillna(0, inplace=True)
print pv2
pv2.plot()
plt.show()
