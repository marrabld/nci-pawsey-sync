# nci-pawsey-sync
A small flask project designed to keep the Copernicus archive between the NCI and Pawsey in Sync


## Install Dependencies

Docker    
Docker-compose    

## Runtime Dependencies
These can be installed through the manage.py tool

### Pawsey's Pshell client
https://bitbucket.org/datapawsey/mfclient/downloads/

### NCI sara api client
https://bitbucket.org/chchrsc/auscophub/downloads/


## Install 

`docker-compose up`

## manage.py 

```
python manage.py 
    init_db             Initialize the database.    
    load_test_data      Populate the database with dummy data so we can test    
                        the application    
    drop_db             Drop the database.    
    update_pshell       Download the latest version of pshell used to transfer    
                        to Pawsey    
    update_auscop       update the auscop api script from bitbucket    
    clear_cache         Delete the directory where the files are cached.    
    shell               Runs a Python shell inside Flask application context.    
    runserver           Runs the Flask development server i.e. app.run()    ```
    
    
