# Django DB Optimizations

Example code that shows how to add postgres index that will make searching admin ultra fast.  
There's also comparison with Haystack + Elasticsearch.

## How to start
```
docker-compose up -d
pipenv sync
pipenv run python manage.py migrate

# load db dump or generate data instead
# pipenv run python manage.py demodata # takes ~40min, generates 400k random Customers
wget https://alpakara-public.s3.eu-central-1.amazonaws.com/dump.gz
docker-compose exec db bash
cat /app/dump.gz | gunzip | psql -U $POSTGRES_USER $POSTGRES_DB

pipenv run pytest
pipenv run python manage.py runserver
```
Login to http://localhost:8000/admin using:  
email: `demo@demo.com`  
password: `demo123`

# Results
admin search for 'decker' (10 runs for 400000 rows):
+ postgres without join:  716 ms ± 6.01 ms (105 queries)
+ postgres without index: 627 ms ± 6.2 ms
