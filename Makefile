## @ pypi Commands
.PHONY: pypi
pypi:
	poetry build
	poetry publish

## @ Tests Commands
.PHONY: test
test: ## Run tests
	pytest -v

## @ requirements Commands
.PHONY: requirements
requirements: ## Update requirements.txt
	poetry export --without-hashes -f requirements.txt > requirements.txt

