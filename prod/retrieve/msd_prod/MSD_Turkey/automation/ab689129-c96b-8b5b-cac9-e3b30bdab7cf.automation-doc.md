## ab689129-c96b-8b5b-cac9-e3b30bdab7cf

**Name** (not equal to External Key)**:** TR_Import_CRM_Profiles

**Description:** n/a

**Folder:** my automations/DIL Interface/

**Started by:** File Drop

**Status:** AwaitingTrigger

**File Trigger:**

* Queue Files: true
* Published: true
* Pattern: CRMProfiles_TR
* Folder:  import\production\

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ |
| --- | --- |
| _1.1: importFile_<br>TR_Import_CRM_Profiles | _2.1: query_<br>CRM_Profile_Update |
