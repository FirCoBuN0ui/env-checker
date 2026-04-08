import sys
import importlib.util
from pathlib import Path

DEFAULT_PACKAGES = ["requests", "pandas", "numpy"]

HELP_TEXT = """
env-checker: check whether Python packages are installed.

Usage:
  python main.py                         # check default packages
  python main.py requests flask          # check given packages
  python main.py -f requirements.txt     # check packages from file
  python main.py --help                  # show help
""".strip()


def is_installed(pkg_name: str) -> bool:
    return importlib.util.find_spec(pkg_name) is not None


def normalize_packages(raw_args: list[str]) -> list[str]:
    seen = set()
    result = []
    for p in raw_args:
        p = p.strip()
        if not p:
            continue
        if p not in seen:
            seen.add(p)
            result.append(p)
    return result


def parse_requirement_name(line: str) -> str:
    """
    支持简单 requirements 行：
    requests==2.32.3 -> requests
    pandas>=2.0      -> pandas
    numpy            -> numpy
    忽略注释和空行
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return ""

    # 去掉行内注释
    if "#" in line:
        line = line.split("#", 1)[0].strip()

    # 去掉常见版本符号后的部分
    for sep in ["==", ">=", "<=", "~=", "!=", ">", "<"]:
        if sep in line:
            line = line.split(sep, 1)[0].strip()
            break

    return line


def load_packages_from_file(file_path: str) -> list[str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    packages = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        name = parse_requirement_name(raw)
        if name:
            packages.append(name)

    return normalize_packages(packages)


def resolve_packages(args: list[str]) -> list[str]:
    if not args:
        return DEFAULT_PACKAGES

    if "-f" in args:
        idx = args.index("-f")
        if idx + 1 >= len(args):
            raise ValueError("'-f' requires a file path, e.g. -f requirements.txt")
        file_path = args[idx + 1]
        return load_packages_from_file(file_path)

    return normalize_packages(args)


def main():
    args = sys.argv[1:]

    if any(a in ("-h", "--help") for a in args):
        print(HELP_TEXT)
        return 0

    try:
        packages = resolve_packages(args)
    except Exception as e:
        print(f"Error: {e}")
        return 2

    if not packages:
        print("No valid packages to check.")
        return 2

    print("Python version:", sys.version.split()[0])
    print(f"Checking {len(packages)} package(s): {packages}")
    print("-" * 40)

    installed_count = 0
    for pkg in packages:
        ok = is_installed(pkg)
        if ok:
            installed_count += 1
        print(f"- {pkg}: {'installed' if ok else 'not installed'}")

    print("-" * 40)
    print(f"Summary: {installed_count}/{len(packages)} installed")

    return 0 if installed_count == len(packages) else 1


if __name__ == "__main__":
    raise SystemExit(main())