# Real Estate Site

The project is a bulletin board for a real estate agency.

# How to use

## Install virtual envaroment and requirements

``` #!bash

virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

## Import data from json to the database

``` #!bash

python manage_db.py -c db
puthon manage_db.py -j [json_file]
```

## Run sever

``` #!bash

python server.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
