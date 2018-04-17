#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 20:10:25 2018

@author: anjali
"""

import connection as conn
import pandas as pd

def read_table(table_name):
    engine = conn.connect()
    datafull = pd.read_sql_table(table_name, engine)
    return datafull, engine

def create_final_df(record):
    df = pd.DataFrame(columns=['posting_date','posting_year','posting_month',
                               'source_no','location_code',
                               'inventory_posting_group',
                               'source_posting_group','quantity',
                               'source_type','branch_code',
                               'unc_donor_code','unc_donor_class', 
                               'fbc_donor_class','vendor_type'])
    
    #clean data
    posting_date = record['Posting_Date']
    posting_date = posting_date.replace("\"", "").strip()
    if "-" in posting_date:
        split_string = posting_date.split("-")
        year = split_string[0]
        month = split_string[1]
    elif "/" in posting_date:
        split_string = posting_date.split("/")
        year_str = split_string[2].split(" ")
        year = year_str[0]
        month = split_string[0]
        if len(month) == 1:
            month = str(0) + month
    #print(year)
    #print(month)
    
    location_code = record['Location_Code'].lower().replace("\"", "").strip()
    
    inventory_posting_grp = record['Inventory_Posting_Group'].lower().replace("\"", "").strip()
    
    source_posting_grp = record['Source_Posting_Group'].lower().replace("\"", "").strip()
    
    source_type = record['Source_Type'].lower().replace("\"", "").strip()
    
    branch_code = record['Branch_Code'].lower().replace("\"", "").strip()
    
    unc_donor_code = record['UNC_Donor_ID_Code']
    
    unc_donor_class = record['UNC_Donor_Class_of_Trade_Code'].lower().replace("\"", "").strip() 
    
    fbc_donor_class = record['FBC_Donor_Class_of_Trade'].lower().replace("\"", "").strip()
    
    vendor_type = record['Vendor_Type'].lower().replace("\"", "").strip()
    
    #insert data to dataframe
    list_data = pd.DataFrame([[posting_date, year, month, 
                               int(record['Source_No_']),
                               location_code, inventory_posting_grp,
                               source_posting_grp, int(record['Quantity']),
                               source_type, branch_code, int(unc_donor_code),
                               unc_donor_class, fbc_donor_class,vendor_type]],
                               columns=['posting_date','posting_year',
                                         'posting_month',
                                         'source_no','location_code',
                                         'inventory_posting_group',
                                         'source_posting_group','quantity',
                                         'source_type','branch_code',
                                         'unc_donor_code','unc_donor_class', 
                                         'fbc_donor_class','vendor_type'])
    df = df.append(list_data, ignore_index=True)
    return df
    
    
def add_purchase_to_table(df, engine, final_name):
    df.to_sql(name=final_name, con=engine, if_exists='append', index=False)


def clean_purchase_data():
    purchase_data_df, engine = read_table('purchase_data_0617')
    print("Records fetched = " + str(len(purchase_data_df)))
    
    for count in range(len(purchase_data_df)):
        record = purchase_data_df.iloc[count]
        #print(record)
        df = create_final_df(record)
        #print(df)
        add_purchase_to_table(df, engine, 'purchase_data')
        print("Inserted " + str(count+1) + " records")
        
clean_purchase_data()