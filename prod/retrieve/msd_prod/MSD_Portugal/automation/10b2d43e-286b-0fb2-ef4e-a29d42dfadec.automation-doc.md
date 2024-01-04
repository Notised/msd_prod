## 10b2d43e-286b-0fb2-ef4e-a29d42dfadec

**Name** (not equal to External Key)**:** Automatismo_Exclusão_Campanhas_Globais

**Description:** n/a

**Folder:** my automations/Automatismo_Exclusao_Global/

**Started by:** Schedule

**Status:** Scheduled

**Schedule:**

* Start: 2022-11-24 09:00:00 +00:00
* End: 2079-06-06 00:00:00 +00:00
* Timezone: GMT Standard Time
* Recurrance: every day until end date

**Notifications:** _none_


| Step 1<br>_<small>Envios por subscriber e critério de 5 envios</small>_ | Step 2<br>_<small>Não interacção</small>_ | Step 3<br>_<small>Supression_Global+Condicoes para Supression das Àreas</small>_ | Step 4<br>_<small>Listas Supression por área</small>_ | Step 5<br>_<small>Listas Supression por área+Admin</small>_ | Step 6<br>_<small>Target_ALL</small>_ | Step 7<br>_<small>Listas Supression por área+TARGETALL</small>_ | Step 8<br>_<small>Listas Supression por área+TARGETALL+ADMIN</small>_ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| _1.1: query_<br>N_Envios | _2.1: query_<br>NOT_OPEN_GLOBAL | _3.1: query_<br>Supression_List_Global | _4.1: query_<br>Supression_Area_Medical | _5.1: query_<br>Supression_Area_Medical_Admin | _6.1: query_<br>TARGET_ALL | _7.1: query_<br>Supression_Area_Medical+TargetALL | _8.1: query_<br>Supression_Area_Medical+TargetALL+ADMIN |
| _1.2: query_<br>N_ENVIOS_Filtro_5_ou_Mais | - | _3.2: query_<br>Global_SP_EmailName | _4.2: query_<br>Supression_Immunology | _5.2: query_<br>Supression_Area_Immunology_Admin | - | _7.2: query_<br>Supression_Immunology+TargetALL | _8.2: query_<br>Supression_Area_Immunology_Admin+TargetAll |
| - | - | _3.3: query_<br>Exclusion_Medical | _4.3: query_<br>Supression_Area_HIV | _5.3: query_<br>Supression_Area_Oncology-Lung_Admin | - | _7.3: query_<br>Supression_Area_HIV+targetALL | _8.3: query_<br>Supression_Area_Oncology-Lung_Admin+TargetAll |
| - | - | - | _4.4: query_<br>Supression_Area_Antibiotics_Antifungals | _5.4: query_<br>Supression_Area_Oncology-Melanoma_Admin | - | _7.4: query_<br>Supression_Area_Antibiotics_Antifungals+TargetAll | _8.4: query_<br>Supression_Area_Oncology-Melanoma_Admin+TargetAll |
| - | - | - | _4.5: query_<br>Supression_Area_Anesthesia | _5.5: query_<br>Supression_Area_MSD_Geral_Admin | - | _7.5: query_<br>Supression_Area_Anesthesia+TargetAll | _8.5: query_<br>Supression_Area_MSD_Geral_Admin_Target |
| - | - | - | _4.6: query_<br>Supression_Oncology_All | _5.6: query_<br>Supression_Area_Oncology_Breast_Admin | - | _7.6: query_<br>Supression_Oncology_All+TargetAll | _8.6: query_<br>Supression_Area_Oncology_Breast_Admin+TargetAll |
| - | - | - | _4.7: query_<br>Supression_Area_Pulmonary-Hypertension | _5.7: query_<br>Supression_Area_Oncology-Head&Neck_Admin | - | _7.7: query_<br>Supression_Area_Pulmonary-Hypertension+TargetAll | _8.7: query_<br>Supression_Area_Oncology-Head&Neck_Admin+targetALL |
| - | - | - | _4.8: query_<br>Supression_Area_Vacinas | _5.8: query_<br>Supression_Area_Oncology_ALL_Admin | - | _7.8: query_<br>Supression_Area_Vacinas+targetAll | _8.8: query_<br>Supression_Area_Oncology_ALL_Admin+TargetAll |
| - | - | - | _4.9: query_<br>Supression_Area_MSD_Geral | _5.9: query_<br>Supression_Area_Oncology_Kidney_or_Bladder_Admin | - | _7.9: query_<br>Supression_Area_MSD_Geral+TargetAll | _8.9: query_<br>Supression_Area_Oncology_Kidney_or_Bladder_Admin+TargetAll |
| - | - | - | _4.10: query_<br>Supression_Area_Oncology-Lung | _5.10: query_<br>Supression_Area_Diabetes_and_COVID_Admin | - | _7.10: query_<br>Supression_Area_Oncology-Lung+TargetAll | _8.10: query_<br>Supression_Area_Diabetes_and_COVID_Admin+TargetAll |
| - | - | - | _4.11: query_<br>Supression_Area_Oncology-Head&Neck | _5.11: query_<br>Supression_Area_Oncology_Prostate_or_Ovarian_Admin | - | _7.11: query_<br>Supression_Area_Oncology-Head&Neck+targetAll | _8.11: query_<br>Supression_Area_Oncology_Prostate_or_Ovarian_Admin+TargetAll |
| - | - | - | _4.12: query_<br>Supression_Area_Oncology-Prostate_Ovarian | _5.12: query_<br>Supression_Area_Vacinas_Admin | - | _7.12: query_<br>Supression_Area_Oncology-Prostate_Ovarian+TargetAll | _8.12: query_<br>Supression_Area_Vacinas_Admin+TargetAll |
| - | - | - | _4.13: query_<br>Supression_Area_Diabetes&COVID | _5.13: query_<br>Supression_Area_Anesthesia_Admin | - | _7.13: query_<br>Supression_Area_Diabetes&COVID+TargetAll | _8.13: query_<br>Supression_Area_Anesthesia_Admin_Target |
| - | - | - | _4.14: query_<br>Supression_Area_Oncology-Kidney_Bladder | _5.14: query_<br>Supression_Area_HIV_Admin | - | _7.14: query_<br>Supression_Area_Oncology-Kidney_Bladder+TargetAll | _8.14: query_<br>Supression_Area_HIV_Admin+TargetAll |
| - | - | - | _4.15: query_<br>Supression_Area_Oncology-Breast | _5.15: query_<br>Supression_Area_Antibiotics_Antifungals_Admin | - | _7.15: query_<br>Supression_Area_Oncology-Breast+TargetAll | _8.15: query_<br>Supression_Area_Antibiotics_Antifungals_Admin_TargetALL |
| - | - | - | _4.16: query_<br>Supression_Area_Oncology-Melanoma | _5.16: query_<br>Supression_Area_Pulmonary-Hypertension_Admin | - | _7.16: query_<br>Supression_Area_Oncology-Melanoma+targetAll | _8.16: query_<br>Supression_Area_Pulmonary-Hypertension_Admin+TargetALL |
