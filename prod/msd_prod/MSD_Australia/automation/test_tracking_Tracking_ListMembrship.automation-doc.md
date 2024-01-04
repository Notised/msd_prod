## test_tracking_Tracking_ListMembrship

**Name** (not equal to External Key)**:** Tracking_ListMembrship

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
| _1.1: importFile_<br>Tracking_ListMembership_Import | _2.1: query_<br>au_update_country_code_ListMembership | _3.1: query_<br>nz_update_country_code_ListMembership | _4.1: script_<br>Delete_listMembershup_records |
