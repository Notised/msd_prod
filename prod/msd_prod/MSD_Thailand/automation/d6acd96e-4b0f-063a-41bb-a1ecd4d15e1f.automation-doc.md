## d6acd96e-4b0f-063a-41bb-a1ecd4d15e1f

**Name** (not equal to External Key)**:** TH_Publist_Commercial_Email_Communication

**Description:** n/a

**Folder:** my automations/PROD/Publication List Extract/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2021-02-01 18:30:00 +05:30
* End: 2079-06-06 00:00:00 +05:30
* Timezone: India Standard Time
* Recurrance: every week until end date

**Notifications:**

* Complete: mdesfmcmonit@merck.com
* Error: mdesfmcmonit@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: query_<br>TH_Publist_Commercial_Email_Communication | _2.1: dataExtract_<br>TH_Publist_Commercial_Email_Communication_Extract | _3.1: fileTransfer_<br>TH_Publist_Commercial_Email_Communication_Transfer |
