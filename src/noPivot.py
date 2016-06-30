#!/usr/bin/python
#coding:utf-8
'''
name   : .py
author : ykita
date   : 
memo   : think how not to use pivot
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

pv2 = pd.pivot_table(df, values='price',index='date', columns='device_type',aggfunc=np.sum, fill_value=0)
# pv2.fillna(0,inplace=True)
print pv2
pv2.plot()
plt.show()
