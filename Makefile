.PHONY: clean ruff install install-silent type-check stubtest rmclog clog build publish pre-commit help
clean:
	rm -rf build dist pygensuggestions.egg-info .ruff_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.py[co]' -delete
	find . -type f -name '*.so' -delete
install:
	pip install -e .
install-silent:
	$(MAKE) install > /dev/null
ruff:
	ruff check .
type-check:
	mypy pygensuggestions
stubtest: type-check
	stubtest pygensuggestions --strict-type-check-only
rmclog:
	rm ChangeLog || true
clog: rmclog
	git log --pretty --numstat --summary > ChangeLog
build:
	python3 -m build
publish: build
	twine upload dist/* --verbose --skip-existing
pre-commit:
	pre-commit run --all-files
help:
	@echo "Available targets:"
	@echo "  help           - Show this help message"
	@echo "  clean          - Clean build artifacts and caches"
	@echo "  install        - Install the package in editable mode"
	@echo "  install-silent - The above without output"
	@echo "  ruff           - Run ruff linter"
	@echo "  type-check     - Run mypy for type checking"
	@echo "  stubtest       - Run stubtest for type stubs validation"
	@echo "  rmclog         - Remove existing changelog file"
	@echo "  clog           - Generate changelog to file named ChangeLog from git history"
	@echo "  build          - Build the package distributions"
	@echo "  publish        - Publish the package to PyPI"
	@echo "  pre-commit     - Run pre-commit hooks on all files"