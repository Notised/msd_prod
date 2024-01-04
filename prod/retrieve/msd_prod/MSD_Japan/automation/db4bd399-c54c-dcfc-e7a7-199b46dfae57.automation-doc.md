## db4bd399-c54c-dcfc-e7a7-199b46dfae57

**Name** (not equal to External Key)**:** SURVEY_20210928

**Description:** n/a

**Folder:** my automations/POC/ALL/Welcome/survey/20210928/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2021-09-28 12:00:00 +09:00
* End: 2079-06-06 00:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: every hour until end date

**Notifications:** _none_


| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: query_<br>TEST_welcomejourney_janrain_pending_20210928 | _2.1: query_<br>TEST_JP_MA_ALL_Welcome_first_pending_QER_20210928 |
| _1.2: query_<br>TEST_welcomejourney_janrain_validated_20210982 | _2.2: query_<br>TEST_janrain_newusers_union_20210928 |
| _1.3: query_<br>TEST_JP_MA_ALL_Welcome_ENTRY_QER_20210928 | - |
