# Limuko Community Water Management System (LCWMS)

This is a system developed to record billing information of LCMWS clients.

It aims to have a central database for all the records and a way to access them.

## Installation

The project runs of **flask** and depends on other packages as well. The packages are in the requirements file.

<!-- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar. -->

```bash
pip install -r requirements.txt
```

## Usage

There are 2 main parts:

1. Administrator Section
2. Meter Reader Section

### 1. Administrator Section

The previledges of the _admin_ are:

- Add a user (Admin, Reader or Client)
- View all clients in the system, plus their bills

### 2. Meter Reader Section

The Reader can only add the current meter reading of the client

### The Database

The database stores four tables. The **admin**, **reader**, **client** and **bill** tables.

The reader and client tables have a relationship with the bill table to store which client the bill belongs to and which user added the bill to the system.

Also the **is_administrator**, **is_red** and **is_adred** functions are added to help in route protection; namely administrator only, reader only, and administrator and reader routes respectively.

## Note

_Remember to have all the enviroment variables declared before hand as they are needed in creation of the app_

The environment variables needed are:

1. SQLALCHEMY_DATABASE_URI
2. SECRET_KEY
3. ROOT_ID

Initialize the database as follows

In the virtual environment run the following commands:

```bash
    flask shell
```

```bash
    from src.models import db, Admin
    from werkzeug.security import generate_password_hash


    db.create_all()

    password = generate_password_hash('123')
    admin = Admin('admin', password)

    db.session.add(admin)
    db.session.commit()
```

The above initializes the tables in the already created database. Also the root admin is set at this instance. The id of the root admin is set as an environment variable.

Only after all environment variables are set, is when the application can be ran.

There is a Dockerfile and docker-compose file for running the application in a container

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
