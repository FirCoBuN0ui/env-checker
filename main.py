import sys
import importlib.util

default_packages = ["requests", "pandas", "numpy"]
packages = sys.argv[1:] if len(sys.argv) > 1 else default_packages

print("Python version:", sys.version.split()[0])
print("Package check:")
for pkg in packages:
    ok = importlib.util.find_spec(pkg) is not None
    print(f"- {pkg}: {'installed' if ok else 'not installed'}")