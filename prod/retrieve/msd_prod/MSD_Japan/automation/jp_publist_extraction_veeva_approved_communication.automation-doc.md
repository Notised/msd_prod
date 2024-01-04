## jp_publist_extraction_veeva_approved_communication

**Description:** n/a

**Folder:** my automations/Transactional/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2019-09-04 11:00:00 +08:00
* End: 2079-06-06 00:00:00 +08:00
* Timezone: Singapore Standard Time
* Recurrance: every week until end date

**Notifications:**

* Complete: mdesfmcmonit@merck.com
* Error: amsjapandxl2@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ |
| --- | --- | --- | --- |
| _1.1: query_<br>jp_publist_veeva_approved_communication | _2.1: wait_<br>3 Minutes | _3.1: dataExtract_<br>jp_publist_veeva_approved_communication_extract | _4.1: fileTransfer_<br>jp_publist_veeva_approved_communication_transfer |
