# Quiz Demo (Poetry)

This is a small command-line quiz about Machine Learning basics and Deep Learning. It demonstrates using Poetry as the build tool for dependency management, packaging, testing, and running the project.

## Project structure

- `pyproject.toml` – Poetry project configuration and metadata
- `src/quizapp/` – package source (CLI and data)
  - `quizapp/cli.py` – command-line entry point
  - `quizapp/quiz_data.json` – questions (easy/medium/hard)
- `tests/` – pytest test suite

## Requirements (developer)

- Python 3.8+
- Poetry (recommended) OR a Python virtual environment with `pip`

## Install (Poetry - recommended)

1. From the project root:

```bash
poetry install
```

This creates an isolated environment and installs runtime and dev dependencies.

## Install (pip / virtualenv)

If you prefer not to use Poetry, you can create a virtual environment and install the exported requirements. First export a `requirements.txt` (optional):

```bash
# export from poetry (run where poetry is available)
poetry export -f requirements.txt --output requirements.txt --without-hashes

# then create and activate a venv and install
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the quiz

After installing dependencies, run the quiz with:

```bash
poetry run quizapp
# or, when using a venv:
python -m quizapp.cli
```

Follow the prompts: select difficulty (1/2/3 for easy/medium/hard) and answer questions with `a`, `b`, `c`, or `d`.

## Run tests

With Poetry:

```bash
poetry run pytest -q
```

With venv / pip:

```bash
source .venv/bin/activate
pytest -q
```

Developer notes (src layout)
--------------------------------

This project uses the "src" layout (`src/quizapp`). When running tests without installing the package into your environment you may need to ensure `src/` is on Python's import path. There are two convenient options:

1) Run tests with PYTHONPATH set (works without installing the package):

```bash
# from project root
PYTHONPATH=src pytest tests/test_quiz.py -q
```

2) Install the package into the project's venv (editable install) so imports work normally. Note: editable installs require a project metadata backend that supports editable installs. If you use Poetry, the easiest reproducible method is to use Poetry's environment:

```bash
# (recommended) use Poetry to create the env and run tests
poetry install
poetry run pytest -q
```

Or use the helper script included in `scripts/run-tests.sh`:

```bash
./scripts/run-tests.sh
```

If you prefer an editable `pip install -e .` workflow, you may need to add setuptools-based metadata (a `setup.cfg`/`setup.py`) or use a backend that supports PEP 660 editable installs.


## Build / Package

Build a wheel using Poetry:

```bash
poetry build
```

Artifacts will be created under `dist/` (wheel and sdist).

## Notes for reviewers / graders

- The question dataset is in `src/quizapp/quiz_data.json`. It is included by the package so the CLI can read it at runtime.
- The console entry point is configured in `pyproject.toml` as `quizapp = "quizapp.cli:main"` so `poetry run quizapp` will run the CLI.
- To reproduce the environment exactly, commit and push the `poetry.lock` file (if present). Reviewers can use `poetry install` for reproducible dependencies.

## Submission and GitHub

- Create a public repository on GitHub (or use the provided one), push all files and the commit history, and include the repository link for grading.
- Include `pyproject.toml`, `poetry.lock`, `README.md`, and tests in the root of the repo so reviewers can run the commands above.

## Contact / Author

Student: tahamuzammil100@gmail.com
