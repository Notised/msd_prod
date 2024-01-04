## ccd8302d-446c-43ef-affb-ebae6fdd9a45

**Name** (not equal to External Key)**:** KPI_reporting_v2_notification

**Description:** n/a

**Folder:** my automations/DAT reporting/

**Started by:** Schedule

**Status:** Ready

**Schedule:** Not defined

**Notifications:**

* Error: shailany.vizconde@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ | Step 6<br>_<small>-</small>_ | Step 7<br>_<small>-</small>_ | Step 8<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| _1.1: dataExtract_<br>KPI_datreporting_v2_move-file-to-imports | _2.1: wait_<br>1 Minutes | _3.1: importFile_<br>KPI_datreporting_v2_import-to-DE | _4.1: wait_<br>1 Minutes | _5.1: dataExtract_<br>KPI_datreporting_v2_move-file-to-Safehouse | _6.1: wait_<br>1 Minutes | _7.1: verification_<br>86c17c58-6fe2-4e97-8700-b1cea5c4aa4f | _8.1: fileTransfer_<br>KPI_datreporting_v2_from-Safehouse-to-GCE |
| - | - | - | - | - | - | - | _8.2: query_<br>KPI_datreporting_clearDE |
