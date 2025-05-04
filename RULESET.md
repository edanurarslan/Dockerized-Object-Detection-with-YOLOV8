# Branch Protection Ruleset

This document outlines the branch protection rules applied to the `main` branch of the **Dockerized YOLOv8 Object Detection Microservice** repository to ensure code quality, maintainability, and collaborative discipline.

## Target Branch: `main`

All rules below are enforced strictly on the `main` branch to preserve stability and ensure all code contributions are reviewed and tested before integration.

---

## Required Status Checks

- All pull requests must pass all required status checks before merging:
  - Unit tests and API tests must pass.
  - Linting or formatting checks must succeed (e.g., `black`, `flake8`).
  - Docker build must complete successfully (if applicable).
  
Example required checks (customize per CI setup):
- `test-object-detection`
- `docker-build-success`
- `code-style-check`

---

## Require Pull Request Reviews

- **At least one (1)** approved review is required before merging.
- **Code review includes functional and stylistic feedback.**
- **Dismiss stale pull request approvals when new commits are pushed.**

---

##  Prevent Force Pushes

- Force pushes are **not allowed** on the `main` branch.
- Rewrites and history edits are disabled.

---

## Require Linear History

- Enforce linear commit history (no merge commits).
- Recommended practice: Rebase and squash commits before merging.

---

## Test Coverage (Optional)

If code coverage tools are integrated (e.g., `pytest-cov`, Codecov):

- Ensure at least **80% code coverage** on new features.
- Code with <80% coverage may require justification or further testing.

---

## Recommended Workflow

1. Create a feature branch (e.g., `feature/api-refactor`).
2. Push commits and open a pull request targeting `main`.
3. Request a review.
4. Ensure all tests and checks pass.
5. Once approved, rebase (if needed) and squash commits.
6. Merge the pull request into `main`.

---

## Dependency Updates

- Dependency version updates should be handled in dedicated branches (e.g., `chore/update-deps`).
- Run full test suite after any upgrade to `ultralytics`, `fastapi`, or `torch`.

---

## Related Files

- [`Dockerfile`](../Dockerfile)
- [`test_object_detection.py`](../test_object_detection.py)
- [`LICENSE`](../LICENSE)
- [`README.md`](../README.md)

---

> This ruleset may evolve as the project scales or CI integrations change. For updates, check the [repository settings](https://github.com/edanurarslan/Dockerized-Object-Detection-with-YOLOV8/settings/branches).
