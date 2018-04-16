create view `fy1617_view` as
select Posting_Date, Entry_Type, Source_No_, Location_Code, Inventory_Posting_Group, Source_Posting_Group, 
Quantity, Source_Type, Branch_Code, UNC_Donor_ID_Code, 
UNC_Donor_Class_of_Trade_Code, FBC_Donor_Class_of_Trade, Vendor_Type
from FY1617;