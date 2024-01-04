## 51c9d90f-b2b4-9d04-dcbf-fa071abca7e0

**Name** (not equal to External Key)**:** anz_dwh_hcp_consent_automation

**Description:** n/a

**Folder:** my automations/prod_dwh/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2018-06-05 12:00:00 +10:00
* End: 2021-02-27 13:00:00 +10:00
* Timezone: AUS Eastern Standard Time
* Recurrance: every day for 999 times

**Notifications:**

* Complete: kar.joon.chew@merck.com
* Error: kar.joon.chew@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: importFile_<br>anz_dwh_hcp_consent_all_subs_import | _2.1: importFile_<br>anz_dwh_hcp_consent_pub_list_import |
