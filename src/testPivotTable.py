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

df = pd.read_pickle('data/orderMaster.py')

pv1 = pd.pivot_table(df, values='payment', rows=['user_id','date'])
print pv1

df.groupby(['user_id', 'user_id']).sum()
pv2 = pd.pivot_table(df, values='payment',rows=['date',], cols='user_id')
pv2.fillna(0, inplace=True)
print pv2
pv2.plot()
plt.show()
