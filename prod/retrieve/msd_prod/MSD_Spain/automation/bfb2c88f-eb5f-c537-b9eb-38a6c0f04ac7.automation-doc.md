## bfb2c88f-eb5f-c537-b9eb-38a6c0f04ac7

**Name** (not equal to External Key)**:** ATM_Import_News_Sunday

**Description:** This Automation imports El Sevier CSVs to get the most updated news for MSD Now Widget included in Sunday Digest newsletters

**Folder:** my automations/2.Business/Imports/

**Started by:** File Drop

**Status:** InactiveTrigger

**File Trigger:**

* Queue Files: true
* Published: false
* Pattern: Noticias_
* Folder:  import\

**Notifications:** _none_


| Step 1<br>_<small>These Import Activities load the news to a DE for each Customer Type</small>_ |
| --- |
| _1.1: importFile_<br>ES_Import_News_Farmacias |
| _1.2: importFile_<br>ES_Import_News_Enfermeria |
| _1.3: importFile_<br>ES_Import_News_Medicos |
