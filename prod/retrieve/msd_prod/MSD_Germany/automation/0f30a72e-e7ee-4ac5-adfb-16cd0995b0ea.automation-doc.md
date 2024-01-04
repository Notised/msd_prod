## 0f30a72e-e7ee-4ac5-adfb-16cd0995b0ea

**Name** (not equal to External Key)**:** MDM_HCPPrimary_Data_Load

**Description:** Data load for MDM_CRM_Data DE, and populating HCP Primary DE with MDM_CRM, COH, DIH and Token from all subscriber.

**Folder:** my automations/NewDataModel (Do Not Delete)/Data Load/

**Started by:** File Drop

**Status:** AwaitingTrigger

**File Trigger:**

* Queue Files: true
* Published: true
* Pattern: CRMProfiles_DE
* Folder:  import\production\

**Notifications:** _none_


| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ | Step 6<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- | --- |
| _1.1: importFile_<br>MDM_CRM_Profile_Data_load | _2.1: query_<br>MDM_CRM_HCPPrimaryDEDataPopulation | _3.1: query_<br>DIH-HCPPrimaryDEDataPopulation | _4.1: query_<br>ConsentHub-HCPPrimaryDEDataPopulation | _5.1: query_<br>NoPrimaryinCOH-HCPPrimaryDEDataPopulation | _6.1: query_<br>Token-HCPPrimaryDEDataPopulation |
