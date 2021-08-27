build-dev:
	make stop-dev
	docker-compose -f build/dev/docker-compose.yml up -d --build

run-web:
	make stop-web
	docker-compose -f build/dev/docker-compose.yml up -d --build web
	docker exec -ti dev_web_1 python manage.py makemigrations
	docker exec -ti dev_web_1 python manage.py migrate
	docker-compose -f build/dev/docker-compose.yml up -d --build celery celery-beat

run-test:
	docker-compose -f build/dev/docker-compose.yml up -d --build tests



stop-dev:
	docker-compose -f build/dev/docker-compose.yml down -v

stop-web:
	docker-compose -f build/dev/docker-compose.yml stop web celery celery-beat

logs-dev:
	docker-compose -f build/dev/docker-compose.yml logs -f

create-admin-dev:
	docker exec -ti dev_web_1 python manage.py createsuperuser

