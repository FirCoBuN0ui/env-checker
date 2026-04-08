# env-checker

A tiny Python starter project to verify local environment and package availability.

## What it does
- Prints current Python version
- Checks whether specific packages are installed (`requests`, `pandas`, `numpy`)

## Run

```bash
python main.py
```

## Example output

```text
Python version: 3.13.5
Package check:
- requests: installed
- pandas: not installed
- numpy: not installed
```
## Exit codes

- `0`: all checked packages are installed
- `1`: at least one checked package is not installed