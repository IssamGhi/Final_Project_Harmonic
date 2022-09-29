# Project: METELYK

![logo_Project-removebg-preview (2)](https://user-images.githubusercontent.com/113267690/192277183-84bd6d62-3fad-40f5-b59c-4188628bc3ed.png)


## Purpose of Project
Project Metelyk has been created to bring solution for the problematic: 
(./Initial_docs/Sujet_Projet_POEI_PythonHarmonic-_anglais.pdf)


### Summary
Metelyk is a radically simple WEB based application on software task management system. It handles user login system, issue tracking and ... 

### Design Principles : 

1. Create environment: Docker, REST API, FLASK, Ansible

2. Develop the functionality of:
    -  Registration and login  : 
        + login for dev 
        + login for admin( should be created automatically at the first start of the application)
    -  Features of the administrator  :
        + can add features to dev(a name, a description, the signature of the expected function and a test file developed in pytest)
        + can access the list of registered features.
        + can access list of developers who have sent a response and response with a ranking by test coverage rate

3. Features of developers:
    - dev can access the list of features to be developed(name, signature, description)
    - dev can submit his code as a Python script ( dll in C optionally)
    - The submission response must contain the link to access the feature test result
    - If the test coverage is not total, the developer can submit a new response.


# Environment Requirements:
Python, Postgresql, Docker, Ansible, Flask Rest Api

# Software Environment Requirements
Please check file requirements.txt

# Developer Team: Metelyk

In alphathequic order: 
- Dilek : https://github.com/ArnholdD 
- Hamdi : https://github.com/Hamdidab 
- Inga : https://github.com/IngaYa
- Issam : https://github.com/IssamGhi 

In case of a question, please contact us...
