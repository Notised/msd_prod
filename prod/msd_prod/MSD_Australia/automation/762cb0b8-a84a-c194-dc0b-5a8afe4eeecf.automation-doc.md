## 762cb0b8-a84a-c194-dc0b-5a8afe4eeecf

**Name** (not equal to External Key)**:** tracking_Complaints_transfer

**Description:** n/a

**Folder:** my automations/Tracking_extract_automation/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2019-01-25 14:00:00 +10:00
* End: 2079-06-06 00:00:00 +10:00
* Timezone: AUS Eastern Standard Time
* Recurrance: every day until end date

**Notifications:** _none_


| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: dataExtract_<br>Tracking_Complaints_data_extract | _2.1: fileTransfer_<br>tracking_Complaints_extract_transfer | _3.1: query_<br>Delete_Complaints_DE_Data |
