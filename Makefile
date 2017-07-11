include .env

.PHONY: pgadmin clean rm-containers rm-images

pgadmin:
	@docker-compose up -d pgadmin

psql:
	@docker-compose up -d postgres
	@docker-compose exec postgres psql -U postgres

clean: rm-containers rm-images

rm-containers:
	-@ docker container ls -aq -f "status=running" -f "label=component-id=pgadmin" | xargs -I {} docker container kill {}
	-@ docker container ls -aq -f "status=exited"  | xargs -I {} docker container rm {}
	-@ docker-compose down --remove-orphans -v

rm-images:
	-@ docker image ls -aq -f "dangling=true" | xargs -I {} docker image rm -f {}
