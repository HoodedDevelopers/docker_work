STAGE ?= dev

default: deploy_all

.PHONY: build_env
build_env: ../infra/
	python build_env.py

.PHONY: build_ss
build_ss: ../infra/
	python build_ss.py

.PHONY: test
test:
	docker-compose exec web /bin/bash