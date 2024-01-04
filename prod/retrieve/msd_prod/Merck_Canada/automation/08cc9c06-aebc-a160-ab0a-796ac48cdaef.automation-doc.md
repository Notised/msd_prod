## 08cc9c06-aebc-a160-ab0a-796ac48cdaef

**Name** (not equal to External Key)**:** ATM_EventStartsNow_OLD

**Description:** n/a

**Folder:** my automations/OLD Data Model (Archived)/Online Events/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2018-10-15 12:00:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Central Europe Standard Time
* Recurrance: every hour until end date

**Notifications:**

* Complete: dmcamseuramca@merck.com
* Error: ivanjan.chattoraj@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: query_<br>SQL_UTC_Currentdate_OLD | _2.1: query_<br>SQL_EventStartsNow_OLD | _3.1: query_<br>STG_EventStartsNow_Dummy_OLD |
