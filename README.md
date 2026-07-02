# mobile-permission-check

> Audit mobile app permission notes for broad access and missing justification.

## Risk note Overview

Audit mobile app permission notes for broad access and missing justification. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 34

Accepts mobile permission manifest. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 34

```bash
python -m pip install -e ".[dev]"
mobile-permission-check examples/sample.txt
mobile-permission-check examples/sample.txt --json --fail-on medium
python -m mobile_permission_check --help
```

## Rule Surface 34

| Rule | Severity | Meaning |
|---|---:|---|
| `missing-justification` | high | permission justification missing |
| `always-location` | medium | always location permission requested |
| `background-enabled` | low | background behavior enabled |

## Validation Notes 34

```bash
ruff check .
pytest
python -m mobile_permission_check --help
```

Example risky input:

```text
permission location_always justification missing background true
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
