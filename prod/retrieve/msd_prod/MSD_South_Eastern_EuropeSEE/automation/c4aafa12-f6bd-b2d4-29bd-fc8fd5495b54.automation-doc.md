## c4aafa12-f6bd-b2d4-29bd-fc8fd5495b54

**Name** (not equal to External Key)**:** XD_Import_CRM_Profiles

**Description:** n/a

**Folder:** my automations/DIL Interface/

**Started by:** File Drop

**Status:** AwaitingTrigger

**File Trigger:**

* Queue Files: true
* Published: true
* Pattern: CRMProfiles_XD
* Folder:  import\production\

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: importFile_<br>XD_Import_CRM_Profiles | _2.1: query_<br>CRM_Profile_Update |
