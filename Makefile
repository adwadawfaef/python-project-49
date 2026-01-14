.PHONY: build package-install clean

build:
	uv build

package-install:
	uv tool install dist/*.whl

clean:
	rm -rf dist/ build/ *.egg-info/
