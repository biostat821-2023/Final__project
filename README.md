# Final Project Plan

## Goal
The aim of this project is to gather clinical information from users specifically on breast cancer. To retrieve the necessary input names, we have utilized datasets from cBioportal that contain both general and cancer-specific information. Each dataset comprises several columns such as patient ID, Sample ID, Cancer Type, Cancer Type Detail, Number of Samples per Patient, Mutation Count, Fraction Genome Altered, Sample Type, Sex, Disease Free (Months), Disease Free Event, ER PCT Primary, ER Status of Sequenced Sample, ER Status of the Primary, HER2 FISH Ratio Primary, HER2 FISH Ratio Value of Sequenced Sample, HER2 FISH Status (Report and ASCO) of Primary, HER2 FISH Status of Sequenced Sample, HER2 IHC Score of Sequenced Sample, HER2 IHC Score Primary, HER2 IHC Status of Sequenced Sample, and HER2 IHC Status Primary.


## Implementation
To achieve our objectives, we plan to develop a Python script and convert it into an API that will prompt users to provide breast cancer-related information. Subsequently, we will store the collected data in a build-up database. For this project, we will use some existing breast cancer datasets to mock a database. Furthermore, we will create analysis functions that will offer essential yet straightforward breast cancer analysis and present the results to users through the API. Finally, we will containerize all our work.

![Untitled drawing](https://user-images.githubusercontent.com/70648104/230992080-781d7835-48cb-4170-bd17-e628a2373beb.jpg)

To develop a Python script that will prompt users to provide breast cancer-related information, we will use Python's built-in libraries such as input() and argparse. Input() function will allow us to get user inputs while argparse will help us to parse the user inputs and validate them. Once we receive the user inputs, we will use Python's requests library to convert them into API calls, which we will then store in a database.

To store the collected data, we will build a database using an existing breast cancer dataset as a mock database. For this project, we may use a popular SQL-based database such as MySQL or PostgreSQL. These databases offer features such as robust querying capabilities, ACID compliance, and scalability, which are necessary for storing and managing large amounts of data.

After storing the data, we will create analysis functions that will perform essential yet straightforward breast cancer analysis. The analysis functions may include statistical analysis of different breast cancer-related factors such as ER/PR/HER2 status, mutation count, and fraction genome altered. To perform these analyses, we may use Python's scientific libraries such as NumPy and Pandas, which offer powerful data manipulation and analysis capabilities.

Finally, to ensure that our work is portable and easily deployable, we will containerize all our work. Containerization involves packaging our Python script, database, and other dependencies into a single container that can be run on any machine that supports the containerization platform. For this project, we may use Docker, a popular containerization platform that offers features such as isolation, reproducibility, and easy deployment. Containerizing our work will also make it easier to scale our project in the future.
