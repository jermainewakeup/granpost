from pathlib import Path

# --- Paths ---
REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_OUT = REPO_ROOT / "data" / "output"
PROFILES_FILE = DATA_OUT / "profiles.json"


def main() -> None:
    print("test")


if __name__ == "__main__":
    main()
