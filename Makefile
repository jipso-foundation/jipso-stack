# Makefile for JIPSO Framework
# Author: JIPSO Foundation
# Usage: run "make <target>"

.PHONY: install test benchmark pvp export build publish clean release

# Install all dependencies using Poetry
install:
	poetry install


# Export dependencies to requirements.txt (for Docker or pip users)
export:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# Bump version and create release commit + tag (e.g. make release VERSION=1.2.0)
release:
	@if [ -z "$(VERSION)" ]; then \
		echo "❌ ERROR: You must provide VERSION=X.Y.Z"; \
		exit 1; \
	fi
	sed -i "s/version = \".*\"/version = \"$(VERSION)\"/" pyproject.toml
	sed -i "s/__version__ = .*/__version__ = '$(VERSION)'/" jipso/__init__.py
	sed -i "s/__version__ = .*/__version__ = '$(VERSION)'/" jipso/cli.py
	sed -i "s/release = .*/release = '$(VERSION)'/" docs/conf.py
	git add .
	git commit -m "🔖 Release version v$(VERSION)"
	git push origin main
	git tag v$(VERSION)
	git push origin v$(VERSION)

doc:
	poetry run sphinx-build -b html docs docs/_build/html

docker_build:
	docker build .

build:
	poetry build

test_release:
	poetry run pytest tests/release/

test_local:
	poetry run pytest tests/local/

bandit:
	poetry run bandit -r jipso -ll

clean:
	rm -rf dist/* .pytest_cache/* .benchmarks/* logs/* docs/_build/* docs/generated/* jipso/__pycache__/* jipso/Mind/__pycache__/* jipso/Body/__pycache__/*
