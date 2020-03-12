# VueDjangoTemplate

## Project Setup
For project setup, read frontend/README.md and APIs/CoreAPI/README.md

frontend will run on http://localhost:8081/

backend api will run on http://localhost:8000/api/v1/

## Issue with CORS on Chrome
When running on chrome, if clicking the search button doesn't retun the json response, it's likely issues with CORS.

Running on incognito mode of chrome should work.

The issue seems to be with the new chrome security update, having "Access-Control-Allow-Origin" in the header still didn't work for me.

## TODO
### Frontend
Set up Vuex - store

Routing

Unit Tests
### Backend API
Set up proper architecture as needed - service layer, repository layer, etc. 

Persist data from Elasticsearch and other db

Unit Tests
## Preview - the only useless functionality right now
![alt text](./searchTemplate.PNG)
*click search
![alt text](./searchJsonReturnTemplate.PNG)
