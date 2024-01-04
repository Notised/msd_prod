## poc_joon_transaction_data_extract

**Description:** n/a

**Folder:** my automations/poc/Joon/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2018-11-14 11:00:00 +08:00
* End: 2018-11-14 11:00:00 +08:00
* Timezone: Singapore Standard Time
* Recurrance: run only once

**Notifications:**

* Complete: kar.joon.chew@merck.com
* Error: kar.joon.chew@merck.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: dataExtract_<br>poc_joon_transactional_data_extract | _2.1: fileTransfer_<br>poc_joon_trx_data_zip_export | _3.1: fileTransfer_<br>poc_joon_transactional_data_zip_extract |
