# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas as pd

"""
数据库常数
"""
#_ENGINE_ ='mysql://root:gree@123@172.16.65.13/test?charset=utf8')
_ENGINE_ = 'sqlite:///sharedata.db'
engine = create_engine(_ENGINE_)

def save_data(tablename, dataframe):
    dataframe.to_sql(tablename, engine, if_exists='append',chunksize = 1000)

def read_data(sql):
    return pd.read_sql(sql, engine)

#daily = pd.read_excel('D:/Work/Git/dqInvestExplorerPython.git/50etf_smart_alpha_backtester.xlsx', 'HistoricalData')[1:]
sql = 'select * from histdate'
data = read_data(sql)
print data

