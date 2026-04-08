import subprocess
import sys
import json

def test_json_mode_outputs_valid_json():
    result = run_cmd(["requests", "--json"])
    assert result.returncode in (0, 1)  # requests 一般已安装，保险写法
    data = json.loads(result.stdout)
    assert "python_version" in data
    assert "checked_packages" in data
    assert "installed" in data
    assert "missing" in data
    assert "summary" in data



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


def test_file_lost_returns_2_and_prints_error():
    result = run_cmd(["-f"])
    assert result.returncode == 2
    assert "requires a file path" in result.stdout



def test_empty_file_returns_2_and_shows_usage(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("", encoding="utf-8")  # 关键：真正创建空文件

    result = run_cmd(["-f", str(empty_file)])
    assert result.returncode == 2
    assert "No valid packages to check." in result.stdout
