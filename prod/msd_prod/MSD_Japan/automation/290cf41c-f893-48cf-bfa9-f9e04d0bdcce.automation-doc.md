## 290cf41c-f893-48cf-bfa9-f9e04d0bdcce

**Name** (not equal to External Key)**:** JP_MA_ZBX_MIDORI_SEND_03_02

**Description:** n/a

**Folder:** my automations/PROD/ZBX/MIDORI/3/

**Started by:** Schedule

**Status:** Ready

**Schedule:**

* Start: 2020-09-23 12:00:00 +09:00
* End: 2020-09-23 12:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: run only once

**Notifications:**

* Error: msd@directus.co.jp

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: query_<br>JP_MA_ZBX_MIDORI_QER_apjuser_SS | _2.1: query_<br>JP_MA_ZBX_MIDORI_QER_SEND_03_02 | _3.1: emailSend_<br>JP_MA_ZBX_MIDORI_UIE_SEND_03_02 |
| _1.2: query_<br>JP_MA_ZBX_MIDORI_QER_DVLS_SS | - | - |
