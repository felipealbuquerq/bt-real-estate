## Instructions

- ### Install PostgreSQL;
    #### Mac
    https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d
    
- ### Create a DB
    #### Mac
    <p>postgres -D /usr/local/var/postgres</p>
    <p>createdb imobdb</p>
    
- ### Create a 'secrets.json' file with your SECRET_KEY, DB_USER and DB_PASSWORD;
    ![Screenshot](/screenshots/secrets_json.png)

- Create a venv with Python 3.7
- pip install -r requirements.txt;
- python manage.py makemigrations && python manage.py migrate;
- python manage.py runserver;
- Enjoy =)
