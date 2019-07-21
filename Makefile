FILEPATH := $(PWD)

build-local:
	docker build ./hassio-git -t hassio-git --build-arg BUILD_FROM="alpine:latest"

shell: build-local
	docker run -v $(FILEPATH)/mocks/config:/config -v $(FILEPATH)/mocks/data:/data -v $(FILEPATH)/hassio-git/run.py:/opt/run.py -it hassio-git /bin/ash

run: build-local
	docker run -v $(FILEPATH)/hassio-git/mocks/config:/config hassio-git
