import sys
import importlib.util

packages = ["requests", "pandas", "numpy"]

print("Python version:", sys.version.split()[0])
print("Package check:")
for pkg in packages:
    ok = importlib.util.find_spec(pkg) is not None
    print(f"- {pkg}: {'installed' if ok else 'not installed'}")