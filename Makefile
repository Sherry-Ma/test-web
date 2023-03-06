install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 or #pylint
build:
	#build container
	docker build -t deploy-fastapi .
run:
	docker run -p 127.0.0.1:8080:8080 860f1c38fd2e
deploy:
	#deploy
all: install lint test deploy