include .env

.PHONY: postgres psql pgadmin elasticsearch clean rm-containers rm-images

postgres:
	@ docker-compose up -d postgres

psql: postgres
	@ sleep 1 # lets postgres container initialize
	@ docker-compose exec postgres psql -U postgres

pgadmin: postgres
	@ docker-compose up -d pgadmin

elasticsearch:
	@ docker-compose up -d elasticsearch

clean: rm-containers rm-images

rm-containers:
	-@ docker container ls -aq -f "status=running" -f "label=component-id=pgadmin" | xargs -I {} docker container kill {}
	-@ docker container ls -aq -f "status=exited"  | xargs -I {} docker container rm {}
	-@ docker-compose down --remove-orphans -v

rm-images:
	-@ docker image ls -aq -f "dangling=true" | xargs -I {} docker image rm -f {}
