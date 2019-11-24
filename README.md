# Django DB Optimizations

Woocommerce shop, django backend for generating tickets, react app for scanning codes

## How to start
```
docker-compose up -d
```

# Results
admin search for 'decker' (10 runs for 400000 rows):
+ postgres without join:   716 ms ± 6.01 ms (105 queries)
+ postgres without index:  627 ms ± 6.2 ms
+ postgres with GIN index: 177 ms ± 3.63 ms, request is 3,5x faster, query is 140x faster




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

```
                                                                                   QUERY PLAN                                                                                   
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Aggregate  (cost=1667.91..1667.92 rows=1 width=8) (actual time=1.774..1.774 rows=1 loops=1)
   ->  Bitmap Heap Scan on main_customer  (cost=183.17..1666.95 rows=384 width=0) (actual time=0.675..1.708 rows=181 loops=1)
         Recheck Cond: ((upper((first_name)::text) ~~ '%DECKER%'::text) OR (upper((last_name)::text) ~~ '%DECKER%'::text) OR (upper((phone_number)::text) ~~ '%DECKER%'::text))
         Heap Blocks: exact=181
         ->  BitmapOr  (cost=183.17..183.17 rows=384 width=0) (actual time=0.590..0.590 rows=0 loops=1)
               ->  Bitmap Index Scan on customer_admin_search  (cost=0.00..60.96 rows=128 width=0) (actual time=0.069..0.069 rows=0 loops=1)
                     Index Cond: (upper((first_name)::text) ~~ '%DECKER%'::text)
               ->  Bitmap Index Scan on customer_admin_search  (cost=0.00..60.96 rows=128 width=0) (actual time=0.495..0.495 rows=181 loops=1)
                     Index Cond: (upper((last_name)::text) ~~ '%DECKER%'::text)
               ->  Bitmap Index Scan on customer_admin_search  (cost=0.00..60.96 rows=128 width=0) (actual time=0.024..0.024 rows=0 loops=1)
                     Index Cond: (upper((phone_number)::text) ~~ '%DECKER%'::text)
 Planning Time: 0.268 ms
 Execution Time: 1.878 ms
```

**
