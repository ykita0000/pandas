#!/usr/bin/python
# coding:utf-8
import numpy as np
import datetime
import functools
import itertools
import pandas as pd
from gimei import Gimei

import matplotlib.pyplot as plt
import seaborn as sns


norders = 1000
ORDERID = range(norders)
nusers = 100
USERID = np.random.choice(range(nusers), size=norders)

ndays = 30
day0 = datetime.date.today()
days = [day0 - datetime.timedelta(days=i) for i in xrange(ndays)]
DATE = np.random.choice(days, size=norders)
DATE.sort()

PAYMENTS = map(int, np.random.exponential(10000, size=norders))

df = pd.DataFrame({
    "payment": PAYMENTS,
    "order_id": ORDERID,
    "date": DATE,
    "user_id": USERID
    })
df.to_pickle('data/orderMaster.pkl')
