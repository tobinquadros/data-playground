# data-playground

Personal playground for simple data engineering and analysis projects.

## Setup

### PostgreSQL

#### To start a dockerized PostgreSQL server

```
make postgres
```

Uses these default ENVIRONMENT VARIABLES:

- `POSTGRES_DATABASE`: postgres
- `POSTGRES_HOST`: localhost
- `POSTGRES_PASSWORD`: postgres
- `POSTGRES_PORT`: 5432
- `POSTGRES_USER`: postgres

#### To use `psql` directly from within the same PostgreSQL instance

This will ensure postgres is running, and begin a psql session from within the
postgres container (no local dependencies need be met):

```
make psql
```

Exit the `psql` session with `<ctrl-d>`.

#### To start a pgAdmin4 instance at http://localhost:5050/browser/

This will ensure the local postgres is running, and start pgadmin:

```
make pgadmin
```

You can now use pgAdmin to connect to any PostgreSQL instance. To connect to
the local postgres server use the credentials given above and set the
`POSTGRES_HOST` to the hostname used in the docker-compose network:

- `POSTGRES_HOST`: postgres

### ElasticSearch

#### To start an elasticsearch instance at http://localhost:9200/

This starts a single instance:

```
make elasticsearch
```

## More To Come (this is early stage WIP)...
