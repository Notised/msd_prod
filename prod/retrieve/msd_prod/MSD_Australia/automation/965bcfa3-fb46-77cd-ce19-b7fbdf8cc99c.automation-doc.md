## 965bcfa3-fb46-77cd-ce19-b7fbdf8cc99c

**Name** (not equal to External Key)**:** Tracking_SendJobs

**Description:** n/a

**Folder:** my automations/Tracking_extract_automation/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2019-01-25 13:00:00 +10:00
* End: 2079-06-06 00:00:00 +10:00
* Timezone: AUS Eastern Standard Time
* Recurrance: every day until end date

**Notifications:** _none_


| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ |
| --- | --- | --- | --- |
| _1.1: importFile_<br>Tracking_SendJobs_Import | _2.1: query_<br>Send_Jobs_Country_code_update_NZ | _3.1: query_<br>Send_Jobs_Country_code_update_AU | _4.1: script_<br>Delete_sendjobs_records |
