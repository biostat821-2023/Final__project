# Final Project Plan

## Goal
The aim of this project is to gather clinical information from users specifically on breast cancer. To retrieve the necessary input names, we have utilized datasets from cBioportal that contain both general and cancer-specific information. Each dataset comprises several columns such as patient ID, Sample ID, Cancer Type, Cancer Type Detail, Number of Samples per Patient, Mutation Count, Fraction Genome Altered, Sample Type, Sex, Disease Free (Months), Disease Free Event, ER PCT Primary, ER Status of Sequenced Sample, ER Status of the Primary, HER2 FISH Ratio Primary, HER2 FISH Ratio Value of Sequenced Sample, HER2 FISH Status (Report and ASCO) of Primary, HER2 FISH Status of Sequenced Sample, HER2 IHC Score of Sequenced Sample, HER2 IHC Score Primary, HER2 IHC Status of Sequenced Sample, and HER2 IHC Status Primary.


## Implementation
To achieve our objectives, we plan to develop a Python script and convert it into an API that will prompt users to provide breast cancer-related information. Subsequently, we will store the collected data in a build-up database. For this project, we will use some existing breast cancer datasets to mock a database. Furthermore, we will create analysis functions that will offer essential yet straightforward breast cancer analysis and present the results to users through the API. Finally, we will containerize all our work.

![Untitled drawing](https://user-images.githubusercontent.com/70648104/230992080-781d7835-48cb-4170-bd17-e628a2373beb.jpg)
