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


df_order = pd.read_pickle('data/orderMaster.pkl')
df_user = pd.read_pickle('data/userMaster.pkl')
# df_joined = df_order.join(df_user
# , how='inner', on='user_id', lsuffix='int', rsuffix='int')
df_joined = pd.merge(
        df_order,
        df_user,
        how='inner',
        on='user_id',
        suffixes=('order','user')
        )
print df_joined
