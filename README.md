# Final Project

## Goal
The aim of this project is to gather clinical information from users specifically on breast cancer. To retrieve the necessary input names, we have utilized datasets from cBioportal that contain both general and cancer-specific information. Each dataset comprises several columns such as Patient ID, Sample ID, Collection Date, Cancer Type, Mutation Count, Chemotherapy, Cytolytic Activity Score, Patient's name, Gender, Date of Birth, Phone, and E-mail.


## Implementation
To achieve our objectives, we plan to develop a Python script and convert it into an API that will prompt users to provide breast cancer-related information. Subsequently, we will store the collected data in a build-up database. For this project, we will use some existing breast cancer datasets to mock a database. Furthermore, we will create analysis functions that will offer essential yet straightforward breast cancer analysis and present the results to users through the API. Finally, we will containerize all our work.

1. Data Input Service
- (1) Enter the patient's demographic data and clinical data through a series of prompts. 
- (2) Use SQLite and store the data into local database

2. Analytical Service
- (1) Use Pandas and Numpy to do data analysis
- (2) Use Dash to visualize the output

3. Containerization and CI
- (1) Use Docker to contianerize the application
- (2) Build automated checks for the dependencies, format, tests when pushing new codes using Github Actions

![Untitled drawing](https://user-images.githubusercontent.com/70648104/230992080-781d7835-48cb-4170-bd17-e628a2373beb.jpg)
