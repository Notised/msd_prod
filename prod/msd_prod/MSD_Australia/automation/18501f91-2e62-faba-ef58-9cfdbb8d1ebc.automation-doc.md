## 18501f91-2e62-faba-ef58-9cfdbb8d1ebc

**Name** (not equal to External Key)**:** cHL_boolet_journey_confirmation

**Description:** n/a

**Folder:** my automations/production/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2019-08-02 16:00:00 +10:00
* End: 2079-06-06 00:00:00 +10:00
* Timezone: AUS Eastern Standard Time
* Recurrance: every hour until end date

**Notifications:** _none_


| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: query_<br>au_key_haem_cHL_stage | _2.1: journeyEntry_<br>AU_KEH_BookletRequest_Stage-rep | _3.1: journeyEntry_<br>AU_KEH_BookletRequest_Stage |
| _1.2: query_<br>au_key_heam_stage-rep | - | - |
