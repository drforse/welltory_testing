# welltory_testing  
Result of testing for Welltory   
## Configuration  
### .env  
MYSQL_ROOT_PASSWORD=mysql root password used when creating instance
MYSQL_DATABASE=mysql database name used when creating instance
MYSQL_USER=mysql username used when creating instance
MYSQL_PASSWORD=mysql password used when creating instance
MYSQL_PORT=mysql port used when creating instance
RABBITMQ_DEFAULT_USER=rabbitmq default username used when running rabbitmq
RABBITMQ_DEFAULT_PASS=rabbitmq default password used when running rabbitmq
WELLTORY_DATA_ANALYSIS_PORT=nginx exposed port
### config.ini
```
[server]
secret_key = django secret key
debug = django debug, 0 to False, 1 to True 
allowed_hosts = django allowed_hosts
local_url = url which should use containers when sending requests to this django app

[db] mysql settings used for connection
name = database name
user = username
password = password
host = where instance is running
port = where instance is running

[redis] redis settings used for connection
host = where instance is running
port = where instance is running

[celery] celery config
broker_url = ex.: amqp://myusername:mypassword@localhost
```
### Django Admin
Follow these steps to create django superuser:  
- get welltory_data_analysis service container_id: `docker ps --all`  
- run `docker exec -it <container_id> /bin/bash` to enter shell  
- run `python manage.py createsuperuser`  
- follow manage.py instructions  
- run `exit` to exit the container shell  
### Installation  
1. clone the repo  
2. configure everything you need (check Configuration) (don't forget to add ip to allowed hosts)  
3. run `docker-compose up -d`  
4. create django superuser if needed (check Django Admin) 
### Tests
run `pytest` to run auto-tests 
### Additional info
You can check info about endpoints on /swagger or /redoc  
