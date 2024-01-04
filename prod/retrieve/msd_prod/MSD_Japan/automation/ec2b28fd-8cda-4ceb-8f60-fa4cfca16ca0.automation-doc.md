## ec2b28fd-8cda-4ceb-8f60-fa4cfca16ca0

**Name** (not equal to External Key)**:** AS_MSD Connect_Regular_181023

**Description:** n/a

**Folder:** my automations/japan/01_Regular/2018/201810/

**Started by:** Schedule

**Status:** Ready

**Schedule:**

* Start: 2018-10-23 14:00:00 +09:00
* End: 2018-10-23 14:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: run only once

**Notifications:**

* Complete: msd@directus.co.jp
* Error: msd@directus.co.jp

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ | Step 6<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- | --- |
| _1.1: query_<br>Q_msdconnect_target | _2.1: query_<br>99_Q_msdconnect_seg_all_old | _3.1: query_<br>99_Q_msdconnect_seg_pharma_old | _4.1: query_<br>99_Q_msdconnect_seg_doctor_old | _5.1: wait_<br>04:00 午後 | _6.1: emailSend_<br>MA_MSD Connect_Regular_医師用_181023 |
| - | - | - | - | - | _6.2: emailSend_<br>MA_MSD Connect_Regular_薬剤師用_181023 |
