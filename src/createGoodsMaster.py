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

ngoods = 100
GOODSID = range(ngoods)
# NAME = [ Gimei().name for _ in xrange(ngoods) ]
REGION = [ Gimei().address.prefecture.kanji for _ in xrange(ngoods) ]
PRICES = map(int, np.random.exponential(10000, size=ngoods))
df = pd.DataFrame({
    "region": REGION,
    # "name": NAME,
    "goods_id": GOODSID,
    "price": PRICES
    })
rint df
df.to_pickle('data/goodsMaster.pkl')

