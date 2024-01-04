## NBE VVA

**Description:**  Import Veeva Suggestions 4Cs file, archive it and put the contacts from the file into a journey, which will send them respective suggestions

**Folder:** my automations/03_Business/NBE/

**Started by:** File Drop

**Status:** InactiveTrigger

**File Trigger:**

* Queue Files: true
* Published: false
* Pattern: DE_NBE_VVA
* Folder:  import\production\

**Notifications:**

* Complete: jean-paul.super@msd.de
* Error: jean-paul.super@msd.de

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: query_<br>EmptySource_NBE_VVA | _2.1: importFile_<br>NBE VVA Import | _3.1: query_<br>NBE VVA Archive |
