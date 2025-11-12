import subprocess
import sys


def test_imports():
    __import__("granpost")


def test_cli_help():
    try:
        subprocess.run(["granpost", "--help"], check=True)
    except FileNotFoundError:
        subprocess.run([sys.executable, "-m", "granpost.cli", "--help"], check=True)
