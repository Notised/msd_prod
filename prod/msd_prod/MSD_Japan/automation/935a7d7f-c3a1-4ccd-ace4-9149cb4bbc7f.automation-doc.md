## 935a7d7f-c3a1-4ccd-ace4-9149cb4bbc7f

**Name** (not equal to External Key)**:** AS_MSD Connect_Campaign_180528

**Description:** n/a

**Folder:** my automations/japan/02_Campaign/2018/201805/

**Started by:** Schedule

**Status:** Ready

**Schedule:**

* Start: 2018-05-28 14:00:00 +09:00
* End: 2018-05-28 14:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: run only once

**Notifications:**

* Complete: msd@directus.co.jp
* Error: msd@directus.co.jp

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- |
| _1.1: query_<br>Q_msdconnect_target | _2.1: query_<br>99_Q_msdconnect_seg_all_old | _3.1: filter_<br>Filter_CPN_180319 | _4.1: wait_<br>04:00 午後 | _5.1: emailSend_<br>MA_MSD Connect_Campaign_プレバイミス_180528 |
