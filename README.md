# recipe-suggestion

Framework
  - Backend
    - Django
    - MySql
  
  - Frontend
    - Angularjs
    - Bootstrap
    
System requirements(Dev Env):
  - Python version : 2.7
  - OS : Ubuntu
  - Database : MySQl
  
Run recipe-suggestion:
  - Clone the project
  - Create Virtual env and activate it
  - Install requirements
    - pip install -r requirements.txt
  - Run recrate_db.sh
    - tools/recreate_db.sh
    - database - dashboard, user - dashboard, password - dashboard
  - Export excell data to MYSQL DB
    - Go to tools folder
    - cd tools
    - Run - python excel_to_db.py 
  - cd ../
  - Run tools/migrate.sh

Thats it, all set go to 127.0.0.1:8000 to see app in action.
