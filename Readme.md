# Django Based rest API to access files in Google Drive

## Description

The aim of the project is basically to build a backend system using API to access the google drive, and download/ingest csv files into the database. The API is build on Django REST Framework.

## Requirements

1. Python 3.9 or above and its packages mentioned in requirements.txt file.
2. Developer Account in google enabled with API's for Drive. The steps for that can be followed here (<https://support.google.com/googleapi/answer/6158841?hl=en>).
3. Any RDBMS, for this project I am using MSSQL Server.
4. API Testing tools like Postman, Thunderclient or others.

## Usage

The project has four API endpoints each endpoint with its own usage as shown below.

1. Endpoint to list all contents in a google drive.

    <http://127.0.0.1:8000/googledrive/>

    The output for this endpoint will be JSON with id and title fields for each content in Google Drive.

2. Endpoint to list files from a specific folder.

    <http://127.0.0.1:8000/googledrive/id/*******************************/>

    This Endpoint will take folder_id as a path parameter and list all files and other contents available into that folder.

3. Endpoint to download the required file and ingest into the database.

    <http://127.0.0.1:8000/googledrive/download/?id=***********************&table_name=fifa_data>

    This Endpoint will inputs id(file_id) and table_name as Query parameters, these two parameters are mandatory to call this endpont else an exception will be thrown via JSON.
    1. file_id specifies the file we are going to read.
    2. table_name specifies the destination table name into the database. If the table already exists into the database then the data can be either replaced or appended into database.

4. Endpoint to fetch the data from the database.

    <http://127.0.0.1:8000/fifadata/>

    For the enduser to fetch the data from the new created/updated table this endpoint can be used so that he can retrive the data via JSON. This can be further updated so that the user can select which table he wants to fetch the data from.

Note: The project is a sample demo project of a backend system, based on the requirement the changes and updates can be made.
