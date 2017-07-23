include .env

.PHONY: jupyter postgres postgres-shell psql pgadmin elasticsearch clean rm-containers rm-images

jupyter:
	@ docker-compose up jupyter

postgres:
	@ docker-compose up -d postgres

postgres-shell: postgres
	@ docker-compose exec postgres bash

psql: postgres
	@ sleep 1 # lets postgres container initialize
	@ docker-compose exec postgres psql -U postgres

pgadmin: postgres
	@ docker-compose up -d pgadmin

elasticsearch:
	@ docker-compose up -d elasticsearch

clean: rm-containers rm-images

rm-containers:
	-@ docker container ls -aq -f "status=running" | xargs -I {} docker container kill {}
	-@ docker-compose down --remove-orphans -v
	-@ docker container prune -f

rm-images:
	-@ docker image prune -f
