## b9222abc-6cf3-baa0-78fc-a1360eb4ae3d

**Name** (not equal to External Key)**:** SFMCToVeevaChildANZ_IDMappings_Version1

**Description:** n/a

**Folder:** my automations/After MDE/SFMCToVeeva/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2021-03-18 01:45:00 +10:00
* End: 2079-06-06 00:00:00 +10:00
* Timezone: AUS Eastern Standard Time
* Recurrance: every day until end date

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ |
| --- | --- | --- | --- |
| _1.1: query_<br>Multiple UUID count_Version1 | _2.1: query_<br>MDM UUID Matching_Version1 | _3.1: query_<br>SFID MDM UUID Matching_Version1 | _4.1: query_<br>UpdateSharedDE_Version1 |
| _1.2: query_<br>VeevaAccounts_Version1 | - | - | - |
