/**
 Usage:
 ```
 psql \
   -U $(whoami) \
   -d postgres \
   -v APP_USER_PASSWORD='password' \
   -f _db/set_up.sql
 ```
**/

BEGIN;
CREATE USER django_e2e_benchmarks WITH PASSWORD :'APP_USER_PASSWORD';
ALTER USER django_e2e_benchmarks CREATEDB;
COMMIT;

CREATE DATABASE django_e2e_benchmarks OWNER django_e2e_benchmarks;
