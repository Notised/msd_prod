## Global Veeva Data

**Description:** To pull data together from multiple Veeva objects into data extensions. Data are still for all coutries and target data extensions are shared. This automation should be created only once per parent 

**Folder:** my automations/Veeva Data/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2019-07-24 17:00:00 +08:00
* End: 2079-06-06 00:00:00 +08:00
* Timezone: Singapore Standard Time
* Recurrance: every 3 hours until end date

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ | Step 6<br>_<small>-</small>_ | Step 7<br>_<small>-</small>_ | Step 8<br>_<small>-</small>_ | Step 9<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| _1.1: query_<br>Survey Data | _2.1: query_<br>Load_Accounts | _3.1: query_<br>Load_Account_Call_XREF_AU | _4.1: query_<br>Load_Account_Call_XREF_NZ | _5.1: query_<br>Load_Account_Call_XREF_TW | _6.1: query_<br>Load_Account_Call_CallDetail_XREF_AU | _7.1: query_<br>Load_Account_Call_CallDetail_XREF_NZ | _8.1: query_<br>Load_Account_Call_CallDetail_XREF_TW | _9.1: query_<br>Load_Call_Final |
| _1.2: query_<br>Approved_Documents | _2.2: query_<br>Load_Calls | - | - | - | - | - | - | - |
| _1.3: query_<br>Product Metrics | _2.3: query_<br>Load_Call_Details | - | - | - | - | - | - | - |
| _1.4: query_<br>User_Data | - | - | - | - | - | - | - | - |
| _1.5: query_<br>Sample_Order_ANZ | - | - | - | - | - | - | - | - |
| _1.6: query_<br>Load_CLM_Call | - | - | - | - | - | - | - | - |
