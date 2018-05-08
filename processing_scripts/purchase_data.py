#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 11:56:27 2018

@author: anjali
"""

import connection as engine
import pandas as pd

def purchase_trend(query, ind, cols, vals):
    data = pd.read_sql(query,engine.connect()) 
    pivot_df = data.pivot(index=ind, columns=cols, values=vals)
    pivot_df.plot.bar(stacked=True, figsize=(15,10)).legend(bbox_to_anchor=(1.0, 1.2))
    
def get_purchase_month(month):
    query = "SELECT posting_year, unc_donor_class, sum(quantity) as quantity FROM FEEED_data1.purchase_data where posting_month = '" + month + "' and fbc_donor_class = 'vendor' and quantity > 0 group by posting_year, unc_donor_class"
    return query
    
def plot_purchase_trend():
    #get data over the recorded years for months
    """
    query = "SELECT posting_year, posting_month, sum(quantity) as quantity FROM FEEED_data1.purchase_data where fbc_donor_class = 'vendor' and quantity > 0 group by posting_year, posting_month"
    data = pd.read_sql(query,engine.connect())    
    pivot_df = data.pivot(index='posting_year', columns='posting_month', values='quantity')
    pivot_df.plot.bar(stacked=True, figsize=(10,7))
    """
    
    #purchase_trend(get_purchase_month('07'),'posting_year', 'unc_donor_class','quantity')
    #purchase_trend(get_purchase_month('08'),'posting_year', 'unc_donor_class','quantity')
    #purchase_trend(get_purchase_month('10'),'posting_year', 'unc_donor_class','quantity')
    
    
plot_purchase_trend()
    
    
    