install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

#.PHONY: install test lint selfcheck check build
