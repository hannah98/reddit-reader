APP_NAME := "reddit-reader"

CUSTOMDIR := $(PWD)/customsettings
PRAWINI := $(PWD)/praw.ini
PORT := 8000

-include env.makefile

VERSION=$(shell ./version.sh)

ifdef rrcustomdir
CUSTOMDIR := $(rrcustomdir)
endif

ifdef rrprawini
PRAWINI := $(rrprawini)
endif

ifdef rrport
PORT := $(rrport)
endif

.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make <target>\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  %-10s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

build: ## Build the container
	docker build -t $(APP_NAME) --build-arg BUILD_VERSION=$(VERSION) .

stop: ## Stop and remove a running container
	docker rm -f $(APP_NAME) || true

run: stop build ## Run container
	docker run -it --name=$(APP_NAME) -e LOGLEVEL=DEBUG -v $(CUSTOMDIR):/app/customsettings:ro -v $(PRAWINI):/app/praw.ini:ro -p $(PORT):8000 $(APP_NAME)

tag: ## Create a git tag
	@git tag -a "v$(VERSION)" -m "v$(VERSION)"

push: tag ## Push git changes
	git push
	git push --tags
