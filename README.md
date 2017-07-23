# data-playground

Personal playground for simple data engineering and analysis projects.

## Setup

### Jupyter

#### To start a Jupyter Notebook Server

This Jupyter Notebook server is be capable of connecting to all data sources
that are located in the [docker-compose.yml](docker-compose.yml) file by using
their docker-compose service names as hostnames, along with the appropriate
ports. For details on the python libraries available within the
jupyter-notebook runtime see the
[jupyter/requirements.txt](jupyter/requirements.txt) file.

```
make jupyter
```

The login URL (with pre-set token) will be:
http://localhost:8888/?token=cb757c6e42a6b68b6dc73685eb78e231c4baf1db2c767783

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

#### To start a `bash` shell session from within the PostgreSQL container

This will ensure postgres is running, and begin a `bash` shell session from
within the postgres container:

```
make postgres-shell
```

#### To start a `psql` session from within the PostgreSQL container

This will ensure postgres is running, and begin a `psql` session from within the
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
the local dockerized postgres container use the credentials given above and set
the `POSTGRES_HOST` to the postgres service name used in the
[docker-compose.yml](docker-compose.yml) file:

- `POSTGRES_HOST`: postgres

### ElasticSearch

#### To start an elasticsearch instance at http://localhost:9200/

This starts a single instance:

```
make elasticsearch
```

## More To Come (this is early stage WIP)...
