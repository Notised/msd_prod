## e16dbcae-09ef-8e8d-8ca7-a6de9e03ac5b

**Name** (not equal to External Key)**:** ATM_Rejected_Duplicated_users

**Description:** Rejected users during validation because of duplicate account found

**Folder:** my automations/2.Business/2_SEGMENT/PROJECTS/Duplicated_Users/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2023-06-13 08:00:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Romance Standard Time
* Recurrance: every hour until end date

**Notifications:**

* Error: jose.maria.esteban@merck.com

| Step 1<br>_<small>Add user to journey entry source that match criteria</small>_ |
| --- |
| _1.1: query_<br>QRY_Rejected_Duplicated_users |
