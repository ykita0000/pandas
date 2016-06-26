#!/usr/bin/python
# coding:utf-8
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

def generate_user_table():
    nusers = 100
    USERID = range(nusers)
    NAME = [ Gimei().name for _ in xrange(nusers) ]
    ADDRESS = [ Gimei().address for _ in xrange(nusers) ]
    df = pd.DataFrame({
        "address": ADDRESS,
        "name": NAME,
        "user_id": USERID
        })
    return df

def generate_goods_table():
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
    return df


def generate_order_table():
    norders = 1000
    ORDERID = range(norders)

    nusers = 100
    USERID = np.random.choice(range(nusers), size=norders)

    ngoods = 100
    GOODSID = np.random.choice(range(ngoods), size=norders)
    
    ndays = 30
    day0 = datetime.date.today()
    days = [day0 - datetime.timedelta(days=i) for i in xrange(ndays)]
    DATE = np.random.choice(days, size=norders)
    DATE.sort()

    USERID = np.random.choice(range(nusers), size=norders)

    df = pd.DataFrame({
        "date": DATE,
        "goods_id": GOODSID,
        "user_id": USERID
        })
    return df

norders = 1000
nusers = 100
ngoods = 100
ndays = 30

df_users = generate_user_table()
df_goods = generate_goods_table()
df_order = generate_order_table()

print df_order
print df_goods
print df_users


df_joined = pd.merge(
        df_order,
        df_goods,
        how='inner',
        on='goods_id',
        suffixes=('order','user')
        )
print df_joined.sort('date')
