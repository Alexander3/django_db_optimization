# Django DB Optimizations

Woocommerce shop, django backend for generating tickets, react app for scanning codes

## How to start
```
docker-compose up -d
```

# Results
admin search for 'decker' (10 runs for 400000 rows):
+ postgres without index: 627 ms ± 6.2 ms
