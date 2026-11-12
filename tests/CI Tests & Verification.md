# CI Tests & Verification Notes (Section D)

This file documents the three automated tests and static code check implemented for the CI pipeline to satisfy the project requirements.

## 1. Automated Tests (`pytest`)
We implemented 3 main automated tests in `tests/test_app.py` covering:
- **Normal Output:** Verifies that the root/home page (`/`) responds successfully with status `200`.
- **Health Endpoint (`/health`):** Confirms that the health check route returns the correct status (`healthy`) and application version.
- **Edge / Error Case:** Validates that requesting a non-existent route correctly returns a `404 Not Found` status.
python -m pytest

## 2. Static Code Check (Linter)
To run the static code check using `flake8` and verify code style without execution, run[cite: 1]:
```bash
python -m flake8 .

## 3. Pipeline Behavior
- Both `flake8` and `pytest` run automatically on every push and pull request via GitHub Actions.
- If any test or static check fails, the pipeline fails immediately and blocks the creation of the Docker image artifact.
