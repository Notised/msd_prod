## NBE HQ

**Description:** Import HQ Emails 4Cs file, archive it and put the contacts from the file into a journey, which will send them respective email

**Folder:** my automations/03_Business/NBE/

**Started by:** File Drop

**Status:** InactiveTrigger

**File Trigger:**

* Queue Files: true
* Published: false
* Pattern: DE_NBE_HQ
* Folder:  import\production\

**Notifications:**

* Complete: sachidananda.prusty@msd.com
* Error: sachidananda.prusty@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: importFile_<br>NBE HQ | _2.1: query_<br>NBE HQ Archive | _3.1: query_<br>NBE_HQ_Email_Sendout |
