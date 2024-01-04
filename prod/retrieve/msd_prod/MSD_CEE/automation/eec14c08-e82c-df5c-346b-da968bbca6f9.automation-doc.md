## eec14c08-e82c-df5c-346b-da968bbca6f9

**Name** (not equal to External Key)**:** XE_Campaign_Mapping

**Description:** n/a

**Folder:** my automations/DIL Interface/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2020-11-14 00:30:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Central Europe Standard Time
* Recurrance: every day until end date

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ |
| --- | --- | --- | --- |
| _1.1: query_<br>Campaign Mapping | _2.1: dataExtract_<br>Campaign Mapping Extract | _3.1: dataExtract_<br>Campaign Mapping Convert | _4.1: fileTransfer_<br>Campaign Mapping Transfer |
