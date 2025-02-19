# ATW

This Project should scrape and analyse Data and Websites

## Getting started

``` Python
pipenv run # to download all requirements
pipenv shell # Enable the Evironment (after this it is visible in Code)
```

``` Bash
prisma generate
prisma db push
```


## To run it:
make a config.env with following structure:
``` enviroment
TARGET_URL="<URL>"
TESTING=False
CRAWL=True
```

## Current bugs
Somtimes is the origin multiple times in the DB.
-> THis mean that the Checker is not perfect.
