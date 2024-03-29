## Instructions

- ### Install PostgreSQL;
    #### Mac
    ##### Remove previous versions of PostgreSQL
    <code>brew uninstall --force postgresql</code>

    ##### Delete all Files of Postgres
    <code>rm -rf /usr/local/var/postgres</code>

    ##### Install Postgres with Homebrew
    <code>brew install postgres</code>

    ##### Install PostGIS with Homebrew
    <code>brew install postgis</code>

    ##### Start PostgreSQL server
    <code>pg_ctl -D /usr/local/var/postgres start</code>

    ##### Create Database
    <code>initdb /usr/local/var/postgres</code>

    <p>If terminal shows an error</p>
    <code>initdb: directory "/usr/local/var/postgres" exists but is not empty
        If you want to create a new database system, either remove or empty
        the directory "/usr/local/var/postgres" or run initdb
        with an argument other than "/usr/local/var/postgres".</code>
    
    ##### Remove old database file
    <code>rm -r /usr/local/var/postgres</code>

    ##### Run the initdb command again
    <code>initdb /usr/local/var/postgres</code>    

    [Reference](https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d)
    
- ### Create a DB
    #### Mac
    
    ##### Create a new database
    <code>createdb imobdb</code>

    ##### Enable PostGIS
    <code>psql imobdb</code>
    <p>This command should show the psql command prompt</p>

    ![Screenshot Terminal](/screenshots/psql_command_prompt.png)

    [Reference](https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d)    
    
- ### Create a 'secrets.json' file with your SECRET_KEY, DB_USER and DB_PASSWORD;
    ![Screenshot JSON](/screenshots/secrets_json.png)

- Create a venv with Python 3.7
- python -m pip install django or python3 -m pip install django
- pip install -r requirements.txt;
- python manage.py makemigrations && python manage.py migrate;
- python manage.py runserver;
- Enjoy =)
