**Python CRUD**

This is an small project that uses the next technologies:

 - ***[Python 3.7.7](https://www.python.org/downloads/release/python-377/)***
 - ***[SQLite3](https://docs.python.org/2/library/sqlite3.html)***
 - ***[Falcon Framework](https://falcon.readthedocs.io/en/stable/user/index.html)***
 - ***[Gunicorn](https://gunicorn.org/)***

___

**INITIAL**

The architecture of the project consists in two approaches on how the data is handled. It has a ***SQL*** version which uses ***SQLite***, and a ***NoSQL*** type version, which uses a ***.json*** file.

To check if you have the required version of python to run this project, you should run the command:

```sh
python --version
```

It should prompt something like:

```sh
Python 3.7.7
```

___

**STRUCTURE**

First, open the terminal. Then enter in the project folder.

It should have this structure

```
./crud
  /app
    /api
        /data
            /abstractor
              NoSQLPerson.py
              SQLPerson.py
            /database
              migrate.py
              NoSQL.py
              SQL.py
              storage.db
              storage.json
            /operators
              PersonOperator.py
        /handler
          Error.py
          PersonDetail.py
          Persons.py
          PersonSearch.py
        /utils
          /commons
            search.py
            similar.py
          /form
            fields.py
            validate.py
          logger.py
          system.py
        router.py
        run.py
    /client
      /src
        /models
          person.py
        /services
          http.py
          PersonService.py
        /utils
          /common
            clear.py
          /form
            fields.py
            userInput.py
            validate.py
          system.py
        /views
          /common
            exitOrHome.py
            PersonDetail.py
            recreateScenary.py
          /components
            CreatePerson.py
            DeletePerson.py
            EditPerson.py
            ModifyPerson.py
            PersonList.py
            SearchBy.py
            SelectEdit.py
          /pages
            AllPersons.py
            Home.py
            Register.py
            Search.py
      run.py
  /logs
    -- log files
  api.sh
  client.sh
  README.md
```

The applications has the capability to run in different instances the API and the Client. Thus givin the possibility to use another client on the same API.

___

**RUN THE PROJECT**

The project will install the necessary dependencies according to what you are executing (API or Client). Its necessary to activate the API in order to use the Client. The best way to run the app is through the Bash files located in the root of the project.

***API***

To run the API, you should open a Terminal and run the bash script crud/api.sh like the following:

```sh
bash api.sh
```

This will localize the python enviroment where to install the necessary packages and run from there. This accepts one parameter that will tell which database to use. (NoSQL or SQL). The SQL database is selected by default

To do that, you should run the script as following:

```sh
bash api.sh nosql
```

***CLIENT***

To run the CLIENT, you should have the API running in another Terminal. Then run the following script:

```sh
bash client.sh
```
