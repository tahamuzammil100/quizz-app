# Quiz Demo (Poetry)

This is a small command-line quiz about Machine Learning basics and Deep Learning. It demonstrates using Poetry as the build tool for dependency management, packaging, testing, and running the project.

## Project structure

   ```
   .
   ├── src/quizapp/          # Application source code
   │   ├── cli.py            # Main quiz application
   │   └── quiz_data.json    # Quiz questions
   ├── tests/                # Test files
   ├── docs/                 # Documentation
   ├── pyproject.toml        # Project configuration
   └── README.md             # This file
   ```

   ## Documentation

   API documentation is available in the `docs/` folder.
    To generate/view the documentation:

   ```bash
   cd docs
   make html
   open build/html/index.html
   ```

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


## Build / Package

Build a wheel using Poetry:

```bash
poetry build
```

Artifacts will be created under `dist/` (wheel and sdist).

## Testing

  Run the test suite with:

```bash
  poetry run pytest
```


  To run a specific test file:

```bash
  poetry run pytest tests/test_cli.py
```

## Notes for reviewers / graders

- The question dataset is in `src/quizapp/quiz_data.json`. It is included by the package so the CLI can read it at runtime.
- The console entry point is configured in `pyproject.toml` as `quizapp = "quizapp.cli:main"` so `poetry run quizapp` will run the CLI.
- To reproduce the environment exactly, commit and push the `poetry.lock` file (if present). Reviewers can use `poetry install` for reproducible dependencies.

## Submission and GitHub

- Create a public repository on GitHub (or use the provided one), push all files and the commit history, and include the repository link for grading.
- Include `pyproject.toml`, `poetry.lock`, `README.md`, and tests in the root of the repo so reviewers can run the commands above.

## Contact / Author

Student: tahamuzammil100@gmail.com
