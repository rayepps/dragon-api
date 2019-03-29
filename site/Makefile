SHELL:=/bin/bash





.PHONY: serve
serve:
	python3 -m http.server

.PHONY: deploy
deploy:
	aws s3 cp . s3://greendragon.pro/ --recursive
