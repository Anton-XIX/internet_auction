# Auction


## Dependencies
Project dependencies:

- docker
- python 3.8 +
- django 3.2.4
- PostgreSQL 
- Django Rest Framework 3.12.4
- Pillow 8.1.2


## Usage
Create 2 files in main folder:
.env.dev 
```
DEBUG=1
DJANGO_ALLOWED_HOSTS=*
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_dev
SQL_USER=django
SQL_PASSWORD=django_pass
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres

```

.env.db
```
POSTGRES_USER=django
POSTGRES_PASSWORD=django_pass
POSTGRES_DB=django_dev
```

### Development:
```
# Up
$ make build-dev

# Navigate to:
# - admin http://0.0.0.0:8080/admin/

# Logs
$ make logs-dev

# Down
$ make stop-dev

# Create superuser
$ create-admin-dev

```
---
