.PHONY: build package-install clean lint

build:
	uv build

package-install:
	uv tool install dist/*.whl

clean:
	rm -rf dist/ build/ *.egg-info/

lint:
	uv run ruff check brain_games