#create a view to have all the records for distribution
CREATE view `negative_adj_data_0617` as
SELECT * FROM FEEED_data1.fy0607_view
where Entry_Type like '%Positive%'
UNION
SELECT * FROM FEEED_data1.fy0708_view
where Entry_Type like '%Positive%'
UNION
SELECT * FROM FEEED_data1.fy0809_view
where Entry_Type like '%Positive%'
UNION
SELECT * FROM FEEED_data1.fy0910_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1011_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1112_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1213_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1314_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1415_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1516_view
where Entry_Type like '%Negative%'
UNION
SELECT * FROM FEEED_data1.fy1617_view
where Entry_Type like '%Negative%';