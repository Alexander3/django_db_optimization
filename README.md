# Django DB Optimizations

Example code that shows how to add postgres index that will make searching admin ultra fast.  
There's also comparison with Haystack + Elasticsearch.

## How to start
```
docker-compose up -d
pipenv sync
pipenv run python manage.py migrate
pipenv run python manage.py demodata # takes ~40min, generates 400k random Customers
pytest
```

# Results
admin search for 'decker' (10 runs for 400000 rows):
+ postgres without index: 627 ms ± 6.2 ms
