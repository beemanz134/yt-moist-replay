<p align="center">


## Table of Contents





## What's in the box ?

### uv

[uv](https://github.com/astral-sh/uv) is an extremely fast Python package and project manager, written in Rust.

**pyproject.toml file** ([`pyproject.toml`](pyproject.toml)): orchestrate your project and its dependencies
**uv.lock file** ([`uv.lock`](uv.lock)): ensure that the package versions are consistent for everyone
working on your project

For more configuration options and details, see the [configuration docs](https://docs.astral.sh/uv/).

### pre-commit

[pre-commit](https://pre-commit.com/) is a framework for managing and maintaining multi-language pre-commit hooks.

**.pre-commit-config.yaml file** ([`.pre-commit-config.yaml`](.pre-commit-config.yaml)): describes what repositories and
hooks are installed

For more configuration options and details, see the [configuration docs](https://pre-commit.com/).

### ruff

[ruff](https://github.com/astral-sh/ruff) is an extremely fast Python linter, written in Rust.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://github.com/astral-sh/ruff#configuration).

### mypy

[mypy](http://mypy-lang.org/) is an optional static type checker for Python that aims to combine the benefits of
dynamic (or "duck") typing and static typing.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://mypy.readthedocs.io/).

### bandit

[bandit](https://bandit.readthedocs.io/) is a tool designed to find common security issues in Python code.

Rules are defined in the [`pyproject.toml`](pyproject.toml).

For more configuration options and details, see the [configuration docs](https://bandit.readthedocs.io/).

### docformatter

[docformatter](https://github.com/PyCQA/docformatter) is a tool designed to format docstrings to
follow [PEP 257](https://peps.python.org/pep-0257/).

Options are defined in the [`.pre-commit-config.yaml`](.pre-commit-config.yaml).

---

## Testing

We are using [pytest](https://docs.pytest.org/) & [pytest-cov](https://github.com/pytest-dev/pytest-cov) to write tests.

To run tests:


