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

- Add and delete a user (Admin, Reader or Client)
- View all clients in the system, plus their bills

### 2. Meter Reader Section

The Reader can only add the current meter reading of the client

### The Database

The database stores four tables. The **admin**, **reader**, **client** and **bill** tables.

The reader and client tables have a relationship with the bill table to store which client the bill belongs to and which user added the bill to the system.

Also the **is_admin** and **can** functions are added to help in route protection.

## Note

_Remember to have all the enviroment variables declared before hand as they are needed in creation of the app_

Also, there's a Dockerfile for those who want to run in on a docker container. Ensure before you build, there's a working database in your container, or your are connected to one.

The project as of now is using sqlite, which is initialized as follows

In the virtual environment run the following commands:

```bash
    (venv)$ flask shell
```

```bash
    >> from src.models import db, Admin
    >> db.create_all()
    >> admin = Admin('admin', '123')
    >> db.session.add(admin)
    >> db.session.commit()
```

Then build the image and run it as usual.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
