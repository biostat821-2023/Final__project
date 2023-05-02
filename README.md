# Final Project

## Goal
The aim of this project is to provide flexibility to allow users to provide demographic and clinicial information specifically on breast cancer. To retrieve the necessary input names, we have utilized datasets from [cBioportal](https://www.cbioportal.org/study/clinicalData?id=brca_smc_2018) that contain both general and cancer-specific information. The Patient table in the database comprises columns of `Patient ID`, `Patient name`, `Gender`, `Date of Birth`, `Age`, `Phone`, and `E-mail`. The Sample table in the database comprises columns of `Patient ID`, `Sample ID`, `Collection Date`, `Cancer Type`, `Mutation Count`, `Chemotherapy`, `Cytolytic Activity Score`.


## Implementation
To achieve our objectives, we plan to develop a Python script and build a library interface which will prompt users to provide breast cancer-related information. Subsequently, we will store the collected data in a build-up database. For this project, we will use some existing breast cancer datasets to mock a database and then create analysis functions that will offer essential yet straightforward breast cancer analysis and present the results to user. Finally, we also build up commandline tools to make the implementation and analysis more efficient.

### 1. Data Input Service

Users will be asked to fill in demographic information and clinical information which will connect to SQLite. 

We have two classes and each class has three functions 
- (1) Enter the patient's demographic data and clinical data through a series of prompts. 
- (2) Use SQLite and store the data into local database

### 2. Analytical Service

We intend to grant users with great flexibility, therefore in the analysis section, we first ask users which database they want to connect to and check if the database exists. We ask until we have a valid input and users can also choose to exit the program. We then ask the users to choose which analysis they want to perform. 

Specifically for this project, we conduct analysis on global information of the dataset, which includes: 
- Number of unique patients
- Number of unique cancer types
- Number of samples in each cancer type
- Age distribution (including visualization) 
We also intend to analyze information specifically to a patient, which includes: 
- Number of samples for each patient
- Number of samples for each cancer type for patient

### 3. Containerization and CI
- (1) Use Docker to contianerize the application
- (2) Build automated checks for the dependencies, format, tests when pushing new codes using Github Actions

![Untitled drawing](https://user-images.githubusercontent.com/70648104/230992080-781d7835-48cb-4170-bd17-e628a2373beb.jpg)

--------------------------------------------------------------

## For End-Users


## For Contributors


