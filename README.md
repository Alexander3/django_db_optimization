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




``` sql
EXPLAIN ANALYZE 
SELECT COUNT(*) AS "__count" FROM "main_customer" 
WHERE (UPPER("main_customer"."first_name"::text) LIKE UPPER('%decker%') OR
 UPPER("main_customer"."last_name"::text) LIKE UPPER('%decker%') OR
 UPPER("main_customer"."phone_number"::text) LIKE UPPER('%decker%'));
```
```
                                                                                      QUERY PLAN                                                                                      
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Finalize Aggregate  (cost=138501.30..138501.31 rows=1 width=8) (actual time=261.207..261.207 rows=1 loops=1)
   ->  Gather  (cost=138501.09..138501.30 rows=2 width=8) (actual time=261.117..264.458 rows=3 loops=1)
         Workers Planned: 2
         Workers Launched: 2
         ->  Partial Aggregate  (cost=137501.09..137501.10 rows=1 width=8) (actual time=251.873..251.873 rows=1 loops=3)
               ->  Parallel Seq Scan on main_customer  (cost=0.00..137500.69 rows=160 width=0) (actual time=4.235..251.819 rows=60 loops=3)
                     Filter: ((upper((first_name)::text) ~~ '%DECKER%'::text) OR (upper((last_name)::text) ~~ '%DECKER%'::text) OR (upper((phone_number)::text) ~~ '%DECKER%'::text))
                     Rows Removed by Filter: 133273
 Planning Time: 0.250 ms
 Execution Time: 264.560 ms
```
