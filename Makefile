include .env

.PHONY: \
	cassandra \
	elasticsearch \
	jupyter \
	mysql mysql-shell mysql-client phpmyadmin \
	postgres postgres-shell psql pgadmin \
	clean rm-containers rm-images

cassandra:
	@ docker-compose up -d cassandra

elasticsearch:
	@ docker-compose up -d elasticsearch

jupyter:
	@ docker-compose up -d jupyter
	@ sleep 3 # lets jupyter container initialize
	@ open http://localhost:8888/

postgres:
	@ docker-compose up -d postgres

postgres-shell: postgres
	@ docker-compose exec postgres bash

psql: postgres
	@ sleep 5 # lets postgres container initialize
	@ docker-compose exec postgres psql -U postgres

pgadmin: postgres
	@ docker-compose up -d pgadmin
	@ sleep 5 # lets pgadmin container initialize
	@ open http://localhost:5050/browser/

mysql:
	@ docker-compose up -d mysql

mysql-shell:
	@ docker-compose exec mysql bash

mysql-client: mysql
	@ sleep 15 # lets mysql container initialize
	@ docker-compose exec mysql mysql --password=$(MYSQL_ROOT_PASSWORD)

phpmyadmin: mysql
	@ sleep 15 # lets mysql container initialize
	@ docker-compose up -d phpmyadmin
	@ sleep 3 # lets phpmyadmin container initialize
	@ open http://localhost:8080/

clean: rm-containers rm-images

rm-containers:
	-@ docker container ls -aq -f "status=running" | xargs -I {} docker container kill {}
	-@ docker-compose down --remove-orphans -v
	-@ docker container prune -f

rm-images:
	-@ docker image prune -f
