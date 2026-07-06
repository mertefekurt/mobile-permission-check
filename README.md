<p align="center">
  <img src="assets/readme-cover.svg" alt="Mobile Permission Check cover" width="100%" />
</p>

# Mobile Permission Check

![stack](https://img.shields.io/badge/stack-Python-0891b2?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-b45309?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-be185d?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-4b5563?style=flat-square)

Audit mobile app permission notes for broad access and missing justification.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `mobile-permission-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
mobile-permission-check examples/sample.txt
mobile-permission-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `missing-justification` | high | permission justification missing |
| `always-location` | medium | always location permission requested |
| `background-enabled` | low | background behavior enabled |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
permission location_always justification missing background true
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m mobile_permission_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Mobile Permission Check policy easy to review.
