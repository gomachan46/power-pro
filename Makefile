build:
	docker build ./ -t power-pro

run:
	docker run -it --rm -v "$$PWD:/usr/src/myapp" -w /usr/src/myapp power-pro bash
