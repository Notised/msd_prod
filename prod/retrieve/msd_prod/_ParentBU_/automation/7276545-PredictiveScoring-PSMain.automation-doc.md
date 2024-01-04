## 7276545-PredictiveScoring-PSMain

**Name** (not equal to External Key)**:** MSD Platform Enterprise-7033-7276545-PSMain

**Description:** This automation sends CURRENT data to the Data Scientists for scoring and is an important componentof the Einstein Engagement Scoring application.

**Folder:** my automations/Data Factory Utility Automations/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2020-03-02 21:18:10.11 +01:00
* End: 2100-02-11 21:18:10.11 +01:00
* Timezone: Romance Standard Time
* Recurrance: every 24 hours for 29200 times

**Notifications:** _none_


| Step 1<br>_<small>Predictive Scoring extract-upload task #01</small>_ | Step 2<br>_<small>Predictive Scoring extract-upload task #02</small>_ | Step 3<br>_<small>Predictive Scoring extract-upload task #03</small>_ | Step 4<br>_<small>Predictive Scoring extract-upload task #04</small>_ | Step 5<br>_<small>Predictive Scoring extract-upload task #05</small>_ | Step 6<br>_<small>Predictive Scoring extract-upload task #06</small>_ | Step 7<br>_<small>Predictive Scoring extract-upload task #07</small>_ | Step 8<br>_<small>Predictive Scoring extract-upload task #08</small>_ | Step 9<br>_<small>Predictive Scoring extract-upload task #09</small>_ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| _1.1: dataFactoryUtility_<br>Extract-Upload stats.Bounce into S3 | _2.1: dataFactoryUtility_<br>Extract-Upload C7302025._GeofenceDefinition into S3 | _3.1: dataFactoryUtility_<br>Extract-Upload C518000464._MobileAddress into S3 | _4.1: dataFactoryUtility_<br>Extract-Upload C7276545.PSConfig into S3 | _5.1: dataFactoryUtility_<br>Extract-Upload C518000464._MobileMessage into S3 | _6.1: dataFactoryUtility_<br>Extract-Upload C518000464.SmsMemberSharedShortCode_Config into S3 | _7.1: dataFactoryUtility_<br>Extract-Upload dbo.EmailSendDefinition into S3 | _8.1: dataFactoryUtility_<br>Extract-Upload dbo.EnterpriseMember into S3 | _9.1: dataFactoryUtility_<br>Extract-Upload C7276545.VPS_ExportDone into S3 |
| _1.2: dataFactoryUtility_<br>Extract-Upload stats.BounceDecrementQueue into S3 | _2.2: dataFactoryUtility_<br>Extract-Upload C7302025._MobileMessage into S3 | _3.2: dataFactoryUtility_<br>Extract-Upload C518000464._MobileMessageTracking into S3 | _4.2: dataFactoryUtility_<br>Extract-Upload dbo.ProgramActivityInstance into S3 | _5.2: dataFactoryUtility_<br>Extract-Upload C518000541._MobileMessage into S3 | _6.2: dataFactoryUtility_<br>Extract-Upload C518000464.SmsMemberShortCodeDistinct into S3 | _7.2: dataFactoryUtility_<br>Extract-Upload dbo.Send into S3 | _8.2: dataFactoryUtility_<br>Extract-Upload dbo.MemberTimeZone into S3 | - |
| _1.3: dataFactoryUtility_<br>Extract-Upload stats.Click into S3 | _2.3: dataFactoryUtility_<br>Extract-Upload C7302025._MobileMessageTracking into S3 | _3.3: dataFactoryUtility_<br>Extract-Upload C518000464._PushTag into S3 | _4.3: dataFactoryUtility_<br>Extract-Upload dbo.ProgramInstance into S3 | _5.3: dataFactoryUtility_<br>Extract-Upload C518000676._MobileMessage into S3 | _6.3: dataFactoryUtility_<br>Extract-Upload C518000541.SmsMemberSharedShortCode_Config into S3 | _7.3: dataFactoryUtility_<br>Extract-Upload dbo.tblEmails into S3 | _8.3: dataFactoryUtility_<br>Extract-Upload dbo.SendDefType into S3 | - |
| _1.4: dataFactoryUtility_<br>Extract-Upload stats.Complaint into S3 | _2.4: dataFactoryUtility_<br>Extract-Upload C7302025._PushAddress into S3 | _3.4: dataFactoryUtility_<br>Extract-Upload C518000541._MobileAddress into S3 | _4.4: dataFactoryUtility_<br>Extract-Upload InteractionStudio.Activity into S3 | _5.4: dataFactoryUtility_<br>Extract-Upload C518000770._MobileMessage into S3 | _6.4: dataFactoryUtility_<br>Extract-Upload C518000541.SmsMemberShortCodeDistinct into S3 | _7.4: dataFactoryUtility_<br>Extract-Upload dbo.tblLists into S3 | _8.4: dataFactoryUtility_<br>Extract-Upload dbo.tblMembers into S3 | - |
| _1.5: dataFactoryUtility_<br>Extract-Upload stats.Conversion into S3 | _2.5: dataFactoryUtility_<br>Extract-Upload C7302025._PushMessageTracking into S3 | _3.5: dataFactoryUtility_<br>Extract-Upload C518000541._MobileMessageTracking into S3 | _4.5: dataFactoryUtility_<br>Extract-Upload InteractionStudio.DefinitionInfo into S3 | _5.5: dataFactoryUtility_<br>Extract-Upload C518000889._MobileMessage into S3 | _6.5: dataFactoryUtility_<br>Extract-Upload C518000676.SmsMemberSharedShortCode_Config into S3 | - | _8.5: dataFactoryUtility_<br>Extract-Upload dbo.TimeZoneDetail into S3 | - |
| _1.6: dataFactoryUtility_<br>Extract-Upload stats.Open into S3 | _2.6: dataFactoryUtility_<br>Extract-Upload C7302025._PushSubscriptionHistory into S3 | _3.6: dataFactoryUtility_<br>Extract-Upload C518000541._PushTag into S3 | _4.6: dataFactoryUtility_<br>Extract-Upload InteractionStudio.EventDefinition into S3 | _5.6: dataFactoryUtility_<br>Extract-Upload C518000901._MobileMessage into S3 | _6.6: dataFactoryUtility_<br>Extract-Upload C518000676.SmsMemberShortCodeDistinct into S3 | - | - | - |
| _1.7: dataFactoryUtility_<br>Extract-Upload stats.Unsubscribe into S3 | _2.7: dataFactoryUtility_<br>Extract-Upload C7302025._PushTag into S3 | _3.7: dataFactoryUtility_<br>Extract-Upload C518000676._MobileAddress into S3 | _4.7: dataFactoryUtility_<br>Extract-Upload InteractionStudio.EventInstance into S3 | _5.7: dataFactoryUtility_<br>Extract-Upload C518000951._MobileMessage into S3 | _6.7: dataFactoryUtility_<br>Extract-Upload C518000770.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.8: dataFactoryUtility_<br>Extract-Upload C7302025.SmsMemberSharedShortCode_Config into S3 | _3.8: dataFactoryUtility_<br>Extract-Upload C518000676._MobileMessageTracking into S3 | - | _5.8: dataFactoryUtility_<br>Extract-Upload C518001179._MobileMessage into S3 | _6.8: dataFactoryUtility_<br>Extract-Upload C518000770.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.9: dataFactoryUtility_<br>Extract-Upload C7308288._GeofenceDefinition into S3 | _3.9: dataFactoryUtility_<br>Extract-Upload C518000676._PushTag into S3 | - | _5.9: dataFactoryUtility_<br>Extract-Upload C518001212._MobileMessage into S3 | _6.9: dataFactoryUtility_<br>Extract-Upload C518000889.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.10: dataFactoryUtility_<br>Extract-Upload C7308288._MobileMessage into S3 | _3.10: dataFactoryUtility_<br>Extract-Upload C518000770._MobileAddress into S3 | - | _5.10: dataFactoryUtility_<br>Extract-Upload C518001277._MobileMessage into S3 | _6.10: dataFactoryUtility_<br>Extract-Upload C518000889.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.11: dataFactoryUtility_<br>Extract-Upload C7308288._MobileMessageTracking into S3 | _3.11: dataFactoryUtility_<br>Extract-Upload C518000770._MobileMessageTracking into S3 | - | _5.11: dataFactoryUtility_<br>Extract-Upload C518001299._MobileMessage into S3 | _6.11: dataFactoryUtility_<br>Extract-Upload C518000901.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.12: dataFactoryUtility_<br>Extract-Upload C7308288._PushAddress into S3 | _3.12: dataFactoryUtility_<br>Extract-Upload C518000770._PushTag into S3 | - | _5.12: dataFactoryUtility_<br>Extract-Upload C518001300._MobileMessage into S3 | _6.12: dataFactoryUtility_<br>Extract-Upload C518000901.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.13: dataFactoryUtility_<br>Extract-Upload C7308288._PushMessageTracking into S3 | _3.13: dataFactoryUtility_<br>Extract-Upload C518000889._MobileAddress into S3 | - | _5.13: dataFactoryUtility_<br>Extract-Upload C518001345._MobileMessage into S3 | _6.13: dataFactoryUtility_<br>Extract-Upload C518000951.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.14: dataFactoryUtility_<br>Extract-Upload C7308288._PushSubscriptionHistory into S3 | _3.14: dataFactoryUtility_<br>Extract-Upload C518000889._MobileMessageTracking into S3 | - | _5.14: dataFactoryUtility_<br>Extract-Upload C518001346._MobileMessage into S3 | _6.14: dataFactoryUtility_<br>Extract-Upload C518000951.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.15: dataFactoryUtility_<br>Extract-Upload C7308288._PushTag into S3 | _3.15: dataFactoryUtility_<br>Extract-Upload C518000889._PushTag into S3 | - | _5.15: dataFactoryUtility_<br>Extract-Upload C518001991._MobileMessage into S3 | _6.15: dataFactoryUtility_<br>Extract-Upload C518001179.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.16: dataFactoryUtility_<br>Extract-Upload C7308288.SmsMemberSharedShortCode_Config into S3 | _3.16: dataFactoryUtility_<br>Extract-Upload C518000901._MobileAddress into S3 | - | _5.16: dataFactoryUtility_<br>Extract-Upload C518002058._MobileMessage into S3 | _6.16: dataFactoryUtility_<br>Extract-Upload C518001179.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.17: dataFactoryUtility_<br>Extract-Upload C7325705._GeofenceDefinition into S3 | _3.17: dataFactoryUtility_<br>Extract-Upload C518000901._MobileMessageTracking into S3 | - | _5.17: dataFactoryUtility_<br>Extract-Upload C518002245._MobileMessage into S3 | _6.17: dataFactoryUtility_<br>Extract-Upload C518001212.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.18: dataFactoryUtility_<br>Extract-Upload C7325705._MobileMessage into S3 | _3.18: dataFactoryUtility_<br>Extract-Upload C518000901._PushTag into S3 | - | _5.18: dataFactoryUtility_<br>Extract-Upload C518005183._MobileMessage into S3 | _6.18: dataFactoryUtility_<br>Extract-Upload C518001212.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.19: dataFactoryUtility_<br>Extract-Upload C7325705._MobileMessageTracking into S3 | _3.19: dataFactoryUtility_<br>Extract-Upload C518000951._MobileAddress into S3 | - | _5.19: dataFactoryUtility_<br>Extract-Upload C518005710._MobileMessage into S3 | _6.19: dataFactoryUtility_<br>Extract-Upload C518001277.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.20: dataFactoryUtility_<br>Extract-Upload C7325705._PushAddress into S3 | _3.20: dataFactoryUtility_<br>Extract-Upload C518000951._MobileMessageTracking into S3 | - | _5.20: dataFactoryUtility_<br>Extract-Upload C7276545._MobileMessage into S3 | _6.20: dataFactoryUtility_<br>Extract-Upload C518001277.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.21: dataFactoryUtility_<br>Extract-Upload C7325705._PushMessageTracking into S3 | _3.21: dataFactoryUtility_<br>Extract-Upload C518000951._PushTag into S3 | - | _5.21: dataFactoryUtility_<br>Extract-Upload C7295447._MobileMessage into S3 | _6.21: dataFactoryUtility_<br>Extract-Upload C518001299.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.22: dataFactoryUtility_<br>Extract-Upload C7325705._PushSubscriptionHistory into S3 | _3.22: dataFactoryUtility_<br>Extract-Upload C518001179._MobileAddress into S3 | - | _5.22: dataFactoryUtility_<br>Extract-Upload C7306157._MobileMessage into S3 | _6.22: dataFactoryUtility_<br>Extract-Upload C518001299.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.23: dataFactoryUtility_<br>Extract-Upload C7325705._PushTag into S3 | _3.23: dataFactoryUtility_<br>Extract-Upload C518001179._MobileMessageTracking into S3 | - | _5.23: dataFactoryUtility_<br>Extract-Upload C7310690._MobileMessage into S3 | _6.23: dataFactoryUtility_<br>Extract-Upload C518001300.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.24: dataFactoryUtility_<br>Extract-Upload C7325705.SmsMemberSharedShortCode_Config into S3 | _3.24: dataFactoryUtility_<br>Extract-Upload C518001179._PushTag into S3 | - | _5.24: dataFactoryUtility_<br>Extract-Upload C7313494._MobileMessage into S3 | _6.24: dataFactoryUtility_<br>Extract-Upload C518001300.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.25: dataFactoryUtility_<br>Extract-Upload C7326820._GeofenceDefinition into S3 | _3.25: dataFactoryUtility_<br>Extract-Upload C518001212._MobileAddress into S3 | - | _5.25: dataFactoryUtility_<br>Extract-Upload C7315205._MobileMessage into S3 | _6.25: dataFactoryUtility_<br>Extract-Upload C518001345.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.26: dataFactoryUtility_<br>Extract-Upload C7326820._MobileMessage into S3 | _3.26: dataFactoryUtility_<br>Extract-Upload C518001212._MobileMessageTracking into S3 | - | _5.26: dataFactoryUtility_<br>Extract-Upload C7317524._MobileMessage into S3 | _6.26: dataFactoryUtility_<br>Extract-Upload C518001345.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.27: dataFactoryUtility_<br>Extract-Upload C7326820._MobileMessageTracking into S3 | _3.27: dataFactoryUtility_<br>Extract-Upload C518001212._PushTag into S3 | - | _5.27: dataFactoryUtility_<br>Extract-Upload C7322086._MobileMessage into S3 | _6.27: dataFactoryUtility_<br>Extract-Upload C518001346.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.28: dataFactoryUtility_<br>Extract-Upload C7326820._PushAddress into S3 | _3.28: dataFactoryUtility_<br>Extract-Upload C518001277._MobileAddress into S3 | - | _5.28: dataFactoryUtility_<br>Extract-Upload C7323617._MobileMessage into S3 | _6.28: dataFactoryUtility_<br>Extract-Upload C518001346.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.29: dataFactoryUtility_<br>Extract-Upload C7326820._PushMessageTracking into S3 | _3.29: dataFactoryUtility_<br>Extract-Upload C518001277._MobileMessageTracking into S3 | - | _5.29: dataFactoryUtility_<br>Extract-Upload C7323638._MobileMessage into S3 | _6.29: dataFactoryUtility_<br>Extract-Upload C518001991.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.30: dataFactoryUtility_<br>Extract-Upload C7326820._PushSubscriptionHistory into S3 | _3.30: dataFactoryUtility_<br>Extract-Upload C518001277._PushTag into S3 | - | _5.30: dataFactoryUtility_<br>Extract-Upload C7325199._MobileMessage into S3 | _6.30: dataFactoryUtility_<br>Extract-Upload C518001991.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.31: dataFactoryUtility_<br>Extract-Upload C7326820._PushTag into S3 | _3.31: dataFactoryUtility_<br>Extract-Upload C518001299._MobileAddress into S3 | - | _5.31: dataFactoryUtility_<br>Extract-Upload C7325200._MobileMessage into S3 | _6.31: dataFactoryUtility_<br>Extract-Upload C518002058.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.32: dataFactoryUtility_<br>Extract-Upload C7326820.SmsMemberSharedShortCode_Config into S3 | _3.32: dataFactoryUtility_<br>Extract-Upload C518001299._MobileMessageTracking into S3 | - | _5.32: dataFactoryUtility_<br>Extract-Upload C7325808._MobileMessage into S3 | _6.32: dataFactoryUtility_<br>Extract-Upload C518002058.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.33: dataFactoryUtility_<br>Extract-Upload C7329600._PushTag into S3 | _3.33: dataFactoryUtility_<br>Extract-Upload C518001299._PushTag into S3 | - | _5.33: dataFactoryUtility_<br>Extract-Upload C7325809._MobileMessage into S3 | _6.33: dataFactoryUtility_<br>Extract-Upload C518002245.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.34: dataFactoryUtility_<br>Extract-Upload Stats.RefererEmailClient into S3 | _3.34: dataFactoryUtility_<br>Extract-Upload C518001300._MobileAddress into S3 | - | _5.34: dataFactoryUtility_<br>Extract-Upload C7327899._MobileMessage into S3 | _6.34: dataFactoryUtility_<br>Extract-Upload C518002245.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.35: dataFactoryUtility_<br>Extract-Upload stats.Send into S3 | _3.35: dataFactoryUtility_<br>Extract-Upload C518001300._MobileMessageTracking into S3 | - | _5.35: dataFactoryUtility_<br>Extract-Upload C7329574._MobileMessage into S3 | _6.35: dataFactoryUtility_<br>Extract-Upload C518005183.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.36: dataFactoryUtility_<br>Extract-Upload Stats.UserAgentApplication into S3 | _3.36: dataFactoryUtility_<br>Extract-Upload C518001300._PushTag into S3 | - | _5.36: dataFactoryUtility_<br>Extract-Upload C7329594._MobileMessage into S3 | _6.36: dataFactoryUtility_<br>Extract-Upload C518005183.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.37: dataFactoryUtility_<br>Extract-Upload Stats.UserAgentDevice into S3 | _3.37: dataFactoryUtility_<br>Extract-Upload C518001345._MobileAddress into S3 | - | _5.37: dataFactoryUtility_<br>Extract-Upload C7329596._MobileMessage into S3 | _6.37: dataFactoryUtility_<br>Extract-Upload C518005710.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | _2.38: dataFactoryUtility_<br>Extract-Upload Stats.UserAgentEmailClient into S3 | _3.38: dataFactoryUtility_<br>Extract-Upload C518001345._MobileMessageTracking into S3 | - | _5.38: dataFactoryUtility_<br>Extract-Upload C7329790._MobileMessage into S3 | _6.38: dataFactoryUtility_<br>Extract-Upload C518005710.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | _2.39: dataFactoryUtility_<br>Extract-Upload Stats.UserAgentOperatingSystem into S3 | _3.39: dataFactoryUtility_<br>Extract-Upload C518001345._PushTag into S3 | - | _5.39: dataFactoryUtility_<br>Extract-Upload C7329791._MobileMessage into S3 | _6.39: dataFactoryUtility_<br>Extract-Upload C7276545.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.40: dataFactoryUtility_<br>Extract-Upload C518001346._MobileAddress into S3 | - | _5.40: dataFactoryUtility_<br>Extract-Upload C7329792._MobileMessage into S3 | _6.40: dataFactoryUtility_<br>Extract-Upload C7276545.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.41: dataFactoryUtility_<br>Extract-Upload C518001346._MobileMessageTracking into S3 | - | _5.41: dataFactoryUtility_<br>Extract-Upload C7329793._MobileMessage into S3 | _6.41: dataFactoryUtility_<br>Extract-Upload C7295447.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.42: dataFactoryUtility_<br>Extract-Upload C518001346._PushTag into S3 | - | _5.42: dataFactoryUtility_<br>Extract-Upload C7329795._MobileMessage into S3 | _6.42: dataFactoryUtility_<br>Extract-Upload C7295447.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.43: dataFactoryUtility_<br>Extract-Upload C518001991._MobileAddress into S3 | - | _5.43: dataFactoryUtility_<br>Extract-Upload C7329814._MobileMessage into S3 | _6.43: dataFactoryUtility_<br>Extract-Upload C7306157.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.44: dataFactoryUtility_<br>Extract-Upload C518001991._MobileMessageTracking into S3 | - | _5.44: dataFactoryUtility_<br>Extract-Upload C7329868._MobileMessage into S3 | _6.44: dataFactoryUtility_<br>Extract-Upload C7306157.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.45: dataFactoryUtility_<br>Extract-Upload C518001991._PushTag into S3 | - | _5.45: dataFactoryUtility_<br>Extract-Upload C7330116._MobileMessage into S3 | _6.45: dataFactoryUtility_<br>Extract-Upload C7310690.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.46: dataFactoryUtility_<br>Extract-Upload C518002058._MobileAddress into S3 | - | _5.46: dataFactoryUtility_<br>Extract-Upload C7330118._MobileMessage into S3 | _6.46: dataFactoryUtility_<br>Extract-Upload C7310690.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.47: dataFactoryUtility_<br>Extract-Upload C518002058._MobileMessageTracking into S3 | - | _5.47: dataFactoryUtility_<br>Extract-Upload C7330119._MobileMessage into S3 | _6.47: dataFactoryUtility_<br>Extract-Upload C7313494.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.48: dataFactoryUtility_<br>Extract-Upload C518002058._PushTag into S3 | - | _5.48: dataFactoryUtility_<br>Extract-Upload C7330120._MobileMessage into S3 | _6.48: dataFactoryUtility_<br>Extract-Upload C7313494.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.49: dataFactoryUtility_<br>Extract-Upload C518002118._PushTag into S3 | - | _5.49: dataFactoryUtility_<br>Extract-Upload C7330128._MobileMessage into S3 | _6.49: dataFactoryUtility_<br>Extract-Upload C7315205.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.50: dataFactoryUtility_<br>Extract-Upload C518002245._MobileAddress into S3 | - | _5.50: dataFactoryUtility_<br>Extract-Upload C7330183._MobileMessage into S3 | _6.50: dataFactoryUtility_<br>Extract-Upload C7315205.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.51: dataFactoryUtility_<br>Extract-Upload C518002245._MobileMessageTracking into S3 | - | _5.51: dataFactoryUtility_<br>Extract-Upload C7330212._MobileMessage into S3 | _6.51: dataFactoryUtility_<br>Extract-Upload C7317524.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.52: dataFactoryUtility_<br>Extract-Upload C518002245._PushTag into S3 | - | _5.52: dataFactoryUtility_<br>Extract-Upload C7330214._MobileMessage into S3 | _6.52: dataFactoryUtility_<br>Extract-Upload C7317524.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.53: dataFactoryUtility_<br>Extract-Upload C518005183._MobileAddress into S3 | - | _5.53: dataFactoryUtility_<br>Extract-Upload C7330438._MobileMessage into S3 | _6.53: dataFactoryUtility_<br>Extract-Upload C7322086.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.54: dataFactoryUtility_<br>Extract-Upload C518005183._MobileMessageTracking into S3 | - | _5.54: dataFactoryUtility_<br>Extract-Upload C7330439._MobileMessage into S3 | _6.54: dataFactoryUtility_<br>Extract-Upload C7322086.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.55: dataFactoryUtility_<br>Extract-Upload C518005183._PushTag into S3 | - | _5.55: dataFactoryUtility_<br>Extract-Upload C7330441._MobileMessage into S3 | _6.55: dataFactoryUtility_<br>Extract-Upload C7323617.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.56: dataFactoryUtility_<br>Extract-Upload C518005710._MobileAddress into S3 | - | _5.56: dataFactoryUtility_<br>Extract-Upload C7330990._MobileMessage into S3 | _6.56: dataFactoryUtility_<br>Extract-Upload C7323617.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.57: dataFactoryUtility_<br>Extract-Upload C518005710._MobileMessageTracking into S3 | - | _5.57: dataFactoryUtility_<br>Extract-Upload C7331078._MobileMessage into S3 | _6.57: dataFactoryUtility_<br>Extract-Upload C7323638.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.58: dataFactoryUtility_<br>Extract-Upload C518005710._PushTag into S3 | - | _5.58: dataFactoryUtility_<br>Extract-Upload C7331095._MobileMessage into S3 | _6.58: dataFactoryUtility_<br>Extract-Upload C7323638.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.59: dataFactoryUtility_<br>Extract-Upload C7276545._GeofenceDefinition into S3 | - | _5.59: dataFactoryUtility_<br>Extract-Upload C7331157._MobileMessage into S3 | _6.59: dataFactoryUtility_<br>Extract-Upload C7325199.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.60: dataFactoryUtility_<br>Extract-Upload C7276545._MobileAddress into S3 | - | _5.60: dataFactoryUtility_<br>Extract-Upload C7331160._MobileMessage into S3 | _6.60: dataFactoryUtility_<br>Extract-Upload C7325199.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.61: dataFactoryUtility_<br>Extract-Upload C7276545._MobileMessageTracking into S3 | - | _5.61: dataFactoryUtility_<br>Extract-Upload dbo.ABTestSend into S3 | _6.61: dataFactoryUtility_<br>Extract-Upload C7325200.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.62: dataFactoryUtility_<br>Extract-Upload C7276545._PushAddress into S3 | - | _5.62: dataFactoryUtility_<br>Extract-Upload dbo.ABTestSendJob into S3 | _6.62: dataFactoryUtility_<br>Extract-Upload C7325200.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.63: dataFactoryUtility_<br>Extract-Upload C7276545._PushMessageAudience into S3 | - | _5.63: dataFactoryUtility_<br>Extract-Upload dbo.CampaignAsset into S3 | _6.63: dataFactoryUtility_<br>Extract-Upload C7325808.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.64: dataFactoryUtility_<br>Extract-Upload C7276545._PushMessageTracking into S3 | - | _5.64: dataFactoryUtility_<br>Extract-Upload dbo.CampaignAssetType into S3 | _6.64: dataFactoryUtility_<br>Extract-Upload C7325808.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.65: dataFactoryUtility_<br>Extract-Upload C7276545._PushSubscriptionHistory into S3 | - | _5.65: dataFactoryUtility_<br>Extract-Upload dbo.CustomObject into S3 | _6.65: dataFactoryUtility_<br>Extract-Upload C7325809.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.66: dataFactoryUtility_<br>Extract-Upload C7276545._PushTag into S3 | - | _5.66: dataFactoryUtility_<br>Extract-Upload dbo.JobCampaignDefinition into S3 | _6.66: dataFactoryUtility_<br>Extract-Upload C7325809.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.67: dataFactoryUtility_<br>Extract-Upload C7295447._GeofenceDefinition into S3 | - | _5.67: dataFactoryUtility_<br>Extract-Upload dbo.Program into S3 | _6.67: dataFactoryUtility_<br>Extract-Upload C7327899.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.68: dataFactoryUtility_<br>Extract-Upload C7295447._MobileAddress into S3 | - | _5.68: dataFactoryUtility_<br>Extract-Upload dbo.SendGroup into S3 | _6.68: dataFactoryUtility_<br>Extract-Upload C7327899.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.69: dataFactoryUtility_<br>Extract-Upload C7295447._MobileMessageTracking into S3 | - | _5.69: dataFactoryUtility_<br>Extract-Upload dbo.SendJob into S3 | _6.69: dataFactoryUtility_<br>Extract-Upload C7329574.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.70: dataFactoryUtility_<br>Extract-Upload C7295447._PushAddress into S3 | - | _5.70: dataFactoryUtility_<br>Extract-Upload dbo.SimpleTag into S3 | _6.70: dataFactoryUtility_<br>Extract-Upload C7329574.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.71: dataFactoryUtility_<br>Extract-Upload C7295447._PushMessageAudience into S3 | - | _5.71: dataFactoryUtility_<br>Extract-Upload dbo.SimpleTagObject into S3 | _6.71: dataFactoryUtility_<br>Extract-Upload C7329594.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.72: dataFactoryUtility_<br>Extract-Upload C7295447._PushMessageTracking into S3 | - | _5.72: dataFactoryUtility_<br>Extract-Upload dbo.SimpleTagObjectType into S3 | _6.72: dataFactoryUtility_<br>Extract-Upload C7329594.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.73: dataFactoryUtility_<br>Extract-Upload C7295447._PushSubscriptionHistory into S3 | - | _5.73: dataFactoryUtility_<br>Extract-Upload dbo.SourceAddress into S3 | _6.73: dataFactoryUtility_<br>Extract-Upload C7329596.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.74: dataFactoryUtility_<br>Extract-Upload C7295447._PushTag into S3 | - | _5.74: dataFactoryUtility_<br>Extract-Upload dbo.tblJobs_Surveys into S3 | _6.74: dataFactoryUtility_<br>Extract-Upload C7329596.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.75: dataFactoryUtility_<br>Extract-Upload C7306157._GeofenceDefinition into S3 | - | _5.75: dataFactoryUtility_<br>Extract-Upload dbo.tblJobSubscriberBatch into S3 | _6.75: dataFactoryUtility_<br>Extract-Upload C7329790.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.76: dataFactoryUtility_<br>Extract-Upload C7306157._MobileAddress into S3 | - | _5.76: dataFactoryUtility_<br>Extract-Upload dbo.tblSurveyAnswers into S3 | _6.76: dataFactoryUtility_<br>Extract-Upload C7329790.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.77: dataFactoryUtility_<br>Extract-Upload C7306157._MobileMessageTracking into S3 | - | _5.77: dataFactoryUtility_<br>Extract-Upload dbo.TriggeredSendJob into S3 | _6.77: dataFactoryUtility_<br>Extract-Upload C7329791.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.78: dataFactoryUtility_<br>Extract-Upload C7306157._PushAddress into S3 | - | _5.78: dataFactoryUtility_<br>Extract-Upload InteractionStudio.Definition into S3 | _6.78: dataFactoryUtility_<br>Extract-Upload C7329791.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.79: dataFactoryUtility_<br>Extract-Upload C7306157._PushMessageAudience into S3 | - | - | _6.79: dataFactoryUtility_<br>Extract-Upload C7329792.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.80: dataFactoryUtility_<br>Extract-Upload C7306157._PushMessageTracking into S3 | - | - | _6.80: dataFactoryUtility_<br>Extract-Upload C7329792.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.81: dataFactoryUtility_<br>Extract-Upload C7306157._PushSubscriptionHistory into S3 | - | - | _6.81: dataFactoryUtility_<br>Extract-Upload C7329793.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.82: dataFactoryUtility_<br>Extract-Upload C7306157._PushTag into S3 | - | - | _6.82: dataFactoryUtility_<br>Extract-Upload C7329793.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.83: dataFactoryUtility_<br>Extract-Upload C7310690._GeofenceDefinition into S3 | - | - | _6.83: dataFactoryUtility_<br>Extract-Upload C7329795.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.84: dataFactoryUtility_<br>Extract-Upload C7310690._MobileAddress into S3 | - | - | _6.84: dataFactoryUtility_<br>Extract-Upload C7329795.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.85: dataFactoryUtility_<br>Extract-Upload C7310690._MobileMessageTracking into S3 | - | - | _6.85: dataFactoryUtility_<br>Extract-Upload C7329814.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.86: dataFactoryUtility_<br>Extract-Upload C7310690._PushAddress into S3 | - | - | _6.86: dataFactoryUtility_<br>Extract-Upload C7329814.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.87: dataFactoryUtility_<br>Extract-Upload C7310690._PushMessageAudience into S3 | - | - | _6.87: dataFactoryUtility_<br>Extract-Upload C7329868.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.88: dataFactoryUtility_<br>Extract-Upload C7310690._PushMessageTracking into S3 | - | - | _6.88: dataFactoryUtility_<br>Extract-Upload C7329868.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.89: dataFactoryUtility_<br>Extract-Upload C7310690._PushSubscriptionHistory into S3 | - | - | _6.89: dataFactoryUtility_<br>Extract-Upload C7330116.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.90: dataFactoryUtility_<br>Extract-Upload C7310690._PushTag into S3 | - | - | _6.90: dataFactoryUtility_<br>Extract-Upload C7330116.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.91: dataFactoryUtility_<br>Extract-Upload C7313494._GeofenceDefinition into S3 | - | - | _6.91: dataFactoryUtility_<br>Extract-Upload C7330118.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.92: dataFactoryUtility_<br>Extract-Upload C7313494._MobileAddress into S3 | - | - | _6.92: dataFactoryUtility_<br>Extract-Upload C7330118.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.93: dataFactoryUtility_<br>Extract-Upload C7313494._MobileMessageTracking into S3 | - | - | _6.93: dataFactoryUtility_<br>Extract-Upload C7330119.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.94: dataFactoryUtility_<br>Extract-Upload C7313494._PushAddress into S3 | - | - | _6.94: dataFactoryUtility_<br>Extract-Upload C7330119.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.95: dataFactoryUtility_<br>Extract-Upload C7313494._PushMessageAudience into S3 | - | - | _6.95: dataFactoryUtility_<br>Extract-Upload C7330120.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.96: dataFactoryUtility_<br>Extract-Upload C7313494._PushMessageTracking into S3 | - | - | _6.96: dataFactoryUtility_<br>Extract-Upload C7330120.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.97: dataFactoryUtility_<br>Extract-Upload C7313494._PushSubscriptionHistory into S3 | - | - | _6.97: dataFactoryUtility_<br>Extract-Upload C7330128.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.98: dataFactoryUtility_<br>Extract-Upload C7313494._PushTag into S3 | - | - | _6.98: dataFactoryUtility_<br>Extract-Upload C7330128.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.99: dataFactoryUtility_<br>Extract-Upload C7315205._GeofenceDefinition into S3 | - | - | _6.99: dataFactoryUtility_<br>Extract-Upload C7330183.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.100: dataFactoryUtility_<br>Extract-Upload C7315205._MobileAddress into S3 | - | - | _6.100: dataFactoryUtility_<br>Extract-Upload C7330183.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.101: dataFactoryUtility_<br>Extract-Upload C7315205._MobileMessageTracking into S3 | - | - | _6.101: dataFactoryUtility_<br>Extract-Upload C7330212.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.102: dataFactoryUtility_<br>Extract-Upload C7315205._PushAddress into S3 | - | - | _6.102: dataFactoryUtility_<br>Extract-Upload C7330212.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.103: dataFactoryUtility_<br>Extract-Upload C7315205._PushMessageAudience into S3 | - | - | _6.103: dataFactoryUtility_<br>Extract-Upload C7330214.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.104: dataFactoryUtility_<br>Extract-Upload C7315205._PushMessageTracking into S3 | - | - | _6.104: dataFactoryUtility_<br>Extract-Upload C7330214.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.105: dataFactoryUtility_<br>Extract-Upload C7315205._PushSubscriptionHistory into S3 | - | - | _6.105: dataFactoryUtility_<br>Extract-Upload C7330438.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.106: dataFactoryUtility_<br>Extract-Upload C7315205._PushTag into S3 | - | - | _6.106: dataFactoryUtility_<br>Extract-Upload C7330438.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.107: dataFactoryUtility_<br>Extract-Upload C7317524._GeofenceDefinition into S3 | - | - | _6.107: dataFactoryUtility_<br>Extract-Upload C7330439.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.108: dataFactoryUtility_<br>Extract-Upload C7317524._MobileAddress into S3 | - | - | _6.108: dataFactoryUtility_<br>Extract-Upload C7330439.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.109: dataFactoryUtility_<br>Extract-Upload C7317524._MobileMessageTracking into S3 | - | - | _6.109: dataFactoryUtility_<br>Extract-Upload C7330441.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.110: dataFactoryUtility_<br>Extract-Upload C7317524._PushAddress into S3 | - | - | _6.110: dataFactoryUtility_<br>Extract-Upload C7330441.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.111: dataFactoryUtility_<br>Extract-Upload C7317524._PushAddressExtension into S3 | - | - | _6.111: dataFactoryUtility_<br>Extract-Upload C7330990.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.112: dataFactoryUtility_<br>Extract-Upload C7317524._PushApplicationCache into S3 | - | - | _6.112: dataFactoryUtility_<br>Extract-Upload C7330990.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.113: dataFactoryUtility_<br>Extract-Upload C7317524._PushDeviceLookup into S3 | - | - | _6.113: dataFactoryUtility_<br>Extract-Upload C7331078.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.114: dataFactoryUtility_<br>Extract-Upload C7317524._PushDeviceStatistics into S3 | - | - | _6.114: dataFactoryUtility_<br>Extract-Upload C7331078.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.115: dataFactoryUtility_<br>Extract-Upload C7317524._PushInAppStatisticsActivityAggregate into S3 | - | - | _6.115: dataFactoryUtility_<br>Extract-Upload C7331095.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.116: dataFactoryUtility_<br>Extract-Upload C7317524._PushMessage into S3 | - | - | _6.116: dataFactoryUtility_<br>Extract-Upload C7331095.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.117: dataFactoryUtility_<br>Extract-Upload C7317524._PushMessageAudience into S3 | - | - | _6.117: dataFactoryUtility_<br>Extract-Upload C7331157.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.118: dataFactoryUtility_<br>Extract-Upload C7317524._PushMessageInApp into S3 | - | - | _6.118: dataFactoryUtility_<br>Extract-Upload C7331157.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.119: dataFactoryUtility_<br>Extract-Upload C7317524._PushMessageTracking into S3 | - | - | _6.119: dataFactoryUtility_<br>Extract-Upload C7331160.SmsMemberSharedShortCode_Config into S3 | - | - | - |
| - | - | _3.120: dataFactoryUtility_<br>Extract-Upload C7317524._PushSubscriptionHistory into S3 | - | - | _6.120: dataFactoryUtility_<br>Extract-Upload C7331160.SmsMemberShortCodeDistinct into S3 | - | - | - |
| - | - | _3.121: dataFactoryUtility_<br>Extract-Upload C7317524._PushTag into S3 | - | - | _6.121: dataFactoryUtility_<br>Extract-Upload dbo.ABTestSendContent into S3 | - | - | - |
| - | - | _3.122: dataFactoryUtility_<br>Extract-Upload C7322086._GeofenceDefinition into S3 | - | - | _6.122: dataFactoryUtility_<br>Extract-Upload dbo.ABTestSendType into S3 | - | - | - |
| - | - | _3.123: dataFactoryUtility_<br>Extract-Upload C7322086._MobileAddress into S3 | - | - | _6.123: dataFactoryUtility_<br>Extract-Upload dbo.CampaignDefinition into S3 | - | - | - |
| - | - | _3.124: dataFactoryUtility_<br>Extract-Upload C7322086._MobileMessageTracking into S3 | - | - | _6.124: dataFactoryUtility_<br>Extract-Upload dbo.ImpressionRegion into S3 | - | - | - |
| - | - | _3.125: dataFactoryUtility_<br>Extract-Upload C7322086._PushAddress into S3 | - | - | _6.125: dataFactoryUtility_<br>Extract-Upload dbo.JobImpressionRegion into S3 | - | - | - |
| - | - | _3.126: dataFactoryUtility_<br>Extract-Upload C7322086._PushMessageAudience into S3 | - | - | _6.126: dataFactoryUtility_<br>Extract-Upload dbo.Members_ into S3 | - | - | - |
| - | - | _3.127: dataFactoryUtility_<br>Extract-Upload C7322086._PushMessageTracking into S3 | - | - | _6.127: dataFactoryUtility_<br>Extract-Upload dbo.SendSplit into S3 | - | - | - |
| - | - | _3.128: dataFactoryUtility_<br>Extract-Upload C7322086._PushSubscriptionHistory into S3 | - | - | _6.128: dataFactoryUtility_<br>Extract-Upload dbo.Subscriber into S3 | - | - | - |
| - | - | _3.129: dataFactoryUtility_<br>Extract-Upload C7322086._PushTag into S3 | - | - | _6.129: dataFactoryUtility_<br>Extract-Upload dbo.tblJobs into S3 | - | - | - |
| - | - | _3.130: dataFactoryUtility_<br>Extract-Upload C7323617._GeofenceDefinition into S3 | - | - | _6.130: dataFactoryUtility_<br>Extract-Upload dbo.tblJobs_Lists into S3 | - | - | - |
| - | - | _3.131: dataFactoryUtility_<br>Extract-Upload C7323617._MobileAddress into S3 | - | - | _6.131: dataFactoryUtility_<br>Extract-Upload dbo.tblJobs_URLs into S3 | - | - | - |
| - | - | _3.132: dataFactoryUtility_<br>Extract-Upload C7323617._MobileMessageTracking into S3 | - | - | _6.132: dataFactoryUtility_<br>Extract-Upload dbo.tblSurveyQuestions into S3 | - | - | - |
| - | - | _3.133: dataFactoryUtility_<br>Extract-Upload C7323617._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.134: dataFactoryUtility_<br>Extract-Upload C7323617._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.135: dataFactoryUtility_<br>Extract-Upload C7323617._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.136: dataFactoryUtility_<br>Extract-Upload C7323617._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.137: dataFactoryUtility_<br>Extract-Upload C7323617._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.138: dataFactoryUtility_<br>Extract-Upload C7323638._GeofenceDefinition into S3 | - | - | - | - | - | - |
| - | - | _3.139: dataFactoryUtility_<br>Extract-Upload C7323638._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.140: dataFactoryUtility_<br>Extract-Upload C7323638._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.141: dataFactoryUtility_<br>Extract-Upload C7323638._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.142: dataFactoryUtility_<br>Extract-Upload C7323638._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.143: dataFactoryUtility_<br>Extract-Upload C7323638._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.144: dataFactoryUtility_<br>Extract-Upload C7323638._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.145: dataFactoryUtility_<br>Extract-Upload C7323638._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.146: dataFactoryUtility_<br>Extract-Upload C7325199._GeofenceDefinition into S3 | - | - | - | - | - | - |
| - | - | _3.147: dataFactoryUtility_<br>Extract-Upload C7325199._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.148: dataFactoryUtility_<br>Extract-Upload C7325199._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.149: dataFactoryUtility_<br>Extract-Upload C7325199._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.150: dataFactoryUtility_<br>Extract-Upload C7325199._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.151: dataFactoryUtility_<br>Extract-Upload C7325199._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.152: dataFactoryUtility_<br>Extract-Upload C7325199._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.153: dataFactoryUtility_<br>Extract-Upload C7325199._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.154: dataFactoryUtility_<br>Extract-Upload C7325200._GeofenceDefinition into S3 | - | - | - | - | - | - |
| - | - | _3.155: dataFactoryUtility_<br>Extract-Upload C7325200._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.156: dataFactoryUtility_<br>Extract-Upload C7325200._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.157: dataFactoryUtility_<br>Extract-Upload C7325200._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.158: dataFactoryUtility_<br>Extract-Upload C7325200._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.159: dataFactoryUtility_<br>Extract-Upload C7325200._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.160: dataFactoryUtility_<br>Extract-Upload C7325200._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.161: dataFactoryUtility_<br>Extract-Upload C7325200._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.162: dataFactoryUtility_<br>Extract-Upload C7325808._GeofenceDefinition into S3 | - | - | - | - | - | - |
| - | - | _3.163: dataFactoryUtility_<br>Extract-Upload C7325808._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.164: dataFactoryUtility_<br>Extract-Upload C7325808._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.165: dataFactoryUtility_<br>Extract-Upload C7325808._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.166: dataFactoryUtility_<br>Extract-Upload C7325808._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.167: dataFactoryUtility_<br>Extract-Upload C7325808._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.168: dataFactoryUtility_<br>Extract-Upload C7325808._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.169: dataFactoryUtility_<br>Extract-Upload C7325808._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.170: dataFactoryUtility_<br>Extract-Upload C7325809._GeofenceDefinition into S3 | - | - | - | - | - | - |
| - | - | _3.171: dataFactoryUtility_<br>Extract-Upload C7325809._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.172: dataFactoryUtility_<br>Extract-Upload C7325809._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.173: dataFactoryUtility_<br>Extract-Upload C7325809._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.174: dataFactoryUtility_<br>Extract-Upload C7325809._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.175: dataFactoryUtility_<br>Extract-Upload C7325809._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.176: dataFactoryUtility_<br>Extract-Upload C7325809._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.177: dataFactoryUtility_<br>Extract-Upload C7325809._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.178: dataFactoryUtility_<br>Extract-Upload C7327899._GeofenceDefinition into S3 | - | - | - | - | - | - |
| - | - | _3.179: dataFactoryUtility_<br>Extract-Upload C7327899._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.180: dataFactoryUtility_<br>Extract-Upload C7327899._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.181: dataFactoryUtility_<br>Extract-Upload C7327899._PushAddress into S3 | - | - | - | - | - | - |
| - | - | _3.182: dataFactoryUtility_<br>Extract-Upload C7327899._PushMessageAudience into S3 | - | - | - | - | - | - |
| - | - | _3.183: dataFactoryUtility_<br>Extract-Upload C7327899._PushMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.184: dataFactoryUtility_<br>Extract-Upload C7327899._PushSubscriptionHistory into S3 | - | - | - | - | - | - |
| - | - | _3.185: dataFactoryUtility_<br>Extract-Upload C7327899._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.186: dataFactoryUtility_<br>Extract-Upload C7329574._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.187: dataFactoryUtility_<br>Extract-Upload C7329574._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.188: dataFactoryUtility_<br>Extract-Upload C7329574._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.189: dataFactoryUtility_<br>Extract-Upload C7329594._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.190: dataFactoryUtility_<br>Extract-Upload C7329594._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.191: dataFactoryUtility_<br>Extract-Upload C7329594._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.192: dataFactoryUtility_<br>Extract-Upload C7329596._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.193: dataFactoryUtility_<br>Extract-Upload C7329596._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.194: dataFactoryUtility_<br>Extract-Upload C7329596._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.195: dataFactoryUtility_<br>Extract-Upload C7329790._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.196: dataFactoryUtility_<br>Extract-Upload C7329790._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.197: dataFactoryUtility_<br>Extract-Upload C7329790._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.198: dataFactoryUtility_<br>Extract-Upload C7329791._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.199: dataFactoryUtility_<br>Extract-Upload C7329791._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.200: dataFactoryUtility_<br>Extract-Upload C7329791._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.201: dataFactoryUtility_<br>Extract-Upload C7329792._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.202: dataFactoryUtility_<br>Extract-Upload C7329792._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.203: dataFactoryUtility_<br>Extract-Upload C7329792._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.204: dataFactoryUtility_<br>Extract-Upload C7329793._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.205: dataFactoryUtility_<br>Extract-Upload C7329793._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.206: dataFactoryUtility_<br>Extract-Upload C7329793._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.207: dataFactoryUtility_<br>Extract-Upload C7329795._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.208: dataFactoryUtility_<br>Extract-Upload C7329795._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.209: dataFactoryUtility_<br>Extract-Upload C7329795._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.210: dataFactoryUtility_<br>Extract-Upload C7329814._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.211: dataFactoryUtility_<br>Extract-Upload C7329814._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.212: dataFactoryUtility_<br>Extract-Upload C7329814._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.213: dataFactoryUtility_<br>Extract-Upload C7329868._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.214: dataFactoryUtility_<br>Extract-Upload C7329868._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.215: dataFactoryUtility_<br>Extract-Upload C7329868._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.216: dataFactoryUtility_<br>Extract-Upload C7330116._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.217: dataFactoryUtility_<br>Extract-Upload C7330116._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.218: dataFactoryUtility_<br>Extract-Upload C7330116._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.219: dataFactoryUtility_<br>Extract-Upload C7330118._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.220: dataFactoryUtility_<br>Extract-Upload C7330118._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.221: dataFactoryUtility_<br>Extract-Upload C7330118._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.222: dataFactoryUtility_<br>Extract-Upload C7330119._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.223: dataFactoryUtility_<br>Extract-Upload C7330119._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.224: dataFactoryUtility_<br>Extract-Upload C7330119._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.225: dataFactoryUtility_<br>Extract-Upload C7330120._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.226: dataFactoryUtility_<br>Extract-Upload C7330120._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.227: dataFactoryUtility_<br>Extract-Upload C7330120._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.228: dataFactoryUtility_<br>Extract-Upload C7330128._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.229: dataFactoryUtility_<br>Extract-Upload C7330128._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.230: dataFactoryUtility_<br>Extract-Upload C7330128._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.231: dataFactoryUtility_<br>Extract-Upload C7330183._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.232: dataFactoryUtility_<br>Extract-Upload C7330183._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.233: dataFactoryUtility_<br>Extract-Upload C7330183._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.234: dataFactoryUtility_<br>Extract-Upload C7330212._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.235: dataFactoryUtility_<br>Extract-Upload C7330212._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.236: dataFactoryUtility_<br>Extract-Upload C7330212._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.237: dataFactoryUtility_<br>Extract-Upload C7330214._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.238: dataFactoryUtility_<br>Extract-Upload C7330214._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.239: dataFactoryUtility_<br>Extract-Upload C7330214._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.240: dataFactoryUtility_<br>Extract-Upload C7330438._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.241: dataFactoryUtility_<br>Extract-Upload C7330438._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.242: dataFactoryUtility_<br>Extract-Upload C7330438._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.243: dataFactoryUtility_<br>Extract-Upload C7330439._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.244: dataFactoryUtility_<br>Extract-Upload C7330439._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.245: dataFactoryUtility_<br>Extract-Upload C7330439._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.246: dataFactoryUtility_<br>Extract-Upload C7330441._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.247: dataFactoryUtility_<br>Extract-Upload C7330441._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.248: dataFactoryUtility_<br>Extract-Upload C7330441._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.249: dataFactoryUtility_<br>Extract-Upload C7330990._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.250: dataFactoryUtility_<br>Extract-Upload C7330990._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.251: dataFactoryUtility_<br>Extract-Upload C7330990._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.252: dataFactoryUtility_<br>Extract-Upload C7331078._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.253: dataFactoryUtility_<br>Extract-Upload C7331078._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.254: dataFactoryUtility_<br>Extract-Upload C7331078._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.255: dataFactoryUtility_<br>Extract-Upload C7331095._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.256: dataFactoryUtility_<br>Extract-Upload C7331095._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.257: dataFactoryUtility_<br>Extract-Upload C7331095._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.258: dataFactoryUtility_<br>Extract-Upload C7331157._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.259: dataFactoryUtility_<br>Extract-Upload C7331157._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.260: dataFactoryUtility_<br>Extract-Upload C7331157._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.261: dataFactoryUtility_<br>Extract-Upload C7331160._MobileAddress into S3 | - | - | - | - | - | - |
| - | - | _3.262: dataFactoryUtility_<br>Extract-Upload C7331160._MobileMessageTracking into S3 | - | - | - | - | - | - |
| - | - | _3.263: dataFactoryUtility_<br>Extract-Upload C7331160._PushTag into S3 | - | - | - | - | - | - |
| - | - | _3.264: dataFactoryUtility_<br>Extract-Upload dbo.Asset into S3 | - | - | - | - | - | - |
| - | - | _3.265: dataFactoryUtility_<br>Extract-Upload dbo.PushApplicationConfig into S3 | - | - | - | - | - | - |
