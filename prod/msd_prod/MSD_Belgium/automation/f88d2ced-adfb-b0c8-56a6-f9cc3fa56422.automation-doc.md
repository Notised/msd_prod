## f88d2ced-adfb-b0c8-56a6-f9cc3fa56422

**Name** (not equal to External Key)**:** NBX_AWS_Import_Belgium_prod

**Description:** n/a

**Folder:** my automations/NBX/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2022-09-01 06:00:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Romance Standard Time
* Recurrance: every week until end date

**Notifications:**

* Error: joost.van.driessche@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: importFile_<br>NBX_S3Import_Belgium | _2.1: importFile_<br>NBX_S3_Import_Archive_Belgium |
