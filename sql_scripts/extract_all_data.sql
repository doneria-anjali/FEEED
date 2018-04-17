#create a view to have all the records for distribution
CREATE view `FY_data_0617` as
SELECT * FROM FEEED_data1.fy0607_view
UNION
SELECT * FROM FEEED_data1.fy0708_view
UNION
SELECT * FROM FEEED_data1.fy0809_view
UNION
SELECT * FROM FEEED_data1.fy0910_view
UNION
SELECT * FROM FEEED_data1.fy1011_view
UNION
SELECT * FROM FEEED_data1.fy1112_view
UNION
SELECT * FROM FEEED_data1.fy1213_view
UNION
SELECT * FROM FEEED_data1.fy1314_view
UNION
SELECT * FROM FEEED_data1.fy1415_view
UNION
SELECT * FROM FEEED_data1.fy1516_view
UNION
SELECT * FROM FEEED_data1.fy1617_view;

select * FROM FY_data_0617;