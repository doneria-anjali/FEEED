#create a view to have all the records for distribution
CREATE view `transfer_data_0617` as
SELECT * FROM FEEED_data1.fy0607_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy0708_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy0809_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy0910_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1011_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1112_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1213_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1314_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1415_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1516_view
where Entry_Type like '%Transfer%'
UNION
SELECT * FROM FEEED_data1.fy1617_view
where Entry_Type like '%Transfer%';