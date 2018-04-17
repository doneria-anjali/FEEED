#create a view to have all the records for distribution
CREATE view `purchase_data_0617` as
SELECT * FROM FEEED_data1.fy0607_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy0708_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy0809_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy0910_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1011_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1112_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1213_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1314_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1415_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1516_view
where Entry_Type like '%Purchase%'
UNION
SELECT * FROM FEEED_data1.fy1617_view
where Entry_Type like '%Purchase%';

SELECT Inventory_Posting_Group, Source_Posting_Group, Source_Type, 
FBC_Donor_Class_of_Trade	
FROM FEEED_data1.purchase_data_0617 
group by Inventory_Posting_Group, Source_Posting_Group, Source_Type, 
FBC_Donor_Class_of_Trade;

SELECT Inventory_Posting_Group,FBC_Donor_Class_of_Trade, count(*)	
FROM FEEED_data1.purchase_data_0617 
group by Inventory_Posting_Group, FBC_Donor_Class_of_Trade;

#query to obtain data by class code
SELECT FBC_Donor_Class_of_Trade, UNC_Donor_Class_of_Trade_Code, count(*)	
FROM FEEED_data1.purchase_data_0617 
group by FBC_Donor_Class_of_Trade, UNC_Donor_Class_of_Trade_Code
order by UNC_Donor_Class_of_Trade_Code;

#to get donation, purchase data by year
select Posting_Date, FBC_Donor_Class_of_Trade, count(*)
FROM FEEED_data1.purchase_data_0617
where Posting_Date like '%2008%' and FBC_Donor_Class_of_Trade like '%Don%'
group by Posting_Date, FBC_Donor_Class_of_Trade
order by Posting_Date;

SELECT * FROM FEEED_data1.purchase_data_0617 
where FBC_Donor_Class_of_Trade like '%Ven%' and Quantity > 0;