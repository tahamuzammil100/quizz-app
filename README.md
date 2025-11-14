# Quiz Demo (Poetry)

This project is a small command-line quiz about Machine Learning basics and Deep Learning. It demonstrates using Poetry as the build tool for dependency management, packaging, testing, and running the project.

Key features:
- Dependency management with Poetry
- Packaging to wheel via `poetry build`
- Test support with `pytest`
- Simple CLI that asks the user to pick a difficulty and answer multiple-choice questions (a/b/c/d)

Quick commands

Install dependencies (recommended):

```bash
poetry install
```

Run tests:

```bash
poetry run pytest -q
```

Run the quiz (after install):

```bash
poetry run quizapp
```

Build a wheel:

```bash
poetry build
```

Publishing / GitHub

- Create a public repository on GitHub and push this directory as the project root.
- Provide the link to the repository for evaluation.

Notes for reviewers
- The JSON file with questions is at `src/quizapp/quiz_data.json` and is included in the package so the CLI can access it at runtime.
