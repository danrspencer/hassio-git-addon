FILEPATH := $(PWD)

shell: build-mock
	docker run -v $(FILEPATH)/data:/data -v $(FILEPATH)/../hassio-git/run.py:/opt/run.py -it hassio-git-mock /bin/ash

build-mock: build-local
	docker build ./ -t hassio-git-mock

build-local:
	docker build ../hassio-git -t hassio-git --build-arg BUILD_FROM="alpine:latest"