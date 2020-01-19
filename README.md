# ShadowModreg Module Registration App

## How to run

1. Install [python3](https://www.python.org/downloads/) and [postgresql 12](https://www.postgresql.org/download/)

2. run the following commands in command line:

   1. `cd path_to_source_code`

   2. `py -3 -m pip install -r requirements.txt` or `python3 -m pip install -r requirements.txt`

   3. `psql -d postgres -U postgres -f db.sql`

   followed by entering your password
3. configure the credential in app.py:

   ```
   # Config
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'\
       .format(
           username='<username>',
           password='<password>',
           host='localhost',
           port=<port number>,
           database='<database_name>'
       )
   ```

   replace `<username>`, `<password>`,  `<port>` , and `<database>` with the actual configuration from your database. If you are not sure about `<port>` and don't recall changing such a value during initial setup or launching of PostgreSQL server, then it should be `5432` by default. 

4. Run `py -m 3 app.py` or `python3 app.py`

5. Navigate to `http://127.0.0.1:5000/` in your browser to check if flask is active.

## Usage
The application comes preloaded with an admin account with the following credentials

username: admin
password: password1

and student account with the following credentials:

username: user

password: password