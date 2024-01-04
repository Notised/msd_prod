## f60bcc09-aeab-befb-456e-49611fcadc3f

**Name** (not equal to External Key)**:** AR_Import_CRM_Profiles

**Description:** n/a

**Folder:** my automations/DIL Interface/

**Started by:** File Drop

**Status:** AwaitingTrigger

**File Trigger:**

* Queue Files: true
* Published: true
* Pattern: CRMProfiles_AR
* Folder:  import\production\

**Notifications:**

* Complete: sfmcautomations@msd.com
* Error: sfmcautomations@msd.com

| Step 1<br>_<small>Sometimes the automation runs before the file is completely loaded, so wait 1 min before it starts.</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ |
| --- | --- | --- |
| _1.1: wait_<br>1 Minutes | _2.1: importFile_<br>AR_Import_CRM_Profiles | _3.1: query_<br>CRM_Profile_Update |
