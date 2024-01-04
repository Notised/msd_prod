## a2f8f8bc-0ffd-48ed-af45-ce60c8efceb7

**Name** (not equal to External Key)**:** JP_MA_BRI_Properuse_sender6

**Description:** n/a

**Folder:** my automations/PROD/Bridion/Properuse/

**Started by:** Schedule

**Status:** Ready

**Schedule:**

* Start: 2019-11-05 15:00:00 +09:00
* End: 2019-11-05 15:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: run only once

**Notifications:**

* Complete: toyoda.rie@dentsudigital.co.jp
* Error: toyoda.rie@dentsudigital.co.jp

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- |
| _1.1: query_<br>JP_MA_BRI_Properuse_msd_product_list | _2.1: query_<br>JP_MA_BRI_Properuse_LinkClick | _3.1: query_<br>JP_MA_BRI_Properuse_sender6_1 | _4.1: wait_<br>04:00 午後 | _5.1: emailSend_<br>JP_MA_BRI_Properuse_sender6_1 |
| _1.2: query_<br>JP_MA_BRI_Properuse_Dataview_Click | - | _3.2: query_<br>JP_MA_BRI_Properuse_sender6_2 | - | _5.2: emailSend_<br>JP_MA_BRI_Properuse_sender6_2 |
