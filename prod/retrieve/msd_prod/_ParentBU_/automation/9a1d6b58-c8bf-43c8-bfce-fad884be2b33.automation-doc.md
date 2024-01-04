## 9a1d6b58-c8bf-43c8-bfce-fad884be2b33

**Name** (not equal to External Key)**:** EURAM Subscriber Status Monitoring

**Description:** Responsible for maintaining a history of status changes of subscribers of all EURAM business units

**Folder:** my automations/AMS/DO_NOT_TOUCH/Monitoring/Contacts/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2020-03-06 20:00:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Central Europe Standard Time
* Recurrance: every hour until end date

**Notifications:**

* Error: ivanjan.chattoraj@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: query_<br>EURAM Subscriber Status Changes | _2.1: query_<br>EURAM Subscriber Status Audit Trail |
