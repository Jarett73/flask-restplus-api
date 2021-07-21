#Test Flask App


#Installation:
##Python-version: 3.6

###Create a Virtual Environment in the root directory: 
>virtualenv venv
>![alt text](assets/create_venv.png)

###Activate the Virtual Environment:
> venv/Scripts
>activate

###Install dependencies in the activated environment: 
>![alt text](assets/activate_run_requirements.png)
>pip install -r requirements.txt

###Start the application from the root directory
>python manage.py runserver
>![alt text](assets/runserver.png)

###Open the url in the browser
>http://127.0.0.1:5000/api/v1
>Note: append "/api/v1" at the end of the url
>>![alt text](assets/setup_api_success.png)
