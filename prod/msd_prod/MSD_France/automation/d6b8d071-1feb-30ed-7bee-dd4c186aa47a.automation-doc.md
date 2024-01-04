## d6b8d071-1feb-30ed-7bee-dd4c186aa47a

**Name** (not equal to External Key)**:** A_ALL_BOUNCE

**Description:** n/a

**Folder:** my automations/Business/Technical/Campaign Management/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2019-12-17 20:00:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Central Europe Standard Time
* Recurrance: every 6 hours until end date

**Notifications:**

* Error: camille.rimbault@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: query_<br>Hard Bounce | _2.1: query_<br>A_EXCLUSION_INTERNE | _3.1: query_<br>A_EXCLUSION_HELD |
| _1.2: query_<br>Block Bounce | _2.2: query_<br>A_EXCLUSION_DOMAIN | - |
| _1.3: query_<br>Soft Bounce | - | - |
