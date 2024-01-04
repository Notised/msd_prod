## 3e2c5c2b-48eb-b42e-36e7-e44ce41fbaee

**Name** (not equal to External Key)**:** JP_MA_GS_WELCOME1

**Description:** n/a

**Folder:** my automations/PROD/GS/JP_MA_GS_WELCOME/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2020-09-03 12:00:00 +09:00
* End: 2079-06-06 00:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: every week until end date

**Notifications:**

* Complete: yuko.shibata@merck.com
* Error: yuko.shibata@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- |
| _1.1: query_<br>JP_MA_GS_WELCOME_upload | _2.1: query_<br>JP_MA_GS_WELCOME_Query_Mail_O_1 | _3.1: emailSend_<br>JP_MA_GS_WELCOME_O_1 | _4.1: query_<br>JP_MA_GS_WELCOME_Update_FilterdFlg | _5.1: query_<br>JP_MA_RT_NR_WELCOME_Update_SentFlg1 |
| - | _2.2: query_<br>JP_MA_GS_WELCOME_Query_Mail_S_1 | _3.2: emailSend_<br>JP_MA_GS_WELCOME_S_1 | - | - |
