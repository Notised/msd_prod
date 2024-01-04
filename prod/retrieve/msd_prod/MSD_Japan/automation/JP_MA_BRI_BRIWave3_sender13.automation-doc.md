## JP_MA_BRI_BRIWave3_sender13

**Description:** Bridion Wave3 13通目の配信（4/14配信分）


**Folder:** my automations/PROD/Bridion/BRIWave3/

**Started by:** Schedule

**Status:** Ready

**Schedule:**

* Start: 2020-04-14 11:00:00 +09:00
* End: 2020-04-14 11:00:00 +09:00
* Timezone: Tokyo Standard Time
* Recurrance: run only once

**Notifications:**

* Complete: toyoda.rie@dentsudigital.co.jp
* Error: toyoda.rie@dentsudigital.co.jp

| Step 1<br>_<small>-</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>-</small>_ | Step 5<br>_<small>-</small>_ | Step 6<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- | --- |
| _1.1: query_<br>JP_MA_BRI_ BRIWave3_jp_jr_apjuser_qa | _2.1: query_<br>JP_MA_BRI_BRIWave3_Welcome_TargetList_qa | _3.1: query_<br>JP_MA_BRI_BRIWave3_Sender14_qa | _4.1: wait_<br>12:00 PM | _5.1: emailSend_<br>JP_MA_BRI_BRIWave3_Sender13 | _6.1: query_<br>JP_MA_BRI_BRIWelcome_ExclusionMassMailList_qa |
| _1.2: query_<br>JP_MA_BRI_ BRIWave3_Account_Salesforce_8_qa | - | - | - | - | - |
| _1.3: query_<br>JP_MA_BRI_ BRIWave3_Specialty_MSD__c_Salesforce_qa | - | - | - | - | - |
| _1.4: query_<br>JP_MA_BRI_BRIWave3_msd_product_de | - | - | - | - | - |