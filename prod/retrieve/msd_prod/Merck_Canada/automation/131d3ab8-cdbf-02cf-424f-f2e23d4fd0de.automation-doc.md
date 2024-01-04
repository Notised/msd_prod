## 131d3ab8-cdbf-02cf-424f-f2e23d4fd0de

**Name** (not equal to External Key)**:** CA_Data_View_Export

**Description:** n/a

**Folder:** my automations/NewDataModel (Do Not Delete)/DIL Interface/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2020-11-03 00:30:00 -05:00
* End: 2079-06-06 00:00:00 -05:00
* Timezone: Eastern Standard Time
* Recurrance: every day until end date

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ |
| --- | --- | --- | --- |
| _1.1: query_<br>Data View - Sent | _2.1: dataExtract_<br>Data View Extract - Sent | _3.1: dataExtract_<br>Data View Extract Convert - Sent | _4.1: fileTransfer_<br>Data View Transfer - Sent |
| _1.2: query_<br>Data View - Job | _2.2: dataExtract_<br>Data View Extract - Job | _3.2: dataExtract_<br>Data View Extract Convert - Job | _4.2: fileTransfer_<br>Data View Transfer - Job |
| _1.3: query_<br>Data View - Journey | _2.3: dataExtract_<br>Data View Extract - Journey | _3.3: dataExtract_<br>Data View Extract Convert - Journey | _4.3: fileTransfer_<br>Data View Transfer - Journey |
| _1.4: query_<br>Data View - Journey Activity | _2.4: dataExtract_<br>Data View Extract - Journey Activity | _3.4: dataExtract_<br>Data View Extract Convert - Journey Activity | _4.4: fileTransfer_<br>Data View Transfer - Journey Activity |
