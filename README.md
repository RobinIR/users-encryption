# User Encryption for MongoDB and GraphQL server


## Local Installation [only documented for windows]

1. Clone or Download the project in to a directory.

2. Install latest stable version of Python 3. [https://www.python.org/downloads/]

3. Install virtual environment for Python. [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/]


    * Type the below command in the project directory to create virtual environment.

    `python -m venv venv`

    * Type the below command in the project directory to activate the virtual environment.

    `.\venv\Scripts\activate`

4. Type the below command in the project directory to install all required modules.

    `pip install -r requirements.txt`

5. Execute the below command to run the application. (Congifgure variables before this step, see below for more info)

    `python encryption.py`

6. The plaintext username and password will be encrypted for use in the MongoDB collection. The users should have the admin right using isAdmin property as illustrated below:

```users.json
    {
     "users":[
         {"username":"admin", "isAdmin": true, "password":"password"},
         {"username":"username1", "isAdmin": true, "password":"Password1"},
         {"username":"username2", "isAdmin": true, "password":"Password2"},
         .............................................
        ]
    }
```


## Creation of MongoDb database for Qualiexplore application

The MongoDB should have the encrypted users collection.

1. Install MongoDb database tools in to your PC. [https://www.mongodb.com/try/download/database-tools]
2. Run the following mongoimport command for importing users.json file
`mongoimport --uri <connection_string> --collection <collectionname> --drop --file <filename>`

3. The users collection should be like
```users.json
    {
     "users":[
         {"username":"Encrypted Username", "isAdmin": true, "password":"Encrypted Password"},
         {"username":"Encrypted Username", "isAdmin": true, "password":"Encrypted Password"},
         .................................................................
         ]
    }
```