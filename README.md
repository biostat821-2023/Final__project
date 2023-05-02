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

![Schema](https://user-images.githubusercontent.com/112578023/235781006-d2ecdce1-3dd0-4ede-8285-91097d157b7e.png)

--------------------------------------------------------------

## For End-Users
To use our breast cancer information input and analysis service, please follow the instructions below:

1. Install Dependencies
Before using our service, make sure you have the necessary dependencies installed. Navigate to the project directory and run the following command to install all dependencies: pip install -r requirements.txt

2. Enter Patient Information
To enter patient demographic and clinical data, run the following command in the project directory:

3. Analyze Data
To analyze the data, run the following command in the project directory: 'python analysis.py'

## For Contributors

For contributors, we welcome anyone who is interested in contributing to our project. Here are some ways you can get involved:

Code contributions: If you have experience in Python and/or SQL, you can contribute by adding new features, improving existing code, or fixing bugs. We have a GitHub repository where you can find the project code and documentation. Simply fork the repository, make your changes, and submit a pull request for review.

Testing and bug reporting: Even if you're not comfortable with coding, you can still contribute by testing the application and reporting any bugs you find. This will help us improve the quality of our code and make the application more reliable.

Documentation: We always welcome contributions to our documentation. If you have experience in technical writing or just want to help improve our documentation, you can contribute by updating our documentation, fixing errors, or adding new sections.

Feedback: We are always looking for feedback on our project. If you have any suggestions or ideas on how we can improve our application, please let us know.

If you have any questions, feel free to reach out to us on GitHub or via email. We look forward to your contributions!


