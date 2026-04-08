import subprocess
import sys


def run_cmd(args: list[str]):
    return subprocess.run(
        [sys.executable, "main.py", *args],
        capture_output=True,
        text=True,
    )


def test_file_not_found_returns_2_and_prints_error():
    result = run_cmd(["-f", "not_exist.txt"])
    assert result.returncode == 2
    assert "Error:" in result.stdout



def test_file_normalize():
    result = run_cmd(["requests", "requests", "flask"])
    assert "Checking 2 package(s)" in result.stdout
    assert "- requests: installed" in result.stdout


def test_help_returns_0_and_shows_usage():
    result = run_cmd(["--help"])
    assert result.returncode == 0
    assert "Usage:" in result.stdout