FILEPATH := $(PWD)

run:
	docker run hassio-git-mock

shell:
	docker run -v $(FILEPATH)/data:/data -v $(FILEPATH)/../hassio-git/run.py:/opt/run.py -it hassio-git-mock /bin/ash

build-mock:
	docker build ./ -t hassio-git-mock

build-local:
	docker build ../hassio-git -t hassio-git --build-arg BUILD_FROM="alpine:latest"