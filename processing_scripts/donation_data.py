import connection as engine
import pandas as pd

def donation_trend_per_month(query):
    data = pd.read_sql(query,engine.connect()) 
    
    posting_day = []
    donor_code = []
    quant = []
    for count in range(len(data)):
        record = data.iloc[count]
        if "/" in record['posting_date']:
            arr = record['posting_date'].split("/")
            posting_day.append(int(arr[1]))
        elif "-" in record['posting_date']:
            arr = record['posting_date'].split("-")
            date = arr[2].split(" ")
            posting_day.append(int(date[0]))
            
        donor_code.append(int(record['unc_donor_class']))
        quant.append(int(record['quantity']))
    donation = {'posting_day': posting_day,
             'unc_donor_class': donor_code,
             'quantity': quant}

    df = pd.DataFrame.from_dict(donation)

    pivot_df = df.pivot(index='posting_day', columns='unc_donor_class', values='quantity')
    index = sorted(pivot_df.index)
    pivot_df.reindex(index)
    
    pivot_df.plot.bar(stacked=True, figsize=(15,10)).legend(bbox_to_anchor=(1.0, 1.2))

def donation_trend(query, ind, cols, vals):
    data = pd.read_sql(query,engine.connect()) 
    pivot_df = data.pivot(index=ind, columns=cols, values=vals)
    pivot_df.plot.bar(stacked=True, figsize=(15,10)).legend(bbox_to_anchor=(1.0, 1.2))
    
def get_donation(year, month):
    query = "SELECT posting_date, unc_donor_class, sum(quantity) as quantity FROM FEEED_data1.purchase_data where posting_year = " + "'" + year + "' and fbc_donor_class ='donor' and quantity > 0 and posting_month = '" + month + "' and unc_donor_class != 'null' group by posting_date, unc_donor_class"
    return query    

def get_donation_month(month):
    query = "SELECT posting_year, unc_donor_class, sum(quantity) as quantity FROM FEEED_data1.purchase_data where posting_month = '" + month + "' and fbc_donor_class = 'donor' and quantity > 0 and unc_donor_class != 'null' group by posting_year, unc_donor_class"
    return query
    
def plot_donation_trend():
    #get data over the recorded years for months
    """
    query = "SELECT posting_year, posting_month, sum(quantity) as quantity FROM FEEED_data1.purchase_data where fbc_donor_class = 'donor' and quantity > 0 group by posting_year, posting_month"
    data = pd.read_sql(query,engine.connect())    
    pivot_df = data.pivot(index='posting_year', columns='posting_month', values='quantity')
    pivot_df.plot.bar(stacked=True, figsize=(10,7))
    """
    """
    donation_trend(get_donation_month('03'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('04'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('05'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('06'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('07'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('08'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('09'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('10'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('11'),'posting_year', 'unc_donor_class','quantity')
    donation_trend(get_donation_month('12'),'posting_year', 'unc_donor_class','quantity')
    """
    #plot for Jan
    #donation_trend(get_donation_month('01'),'posting_year', 'unc_donor_class','quantity')
    #donation_trend_per_month(get_donation('2012', '01'))
    #donation_trend_per_month(get_donation('2013', '01'))
    #donation_trend_per_month(get_donation('2014', '01'))
    #donation_trend_per_month(get_donation('2015', '01'))
    #donation_trend_per_month(get_donation('2016', '01'))
    #donation_trend_per_month(get_donation('2017', '01'))
    
    donation_trend_per_month(get_donation('2011', '12'))
    donation_trend_per_month(get_donation('2012', '12'))
    donation_trend_per_month(get_donation('2013', '12'))
    donation_trend_per_month(get_donation('2014', '12'))
    donation_trend_per_month(get_donation('2015', '12'))
    donation_trend_per_month(get_donation('2016', '12'))
    #donation_trend_per_month(get_donation('2017', '05'))

plot_donation_trend()
    
    
    