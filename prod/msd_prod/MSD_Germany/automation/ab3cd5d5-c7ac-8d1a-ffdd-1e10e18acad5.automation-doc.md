## ab3cd5d5-c7ac-8d1a-ffdd-1e10e18acad5

**Name** (not equal to External Key)**:** Customer_To_Territory_CS

**Description:** n/a

**Folder:** my automations/NewDataModel (Do Not Delete)/05_Customer-to-territory/

**Started by:** File Drop

**Status:** AwaitingTrigger

**File Trigger:**

* Queue Files: true
* Published: true
* Pattern: customer_2_territory
* Folder:  import\production\

**Notifications:** _none_


| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- |
| _1.1: importFile_<br>DE_Import_Customer_To_Territory_CS | _2.1: verification_<br>89eccbd5-9fa3-417b-810a-ae9a67574409 | _3.1: query_<br>Customer_To_Territory_CS | _4.1: query_<br>01_Cust_To_Terri_My_Target_combined_CS | _5.1: query_<br>02_Cust_To_Terri_My_Target_combined_per_cust_CS |
