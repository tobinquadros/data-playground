include .env .env.secret

.PHONY: jupyter \
	build \
	postgres postgres-shell psql pgadmin db-setup \
	clean rm-containers rm-images

jupyter: postgres db-setup
	@ docker-compose up -d jupyter
	@ sleep 3 # lets jupyter container initialize
	@ open http://localhost:8888/?token=$(JUPYTER_APP_TOKEN)

build:
	@ docker-compose build

postgres:
	@ docker-compose up -d postgres

postgres-shell: postgres
	@ docker-compose exec postgres bash

psql: postgres
	@ sleep 5 # lets postgres container initialize
	@ docker-compose exec postgres psql -U $(POSTGRES_USER)

pgadmin: postgres
	@ docker-compose up -d pgadmin
	@ sleep 5 # lets pgadmin container initialize
	@ open http://localhost:5050/browser/

db-setup: postgres
	@ sleep 5 # lets postgres container initialize
	@ docker-compose exec postgres psql \
		--set=PSV_FILE=$(PSV_FILE) \
		--set=VIOLATION_CODES_FILE=$(VIOLATION_CODES_FILE) \
		--set=NEW_DB=$(POSTGRES_DB) \
		postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOSTNAME)/postgres \
		-f /code/data/setup.sql

clean: rm-containers rm-images

rm-containers:
	-@ docker container ls -aq -f "status=running" | xargs -I {} docker container kill {}
	-@ docker-compose down --remove-orphans -v
	-@ docker container prune -f

rm-images:
	-@ docker image prune -f
