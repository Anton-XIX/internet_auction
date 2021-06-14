build-dev:
	make stop-dev
	docker-compose -f build/dev/docker-compose.yml up -d --build

run-dev:
	docker-compose -f build/dev/docker-compose.yml up -d --build web
	docker exec -ti dev_web_1 python manage.py makemigrations
	docker exec -ti dev_web_1 python manage.py migrate

stop-dev:
	docker-compose -f build/dev/docker-compose.yml down -v

stop-web:
	docker-compose -f build/dev/docker-compose.yml stop web

logs-dev:
	docker-compose -f build/dev/docker-compose.yml logs -f

create-admin-dev:
	docker exec -ti dev_web_1 python manage.py createsuperuser

