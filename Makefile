build-dev:
	make stop-dev
	docker-compose -f build/dev/docker-compose.yml up -d --build
run-dev:
	docker-compose  -f build/dev/docker-compose.yml up -d --build
stop-dev:
	docker-compose -f build/dev/docker-compose.yml down -v
logs-dev:
	docker-compose -f build/dev/docker-compose.yml logs -f
create-admin-dev:
	docker exec -ti dev_web_1 python manage.py createsuperuser