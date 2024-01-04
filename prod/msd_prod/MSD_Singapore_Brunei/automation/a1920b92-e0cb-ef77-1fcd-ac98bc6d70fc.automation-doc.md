## a1920b92-e0cb-ef77-1fcd-ac98bc6d70fc

**Name** (not equal to External Key)**:** SG_DIL_Export

**Description:** n/a

**Folder:** my automations/PROD/DIL Interface/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2020-09-04 01:30:00 +08:00
* End: 2079-06-06 00:00:00 +08:00
* Timezone: Singapore Standard Time
* Recurrance: every day until end date

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: dataExtract_<br>SG_Export_Outbound_Data | _2.1: fileTransfer_<br>SG_Export_Outbound_Data |
