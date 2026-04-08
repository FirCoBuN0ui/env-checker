# env-checker

A tiny Python starter project to verify local environment and package availability.

## What it does

- Prints current Python version
- Checks whether specified packages are installed
- Supports loading package names from a file (`-f`)
- Supports machine-readable JSON output (`--json`)

## Run

```bash
python main.py
python main.py requests flask
python main.py -f requirements.txt
python main.py requests flask --json
```

## Example output (text mode)

```text
Python version: 3.13.5
Checking 2 package(s): ['requests', 'flask']
----------------------------------------
- requests: installed
- flask: not installed
----------------------------------------
Summary: 1/2 installed
```

## Example output (JSON mode)

```bash
python main.py requests flask --json
```

```json
{
  "python_version": "3.13.5",
  "checked_packages": 2,
  "installed": ["requests"],
  "missing": ["flask"],
  "summary": {
    "installed_count": 1,
    "missing_count": 1,
    "all_installed": false
  }
}
```

## Exit codes

- `0`: all checked packages are installed
- `1`: at least one checked package is not installed
- `2`: invalid input or runtime error (for example: missing `-f` file path, file not found, or no valid packages to check)

## CI

GitHub Actions runs `pytest` automatically on every push and pull request.
Workflow file: `.github/workflows/ci.yml`