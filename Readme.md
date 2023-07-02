# Django Based rest API to access files in Google Drive

## Description
The aim of the project is basically to build a backend system using API to access the google drive, and download/ingest csv files into the database. The API is build on Django REST Framework.

## Requirements
1. Python 3.9 or above and its packages mentioned in requirements.txt file.
2. Developer Account in google enabled with API's for Drive. The steps for that can be followed here (https://support.google.com/googleapi/answer/6158841?hl=en).
3. Any RDBMS, for this project I am using MSSQL Server.
4. API Testing tools like Postman, Thunderclient or others.

## Usage
The project has four API endpoints each endpoint with its own usage as shown below.
1. Endpoint to list all contents in a google drive.

database
http://127.0.0.1:8000/fifadata/

List google drive
http://127.0.0.1:8000/googledrive/

List files from a folder
http://127.0.0.1:8000/googledrive/id/1sAUj7kzhxA7QMnej6DuHWdh1LGXT4WeS/

http://127.0.0.1:8000/googledrive/download/?id=1tBkSjllAdxh_g1GMM63EyecsJkqZHNoJ&table_name=fifa_data
