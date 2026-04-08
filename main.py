import sys
import importlib.util

DEFAULT_PACKAGES = ["requests", "pandas", "numpy"]

HELP_TEXT = """
env-checker: check whether Python packages are installed.

Usage:
  python main.py                # check default packages
  python main.py requests flask # check given packages
  python main.py --help         # show help
""".strip()


def is_installed(pkg_name: str) -> bool:
    return importlib.util.find_spec(pkg_name) is not None


def normalize_packages(raw_args: list[str]) -> list[str]:
    # 去重且保持顺序
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


def main():
    args = sys.argv[1:]

    if any(a in ("-h", "--help") for a in args):
        print(HELP_TEXT)
        return 0

    packages = normalize_packages(args) if args else DEFAULT_PACKAGES

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

    # 关键：给自动化环境返回退出码
    return 0 if installed_count == len(packages) else 1


if __name__ == "__main__":
    raise SystemExit(main())