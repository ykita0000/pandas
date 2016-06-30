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

nusers = 100
USERID = range(nusers)
NAME = [ Gimei().name for _ in xrange(nusers) ]
ADDRESS = [ Gimei().address for _ in xrange(nusers) ]
df = pd.DataFrame({
    "address": ADDRESS,
    "name": NAME,
    "user_id": USERID
    })
print df
df.to_pickle('data/userMaster.pkl')
