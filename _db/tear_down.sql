/**
 Usage:
 ```
 psql \
   -U $(whoami) \
   -d postgres \
   -f _db/tear_down.sql
 ```
**/

DROP DATABASE IF EXISTS django_e2e_benchmarks;

DROP USER IF EXISTS django_e2e_benchmarks;
