# data-playground
Personal playground for simple data engineering and analysis projects.

## Setup

To easily start a local PostgreSQL server and pgAdmin4 instance (available at
`http://localhost:5050/browser/`):

```
make pgadmin
```

To connect directly to the same postgres instance with `psql`:

```
make psql
```

The docker image's postrges database credentials:

- `POSTGRES_DATABASE`: postgres
- `POSTGRES_HOST`: postgres (it's on the same docker-compose network)
- `POSTGRES_PORT`: 5432
- `POSTGRES_USER`: postgres

## More To Come (this is early stage WIP)...
