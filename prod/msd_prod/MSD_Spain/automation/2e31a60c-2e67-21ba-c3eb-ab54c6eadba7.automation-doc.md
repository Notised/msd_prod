## 2e31a60c-2e67-21ba-c3eb-ab54c6eadba7

**Name** (not equal to External Key)**:** Automated_DE_creatorLauraF

**Description:** Daily refresh for DE

**Folder:** my automations/2.Business/Tests/Laura/

**Started by:** Schedule

**Status:** PausedSchedule

**Schedule:**

* Start: 2023-09-20 08:00:00 +01:00
* End: 2079-06-06 00:00:00 +01:00
* Timezone: Romance Standard Time
* Recurrance: every day until end date

**Notifications:**

* Complete: laura.fernandez1@merck.com
* Error: laura.fernandez1@merck.com

| Step 1<br>_<small>INMUNO RHU y GE Target y No Target</small>_ | Step 2<br>_<small>-</small>_ | Step 3<br>_<small>-</small>_ | Step 4<br>_<small>HPTEC C y PUL Target y No Target</small>_ | Step 5<br>_<small>AE Go Ahead recibido<br></small>_ | Step 6<br>_<small>-</small>_ | Step 7<br>_<small>-</small>_ | Step 8<br>_<small>-</small>_ | Step 9<br>_<small>-</small>_ | Step 10<br>_<small>-</small>_ | Step 11<br>_<small>-</small>_ | Step 12<br>_<small>-</small>_ | Step 13<br>_<small>-</small>_ | Step 14<br>_<small>-</small>_ | Step 15<br>_<small>-</small>_ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| _1.1: query_<br>QRY_C_HIP_Target | _2.1: query_<br>QRY_ID_IM_ECM_FFVV_AAS_Target | _3.1: query_<br>QRY_Usuarios_visitados_INM_CurrentMonth | _4.1: query_<br>QRY_MED_EMP_C_PUL_All | _5.1: query_<br>QRY_usuarios_ae_recibido_goahead | _6.1: query_<br>QRY_Prueba_Datos_AE_3_0 | _7.1: query_<br>L1_test_indicator_QRY | _8.1: query_<br>QRY_Usuarios_Sent_NL_Pulmon_20230926 | _9.1: query_<br>QRY_usuarios_L1_coincidan_GR_pulmon | _10.1: query_<br>L1_grading_pulmon_DE | _11.1: query_<br>QRY_Target_Extended_INM | _12.1: query_<br>QRY_TargetExtendend_INM | _13.1: query_<br>QRY_Grading_ON_Cabeza_y_cuello | _14.1: query_<br>QRY_grading_ON_pulmon | _15.1: query_<br>QRY_HIP_C_PUL_NoTarget_Delegada |
| _1.2: query_<br>QRY_gastro_notarget_INM | _2.2: query_<br>QRY_ID_IM_ECM_FFVV_AAS_NoTarget | - | _4.2: query_<br>QRY_C_Target | _5.2: query_<br>QRY_AE_GoAHEAD | _6.2: query_<br>QRY_Prueba_Master_AE | - | - | - | - | - | - | _13.2: query_<br>QRY_CC_NoTarget | - | - |
| _1.3: query_<br>QRY_RHU_Target_INM | - | - | _4.3: query_<br>QRY_C_No_Target | - | - | - | - | - | - | - | - | - | - | - |
| _1.4: query_<br>QRY_GE_Target | - | - | _4.4: query_<br>QRY_PUL_Target | - | - | - | - | - | - | - | - | - | - | - |
| - | - | - | _4.5: query_<br>QRY_PUL_No_Target | - | - | - | - | - | - | - | - | - | - | - |
